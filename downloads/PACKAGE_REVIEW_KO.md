# 사용자 수정본 검토 결과 (2026-10-08)

## 결론

사용자가 직접 정리한 두 업로드 ZIP을 각각 기준으로 보완했습니다.
실제 사용용 127개, GitHub용 52개의 원본 파일을 모두 유지했습니다.
주문 앱·런치·학습 코드 및 데이터는 변경하거나 추가 삭제하지 않았습니다.
GitHub용 루트 폴더 이름에 있던 공백은 제거하고 두 ZIP의 루트 이름을 구분했습니다.

## 실행 경로: 사용자 수정 유지

- `llm/start_app.sh`: 스크립트가 있는 폴더로 이동한 뒤 앱을 실행합니다.
- `llm/soomac_io.launch.py`: `__file__` 기준으로 같은 폴더의 STT/TTS 파일을 찾습니다.
- 두 런치 대상 파일이 실제로 포함되어 있습니다. 런치 구성 검사는 ROS 객체를 대체하여 경로만 확인했습니다.
- `~/drive_thru_venv`와 `~/drive_thru_llm/outputs/qwen35_drive_thru_v14_merged`는 외부 경로입니다. 기존 Ubuntu에 해당 환경/모델이 필요합니다.
- 실제 실행 스크립트 이름은 `start_app.sh`입니다(`start_app.py`가 아님).

프로젝트 루트에서 앱 실행:

```bash
bash llm/start_app.sh
```

ROS2 환경을 설정한 터미널에서 IO 브리지 실행:

```bash
ros2 launch "$(pwd)/llm/soomac_io.launch.py"
```

이 ROS 런치는 STT UDP 브리지와 TTS publisher를 실행합니다. vLLM이나 주문 앱을 대신 실행하지 않습니다.
vLLM이 이미 실행 중이면 그대로 사용하세요. 중지된 경우에만 별도 터미널에서
`bash llm/start_vllm.sh`로 실행합니다. 이 클라우드 검토에서는 기존 프로세스를 조작하지 않았습니다.

## 누락 보완 및 문서 수정

두 업로드 모두 `stt/stt_clova_ver_7.py`가 import하는 `nest_pb2.py`, `nest_pb2_grpc.py`가 없었습니다.
실제 사용용에는 `nest.proto`로 생성한 두 파일을 추가했습니다.
GitHub용에는 `.gitignore` 방침에 맞춰 명세와 `stt/generate_proto.py`를 넣었습니다.
GitHub용에서 CLOVA를 쓰려면 먼저 생성 스크립트를 실행해야 합니다.
두 버전 모두 `stt/README.md`에 명령과 의존성을 안내했습니다.
Qwen STT를 사용하는 주문 앱에는 이 CLOVA 전용 생성 과정이 필요하지 않습니다.

GitHub README의 오래된 “프로젝트/ROS 절대경로가 남아 있다”는 설명도 현재 코드에 맞췄습니다.
각 ZIP의 `PACKAGE_FILE_AUDIT.json`에서 원본 대비 추가·수정·삭제 목록과 파일 SHA-256을 확인할 수 있습니다.

## 구성 차이와 보관 기준

- 실제 사용용: 사용자가 남긴 테스트·학습·평가 데이터와 STT 비교 도구까지 유지했습니다.
- GitHub용: 실행 코드, UI, 런치, STT 코드 중심입니다. 테스트·학습 데이터를 뺀 것은 의도된 차이입니다.
- 캐시·백업·가상환경·모델 가중치·인증 파일은 이 배포물에 넣지 않았습니다.
- 개인 `stt/env.sh`가 Ubuntu에 있다면 기존 백업과 함께 보관하세요. 예제 파일은 실제 키를 포함하지 않습니다.
- `router_gold_regressions_39_prompt_before_criteria.json`은 과거 평가 결과이며 실행 필수 파일이 아닙니다. 삭제하면 해당 평가 이력만 사라집니다.
- `make_dataset_v14.py`로 데이터를 처음부터 재생성하려면 별도 `dataset_v13/`이 필요합니다. 이번 업로드 및 이전 검토본에도 없었습니다. 현재 포함된 `dataset_v14/`를 사용하는 실행과는 별개입니다.
- `eval_v14.py`의 과거 V12/V13 평가 세트도 별도 보관 데이터가 있어야 합니다. 현재 ZIP만으로 과거 평가 전체를 재현할 수는 없습니다.

## 검증 결과

- 실제 사용용 주문 처리 테스트: **270 passed**.
- GitHub용 코드에 동일한 외부 테스트 적용: **270 passed**. 실제 import 대상 경로도 GitHub용으로 확인했습니다.
- 기존 오프라인 회귀 스크립트 10개: **9개 통과 / 1개 실패**.
- 남은 실패: `test_safety_final_v14.py`의 `ㅋㅋㅋㅋ` 차단 assertion. 기존 업로드에서도 알려진 문제이며, 파일 정리로 생긴 누락은 아닙니다. 이번에는 사용자 주문 로직을 바꾸지 않았습니다.
- Python 문법 검사: 실제 사용용 76개 / GitHub용 35개 파일 통과.
- 두 버전의 셸 스크립트 문법, UI 참조 파일, 런치 대상 경로 검사 통과.
- CLOVA protobuf 재생성 일치, 직렬화·역직렬화, 로컬 gRPC stub 생성 확인. 실제 API 요청은 보내지 않았습니다.
- 핵심 앱 파일 6개(실제 사용용 기준)는 기존 최신 `modifier_patch/files`와 바이트 단위로 일치합니다.
- 실제 ROS2 기동, GPU/vLLM 추론, 마이크 입력, CLOVA 서버 인증은 여기서 검증하지 않았습니다.

Ubuntu에서 주문 처리 테스트 재실행(실제 사용용):

```bash
cd llm
source ~/drive_thru_venv/bin/activate
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python3 -m pytest -q test_modifier_selection.py
```

ROS의 `launch_testing` 플러그인과 pytest 버전 충돌을 피하기 위해 자동 플러그인 로딩을 끕니다.

## 교체 전 확인

압축은 기존 폴더 위에 덮어 풀지 말고 새 폴더에 먼저 푸세요. 덮어 풀면 예전 파일은 남습니다.
기존 프로젝트 폴더는 통째 백업하고, 외부 가상환경·모델·개인 인증 파일을 유지하세요.
현재 실행 중인 앱은 파일 교체만으로 코드가 바뀌지 않습니다. 새 폴더에서 앱을 다음 실행할 때 반영됩니다.
