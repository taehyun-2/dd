# 직원 화면: 최근 확정 주문 4건

직원 화면은 주문별로 4개의 세로 칸을 나란히 보여줍니다.
주문 1·2·3·4가 보이는 상태에서 5가 확정되면 2·3·4·5로 바뀝니다.
화면에서 사라진 주문의 handoff 파일을 삭제하거나 메인 노드 주문을 취소하지는 않습니다.

각 칸에는 고객 접수 누적번호, 간략한 메뉴·수량, 확정 총액을 표시합니다.
일반 주문은 같은 메뉴/단품·세트/음료 크기별로 묶고 세트 구성·토핑·제외는 설명에서 생략합니다.
확정 총액은 옵션 추가금이 포함된 checkout 결과를 그대로 사용합니다.
맥오더는 누적번호와 “맥오더 58번” 같은 예약번호를 구분하고 상세 메뉴를 임의로 표시하지 않습니다.

확정 주문의 `llm/runtime_data/handoffs/handoff_N.json` 파일이 이력의 기준입니다.
진행 중인 주문·단순 번호 확인·취소된 주문은 이력에 추가하지 않습니다.
다음 차량이 들어오거나 브라우저를 새로고침해도, 파일이 남아 있으면 최근 4건이 복원됩니다.
`/resetall`로 handoff 파일을 지우면 해당 UI 이력도 사라집니다. 이미 PUB한 메인 노드 주문과는 별개입니다.

직원 호출 알림은 그대로 표시됩니다. 네트워크 연결이 끊기면 마지막 보드를 남기고 재연결을 시도합니다.
데스크톱은 4열을 한 화면에 표시하며, 좁은 휴대전화 화면은 4열을 유지하면서 가로 스크롤합니다.

## 바뀐 실행 파일

직전 `*_renumbered.zip` 대비 아래 4개 파일만 실행 코드에 추가/수정됐습니다.

- 수정: `llm/ui/staff.html`
- 수정: `llm/ui/staff.js`
- 수정: `llm/ui_runtime_bridge.py`
- 추가: `llm/staff_order_history.py`

실사용용에는 `llm/test_staff_order_history.py`도 추가했습니다. GitHub용에는 테스트를 넣지 않았습니다.
고객 화면의 HTML/JS, 주문 처리, ROS PUB, 런치 코드는 이 작업에서 변경하지 않았습니다.

## 적용

기존 프로젝트를 백업한 후 위 4개 실행 파일을 함께 반영하세요. 앱을 다음 실행할 때 적용됩니다.
기존 `llm/runtime_data/handoffs/`는 유지해야 기존 접수 순번과 최근 주문이 이어집니다.
새 폴더에서 실행하려면 그 폴더에도 기존 handoff 이력을 함께 옮겨야 합니다.
vLLM과 ROS IO 런치를 재시작할 필요는 없습니다. 브라우저에서는 Ctrl+Shift+R로 새 화면을 불러오세요.
주소는 기존 `http://127.0.0.1:8080/staff.html`입니다.

## 검증

실사용용 관련 테스트 330개, GitHub용 코드 외부 테스트 310개 통과.
실제 Chromium에서 초기 빈 화면, 4칸 정렬, 5번째 주문 전환, 새로고침, 여러 탭,
맥오더 표시, 직원 호출, 좁은 화면과 JavaScript 오류 없음까지 확인했습니다.
확정 handoff를 사용하는 HTTP/UI 검증이며 실제 로봇·ROS DDS·마이크/GPU를 실행한 것은 아닙니다.

```bash
cd llm
source ~/drive_thru_venv/bin/activate
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python3 -m pytest -q test_staff_order_history.py test_line_renumber.py test_individual_items.py test_modifier_selection.py test_main_order_publish.py
```
