# 버거 modifier 수정본

업로드된 최신 `llm.zip`을 기준으로 수정했습니다. 사용자님 Ubuntu의 원본에는 아직 적용되지 않았습니다.

## 변경 파일

- `drive_thru_app.py`: modifier 요청과 특징 답변 구별, 공통 selector 연결, pending 유지/교체/초기화, 구형 modifier rewrite 호출 제거, 번호 표시를 실제 line_id로 일치. 기존 `process_prebuilt()` 적용 경로 재사용.
- 세트 음료 변경 가격 질문은 음료별 전체 크기 가격 목록 대신 추가금만 간단히 안내합니다.
- `modifier_selection.py` (신규): 메뉴 그룹 UNION, 그룹 내부 특징 AND, 그룹별 앞 N개 선택, 번호·순번·메뉴·특징 혼합 선택. 잘못된 조건이나 개수가 있으면 부분 적용하지 않음.
- `order_schema.py`: 주문 수정용 `Exclude.CHEESE` 제거. 이미 반영된 `Topping.PATTY` 유지. 메뉴 정보 조회용 `IngredientCriterion.CHEESE`는 유지.
- `router_fastpath.py`: 토핑 capability의 기존 tomato 목록을 patty로 정정. 재료 제외용 tomato는 유지.
- `test_modifier_selection.py` (신규): 270개 targeted test. 세트 가격 조회 회귀 테스트 포함.
- 세트 업그레이드 가격 안내: 음료 사이즈와 사이드 변경 질문에 단품 가격 대신 증분 요금을 안내합니다.

Router policy와 프롬프트, 모델, Runtime 상태 적용 구현, 일반 quantity 로직은 변경하지 않았습니다. 구형 helper 정의는 다른 참조를 보존하기 위해 남겨두었지만 메인 루프의 중복 modifier rewrite 호출은 제거했습니다.

## 알레르기·버거 재료 질문

- `menu_knowledge.py`의 메뉴별 속재료를 사용자 제공 구성으로 수정했습니다. 이 파일도 해시 확인과 백업 후 적용합니다.
- 공통 속재료: 패티, 양상추, 토마토, 양파, 피클, 소스. 불고기버거는 불고기 소스, 치즈버거는 치즈를 추가하고, 새우·치킨버거는 패티를 각각 새우패티·치킨패티로 안내합니다.
- 새우·갑각류 알레르기에는 새우버거를 제외하고 불고기버거·치즈버거·치킨버거를 추천합니다. 원재료와 조리 중 교차접촉 여부는 직원 확인을 안내하며, 안전을 보장하지 않습니다. 다른 알레르기까지 함께 언급하면 기존 직원 확인 안내를 유지합니다.
- `여기 무슨 가게예요?`에는 햄버거 가게라고 답하고, `나 뭐 주문하면 돼?`에는 햄버거·사이드·음료 주문을 안내합니다. 이 질문들은 주문 상태를 바꾸지 않습니다.
- 버거 종류 없이 속재료를 물으면 먼저 불고기버거·치킨버거·치즈버거·새우버거 중 어떤 메뉴인지 묻습니다. 다음 답변으로 버거명을 받으면 해당 메뉴에 등록된 기본 재료만 설명합니다.
- 예: `햄버거 속재료 뭐 들어가요?` → 버거 종류를 질문 → `치즈버거요` → 치즈버거 기본 재료 안내.

## 대상 답변 뒤 반복 요청 처리

`패티 추가해주세요` 다음 `베이컨 추가한 치킨버거에 추가해주세요`라고 답하면 베이컨이 이미 들어간 치킨버거를 선택해 패티를 추가합니다. 새 주문으로 오인해 대기 중인 변경 요청을 지우던 문제를 수정했습니다. 후보가 두 개면 개수나 번호를 다시 확인하며, `둘 다`로 두 후보를 선택할 수 있습니다. 새 버거 주문은 기존 주문 경로로 처리합니다.

## 일부 메뉴명 입력

`튀김`, `치즈`, `감자`, `스틱` 및 `튀김 하나 주세요` 같은 불완전한 메뉴명은 주문을 변경하지 않고 정확한 이름을 다시 묻습니다. `감자튀김`, `치즈스틱`, `치즈버거` 같은 완전한 메뉴명과 명시적인 `치즈 추가해주세요` 토핑 요청은 기존 경로로 처리합니다.

## Ubuntu에 적용

압축을 프로젝트 바깥의 별도 폴더에 풉니다. 해당 폴더에서 다음을 실행합니다.

```bash
python3 apply_patch.py --target ~/soomac_3.0-IRC_ASZ/llm --check
python3 apply_patch.py --target ~/soomac_3.0-IRC_ASZ/llm
```

기존에 GitHub에서 받은 패치 폴더를 쓰고 있다면 먼저 저장소에서 `git pull origin main`을 실행합니다. 적용기는 업로드 당시 원본과 이전 버전 패치의 SHA-256을 검사합니다. 수정할 기존 파일을 `modifier_backup_날짜_시간/`에 백업한 뒤 필요한 파일을 업데이트합니다. 알 수 없는 로컬 변경이 있으면 덮어쓰지 않고 중단합니다. 어떤 프로세스도 종료하거나 재시작하지 않습니다.

앱이 이미 실행 중이면 파일 적용만으로 실행 중 Python 코드가 바뀌지는 않습니다. 앱의 다음 실행부터 수정본이 사용됩니다. **8000번 vLLM은 그대로 두세요.**

## 검증 결과

- 정적 컴파일 및 schema import 확인: 통과.
- `python -m pytest -xq test_modifier_selection.py`: **270 passed**.
- 네 operation × 전체 지원 재료 × 번호·메뉴·복수 메뉴·개수·전부·세트 특징 등을 실제 `RuntimeWorker → OrderUpdate.model_validate → OrderStateManager.apply`로 검증.
- CASE A~F: 실제 `app.main()`에서도 검증. UI·STT 입출력과 초기 세션만 테스트용으로 대체했고, Router 및 구형 rewrite 호출이 0회인지 assertion으로 확인.
- 패티 +900원, 중복 방지, 없는 토핑/제외의 임의 재지정 방지, 수량 보존, 새 요청 교체, 세션 초기화, 비연속 line_id 검증 포함.
- “음료 사이즈랑 사이드 변경은 각각 얼마예요?”는 스몰 +0원, 미디엄 +300원, 라지 +700원, 치즈스틱 변경 +500원 및 아이스커피 변경 +500원을 안내. 일반 사이드 가격 질문은 감자튀김 2,000원·치즈스틱 2,500원을 계속 안내.
- “음료는 변경 얼마예요?”에는 세트 음료 변경 추가금만 안내: 콜라·제로콜라·스프라이트·환타 추가금 없음, 아이스커피 +500원.
- 기존 오프라인 회귀 스크립트 10개 중 **9개 통과**. `test_safety_final_v14.py`는 `ㅋㅋㅋㅋ` 입력을 차단해야 한다는 line 163 assertion에서 실패. 업로드 원본에서도 동일하게 재현한 기존 문제이며 수정하지 않았음.
- 기존 `app_regression_smoke3.json`: **1 PASS / 2 FAIL**. T001/T004는 최초 주문의 Router 요청에서 `127.0.0.1:8000` 연결 거부로 실패. T073은 통과. 이 클라우드에는 사용자님 로컬 vLLM이 연결되지 않았으므로 전체 live regression 완료로 볼 수 없음.

검증 환경: Python 3.12, pydantic 2.13.5, pytest 9.1.1. 결과는 `validation/`에 포함되어 있습니다. `changes.diff`는 변경 검토용이며 적용에 Git이 필요하지 않습니다.

## 로컬에서 남은 테스트

```bash
cd ~/soomac_3.0-IRC_ASZ/llm
source ~/drive_thru_venv/bin/activate
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q test_modifier_selection.py

export SOOMAC_LLM_URL="http://127.0.0.1:8000/v1"
export SOOMAC_ROUTER_URL="http://127.0.0.1:8000/v1"
export SOOMAC_ROUTER_MODEL="drive-thru-v14"
export SOOMAC_ROUTER_THINKING="off"
export SOOMAC_ROUTER_TELEMETRY=0
python run_app_regression.py regression_cases/app_regression_smoke3.json 120
python run_app_regression.py
```

pytest가 없다면 활성화한 가상환경에서 `python -m pip install pytest`가 필요합니다. `run_app_regression.py`는 실패가 있어도 프로세스 종료 코드가 0일 수 있으므로 출력의 PASS/FAIL 및 생성된 결과 JSON을 확인해야 합니다. 오래된 회귀 기대값에는 tomato 토핑이나 과거 안내 문구가 남아 있을 수 있으며, 성공으로 맞추려고 기존 테스트를 수정하지 않았습니다.

실제 vLLM을 이용한 전체 앱 검증은 아직 완료되지 않았습니다.
