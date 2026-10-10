# 원본 대비 전체 파일 변경 목록

기준: 처음 업로드한 `soomac_3.0-IRC_ASZ.zip` → 최신 `*_staff_board.zip`.
2026-10-10 직원 UI 4칸 변경까지 포함한 전체 비교입니다. 바로 전 renumbered 버전과의 차이는 아래 직원 UI 항목에 따로 표시합니다.

첫 IRC ZIP 847개 → 실사용용 143개: 수정 10개, 추가 16개, 동일 117개, 배포 제외 720개.
“배포 제외”는 수정본 ZIP에서 빠졌다는 뜻입니다. 원본 업로드를 지웠다는 뜻은 아닙니다.

## 첫 IRC ZIP 이후 수정된 파일 전부

| 경로 | 변경 및 주체 |
|---|---|
| `README.md` | 검토 및 실행 안내 링크 추가 |
| `llm/checkout_manager.py` | 확정 주문을 ROS 발행 대기열에 기록; 누적 주문번호 유지 |
| `llm/drive_thru_app.py` | handoff 저장 경로를 파일 위치 기준으로 고정; /resetall 다음 번호 표시 수정 |
| `llm/order_runtime_final.py` | 취소 후 메뉴 항목 번호를 1부터 재정렬; 옵션 그룹/선택 대기/최근 선택 번호 함께 변환 |
| `llm/soomac_io.launch.py` | 사용자의 상대 경로 수정 유지 + 주문 결과 ROS publisher 실행 추가 |
| `llm/start_app.sh` | 사용자가 프로젝트 작업 경로를 스크립트 위치 기준으로 변경; assistant는 유지 |
| `llm/test_individual_items.py` | 취소 후 다음 항목 번호 테스트를 새 번호 정리 요구사항에 맞춤 |
| `llm/ui/staff.html` | 직원 화면을 최근 주문 4개 가로 열로 재구성 |
| `llm/ui/staff.js` | 확정 주문 4개 메뉴·수량·금액 렌더링과 5번째 주문 전환 |
| `llm/ui_runtime_bridge.py` | 직원 화면용 최근 확정 주문 조회 API 추가; 기존 고객 API 유지 |

## 첫 IRC ZIP 이후 추가된 파일 전부

- `LINE_NUMBERING_KO.md`
- `PACKAGE_FILE_AUDIT.json`
- `PACKAGE_REVIEW_KO.md`
- `ROS_ORDER_PUB_KO.md`
- `STAFF_BOARD_KO.md`
- `integration/main_node_mcorder_tts.patch`
- `llm/main_order_payload.py`
- `llm/order_result_publisher.py`
- `llm/staff_order_history.py`
- `llm/test_line_renumber.py`
- `llm/test_main_order_publish.py`
- `llm/test_staff_order_history.py`
- `stt/README.md`
- `stt/generate_proto.py`
- `stt/nest_pb2.py`
- `stt/nest_pb2_grpc.py`

## 더 앞선 최초 llm.zip부터의 누적 코드 변경

처음 IRC ZIP에는 이전 modifier·메뉴 수정이 이미 반영되어 있었습니다. 첫 IRC ZIP 비교만 하면 이 부분이 빠집니다.
아래는 최초 `llm.zip`부터 마지막 전달본까지 변경된 기존 코드 파일 전부입니다.

- `llm/checkout_manager.py`
- `llm/drive_thru_app.py`
- `llm/menu_knowledge.py`
- `llm/order_runtime_final.py`
- `llm/order_schema.py`
- `llm/router_fastpath.py`
- `llm/soomac_io.launch.py`
- `llm/start_app.sh`
- `llm/test_individual_items.py`
- `llm/ui/staff.html`
- `llm/ui/staff.js`
- `llm/ui_runtime_bridge.py`

이 중 `start_app.sh`의 경로 수정은 사용자가 했습니다. `soomac_io.launch.py`의 상대경로는 사용자가, 주문 publisher 추가는 assistant가 했습니다.
추가된 LLM 코드/테스트 전부:

- `llm/main_order_payload.py`
- `llm/modifier_selection.py`
- `llm/order_result_publisher.py`
- `llm/staff_order_history.py`
- `llm/test_line_renumber.py`
- `llm/test_main_order_publish.py`
- `llm/test_modifier_selection.py`
- `llm/test_staff_order_history.py`

STT 쪽에서 assistant가 추가한 코드는 `stt/generate_proto.py`, `stt/nest_pb2.py`, `stt/nest_pb2_grpc.py`입니다.
생성 스크립트와 proto는 GitHub용에도 있지만 생성 파일 2개는 실제 사용용에만 포함합니다.

## GitHub용과의 차이

GitHub용은 사용자가 원한 대로 테스트·학습/평가 데이터·일부 개발 도구를 제외합니다.
첫 IRC ZIP 대비 GitHub용에서 수정된 기존 파일 전부:

- `.gitignore`
- `README.md`
- `llm/README.md`
- `llm/checkout_manager.py`
- `llm/drive_thru_app.py`
- `llm/order_runtime_final.py`
- `llm/soomac_io.launch.py`
- `llm/start_app.sh`
- `llm/ui/staff.html`
- `llm/ui/staff.js`
- `llm/ui_runtime_bridge.py`

첫 IRC ZIP 대비 GitHub용에 추가된 파일 전부:

- `LINE_NUMBERING_KO.md`
- `PACKAGE_FILE_AUDIT.json`
- `PACKAGE_REVIEW_KO.md`
- `ROS_ORDER_PUB_KO.md`
- `STAFF_BOARD_KO.md`
- `integration/main_node_mcorder_tts.patch`
- `llm/main_order_payload.py`
- `llm/order_result_publisher.py`
- `llm/staff_order_history.py`
- `stt/README.md`
- `stt/generate_proto.py`

## 정리 단계별 구분

- 처음 IRC ZIP 847개 → 초기 정리본 226개: 남긴 파일의 내용 변경 없음. 621개 제외(백업/이전 사본 239, Git 내부 이력 193, 중첩 패치 저장소 115, 캐시 73, 중복 llm.zip 1).
- 초기 정리본 226개 → 사용자가 직접 올린 실사용용 127개: 99개를 사용자가 추가 제외했고 start_app.sh/soomac_io.launch.py의 경로를 수정.
- 그 사용자의 수정본을 기준으로 CLOVA 준비 파일, PUB 기능, 연속 항목 번호 등을 보완하여 직전 실사용용 140개가 됨.
- 이번 직원 UI 작업에서 실행 모듈·테스트·안내서 3개가 추가되어 최신 실사용용 143개가 됨.

## 직원 UI 후속 작업

직전 renumbered 전달본까지는 `llm/ui/staff.html`, `llm/ui/staff.js`, `llm/ui_runtime_bridge.py`를 원본 그대로 유지했습니다.
이번 최근 주문 4칸 UI 작업에서 이 3개를 수정하고 `llm/staff_order_history.py`, 실사용용 `llm/test_staff_order_history.py`를 추가했습니다.
이번 UI 작업 전 기준으로는 첫 IRC ZIP 대비 기존 파일 수정 7개/신규 13개였고, 지금은 수정 10개/신규 16개입니다.
직전 renumbered ZIP 대비 비교표는 최신 ZIP 내부 `PACKAGE_FILE_AUDIT.json`에서 확인할 수 있습니다.

## 팀 메인 노드 / 모델

- 팀 GitHub의 `src/irc_main/irc_main/main_node.py`와 로봇팔 코드는 직접 수정/푸시하지 않았습니다. 맥오더 발화 1줄 수정용 patch만 동봉했습니다.
- 학습된 V14 모델 가중치, 사용자 Ubuntu 가상환경, 실행 중 vLLM은 수정하지 않았습니다.
- 첫 IRC 업로드 ZIP에는 `src/`와 `tts/`가 들어 있지 않았습니다. 이 폴더들은 이후 팀 GitHub에서 읽어 확인한 별도 자료입니다.

## 실사용용에서 제외된 전체 720개 경로

### 초기 정리 단계 제외 (621개)

```text
.git/COMMIT_EDITMSG
.git/FETCH_HEAD
.git/HEAD
.git/ORIG_HEAD
.git/config
.git/description
.git/hooks/applypatch-msg.sample
.git/hooks/commit-msg.sample
.git/hooks/fsmonitor-watchman.sample
.git/hooks/post-update.sample
.git/hooks/pre-applypatch.sample
.git/hooks/pre-commit.sample
.git/hooks/pre-merge-commit.sample
.git/hooks/pre-push.sample
.git/hooks/pre-rebase.sample
.git/hooks/pre-receive.sample
.git/hooks/prepare-commit-msg.sample
.git/hooks/push-to-checkout.sample
.git/hooks/update.sample
.git/index
.git/info/exclude
.git/logs/HEAD
.git/logs/refs/heads/backup/desktop-ros-stt
.git/logs/refs/heads/feature/llm
.git/logs/refs/heads/feature/ui
.git/logs/refs/heads/feature/ui-runtime-integration
.git/logs/refs/heads/fix/llm-runtime-guards
.git/logs/refs/heads/main
.git/logs/refs/remotes/origin/HEAD
.git/logs/refs/remotes/origin/feature/llm
.git/logs/refs/remotes/origin/feature/ui-runtime-integration
.git/logs/refs/remotes/origin/fix/llm-runtime-guards
.git/logs/refs/remotes/origin/main
.git/objects/02/15e6e5d64a4327687c672f695ab9efc9bcff50
.git/objects/03/1d16b2eb60b3cf80a21f00e35d70fb47c814b2
.git/objects/05/c347d05981e9410a03baff320cc5365e58dcb3
.git/objects/08/edfd2db12770b54f406384217e28435e92c667
.git/objects/0f/26f8dd96db8b9b6811069904236ddb9198fdff
.git/objects/0f/524af4c66544426ff57576785fa2c1ca7cb447
.git/objects/0f/b4a97a0f33e9cb745fa380777489add72c5b95
.git/objects/12/7012ca309416f4e561e6050176544a992c716a
.git/objects/14/ca4e2a621bd6da94844cd77767594656faf65c
.git/objects/15/c20cf2d6bd9bfd429a6c6c4b54ff6bfc39b819
.git/objects/17/8dd501c54710ee28490606edc7205da4688912
.git/objects/1a/23007ae2cbf9a7fcb79abd5635a54fa8a8db85
.git/objects/1b/5c41f068494791604f750096303390479c019f
.git/objects/1d/acc2e771838dde31e7f288ff66d103752e0e21
.git/objects/1d/fb286ebf4a51d70c5f137b56ac266209877a3d
.git/objects/21/ff5137173465e0a4eede5d955f393a7a427c0a
.git/objects/23/0e419552801069a9bdec3cf23c1cdd197e3bf6
.git/objects/23/811237b5e3255dc1e26469eae1e0e87c2e8221
.git/objects/2b/4a873056ccbb3ad75f6fd3639cd65cbc2ca3a4
.git/objects/2b/947291e84691bbb917cdfe0eba6f35d22cdcbe
.git/objects/2c/0199d039b18989c7a84d1d396fd98e3dc18c29
.git/objects/2e/924fa7af61831e3a34b88a9de4c1126e15efff
.git/objects/31/1496cd5ce2eee83aecdfb2333c2c23c73d7989
.git/objects/34/4a6d4b7140035b87e288cfb6ecf1c8d97f767e
.git/objects/34/4f214ec3833630f61d899b4a44908470fd61d0
.git/objects/37/8e1d31725545b9b25f995a89d58d7f4e34cca8
.git/objects/38/d5c4647e82ea3a7f2b99fb5b12083aada490db
.git/objects/39/e07edc72496ec7e9ec48260afb9442f7603c1e
.git/objects/3b/0cf49783f09b32fa4ff396412d066e6795c80a
.git/objects/3b/b9f08918740a9925ddf71ec7701e40a2c85301
.git/objects/3c/1dee1f0f57c4c3b6bd9ad8a9030fc135dafe99
.git/objects/3d/cabb29de507a188f6ac00852d7b3c8192a1299
.git/objects/40/599393c73f67126c0e419a64cdfcaadf0f94be
.git/objects/42/2a56c9983162a7404a0d27b69d75ad8af25952
.git/objects/42/5cdb92318cefc1d1cfb525fb054cc7bf2175da
.git/objects/43/bcdd9864b3000be2aaf10e03b911e28b5521b6
.git/objects/43/ebc362b87d29f9e787899b39c96f4e73f5edaf
.git/objects/45/ef2b3323d4c99bc485d59ab4fe2e295760c95c
.git/objects/48/80eab8b68d795236109e8e242281e0b47a4551
.git/objects/48/d4562424c9e9a8fa6a2665a5a40456ee1ea1be
.git/objects/4a/3802801caac7e8e276d8fa0586d791b71c9508
.git/objects/4b/46b8901778f224806df1bd0d8d690b9653a74a
.git/objects/4d/aebfbefc46325278889c5cbfcce5fea7805a11
.git/objects/4d/ee9bae436fb6db2ca658bb73a21d563cd10c5a
.git/objects/50/49994f8ed33d9d569d0313c17b902a8bed986e
.git/objects/57/aff8b70e9956147bfd1f86e73c1117d9139abb
.git/objects/58/109c4d5913a6f3ac2db049c25dfe013b659c19
.git/objects/59/6dc7d71663376e3157301e2478794f5f36fdfc
.git/objects/59/73ea9690f16e510ee971eb8d07f80f48ad309d
.git/objects/59/f164119962d1dd5a83bf328e7267266edd84f7
.git/objects/5c/1a944a3aca4b42b27d94aab625e71d541d9a61
.git/objects/5c/f614a5ce0ef230e4200918223864c677c5df83
.git/objects/5d/43f8224c5254d1c734ae91dee3562dada413d8
.git/objects/5d/540f2b93e43dd9a63a9d8f6bd33ca3cba5a698
.git/objects/5e/bcb3c853058ea7422b99e752f9cea88db5c22d
.git/objects/5f/7d635595e3261ad06cfdc8f2b3db3ea21261bd
.git/objects/60/aff232c2e74d6f00453cebb134aea89a9e844e
.git/objects/63/27ebed92ec79eda1cb13f539306355e3615043
.git/objects/64/50b7a53aad87944744aa48cc1dddc85356f00b
.git/objects/64/a948193beea3c1f94b42e907e0c5c8c0bbe63f
.git/objects/65/9b93c4ed7d77977f85d14ff262d3224aeabea6
.git/objects/65/f9b58fbb73bb3846a47038a8353cd3fc15caee
.git/objects/66/5302e5dcc8bcedc8d1991374514511e5a2610d
.git/objects/66/7fcf2257a7a80b28bcbc249685e90965b0c860
.git/objects/68/a2f3220ad704d8cadb953569c0c45ea19e4d6f
.git/objects/6a/cd28acaa2520c183b4381e607aa41ac44048a1
.git/objects/6b/ca823088e2e3a3976bb8ac4857b34a5e4d0e60
.git/objects/6c/7455989c7fc591d0777f7873f73ad98d423ea1
.git/objects/6c/9961c8088c619936f303e7df00c89fea7bc1fd
.git/objects/6d/a2e87ebcdadba5b7aa77f109c53a00307f3bff
.git/objects/74/356d3d2dab5dbcbc73f327b84a0e0a4206ba63
.git/objects/74/4b946d06788e0b34dbd6d09fdc86c8bbeed2e3
.git/objects/76/1b16815aadae6a10f526e5544a76c9ae733b70
.git/objects/7c/c1335e21e5fabcfedf8a202fee93eb3cdbaa6a
.git/objects/80/5f44aa732a3e4772d51ae6ce23179e638608af
.git/objects/82/08cdc4938ee947ce2fb7456e8880835cefa863
.git/objects/82/375862929ab3a854de096274c75478fadf7784
.git/objects/83/348a6f572484135c885a070c2254f4b96712bc
.git/objects/86/dfc68f30680e9896bc5a69f9c0fbe5cb5b6877
.git/objects/87/b1548634cd1b93ac0a00d4cab7a444a837690b
.git/objects/88/9c3b9290fbb4dec26b2e5b2c975813d5dd87a1
.git/objects/89/8baaf33463af19a7cd327700bb8427f66c4a09
.git/objects/8c/fcfadd6541941f162c9439a565bfc0549966c9
.git/objects/8e/5875802e8c9c884574da6cf705d45ab753edd6
.git/objects/8e/5f4c8d2ba17cecc72b397cf7fd3beb00993cb5
.git/objects/94/360a8f1739131942a06bad0b0ed9e1384b9fac
.git/objects/94/3b65d2001ac762944e8ed994f6c50a504e5dc0
.git/objects/97/d9bfd2c48e054216fbea742abb2a28caa3cada
.git/objects/9a/3dc878e021cb75071df838c3a7b46e3e6cb2e9
.git/objects/9b/19ec7d990629f912e53c463077c1e6f59a73d7
.git/objects/9b/8f7b386b9f0cd4380581fb82711c857cf1ae13
.git/objects/9b/ce7e4dfda6f2331d76d406396c6819b73649a9
.git/objects/a1/e9255441e481f115065472db0d364dbc2733e2
.git/objects/a2/acfbe4c86864d2c6957bb8f7d64771c0203900
.git/objects/a2/dd018488d128be3371e5301aa39705b302d5ff
.git/objects/a3/18b5cbba45eac33ed8bf12e62b98345192cd9c
.git/objects/a3/a6944f8bb48722336187a1b82c9a4ddf76ff4c
.git/objects/a8/1ce042219ac505f0748d429cd8dadce4e5c406
.git/objects/a9/507c661ee0a0b8d3e5e301b2a26a6d20831f4f
.git/objects/a9/eb9033e013f1dcf66aff50b0e66f65cd630356
.git/objects/ab/7c32c7f55b2b8967c886594ce2d1513b62936f
.git/objects/ac/5c2be2adb5930227f743463a426a4c6c537817
.git/objects/ae/5a2ec4aa0454a760edef6e10f0ae2f44d6af5c
.git/objects/b1/da018e23492c127711c819ae1436d48bdfd885
.git/objects/b2/98066e37bd0abca7e99a9cab64683462737784
.git/objects/b3/3ca169d79f30dbbc78baa23026e9e66d6dcb36
.git/objects/b3/dc30b7cb4123cc7afab6ae88f44a89a2ef9903
.git/objects/b4/03d9ae5d411a04e1232dde3ecc4a74f9b03da0
.git/objects/be/2a6b20b4a1a503424492d6efcb028ae45cf92e
.git/objects/bf/b3d0a8a10f6a04e74ce69ada0a41d1111eaf57
.git/objects/bf/f4c13e161e2eaaa72e7de881b205cd03d76ad2
.git/objects/bf/faf8e5a8d18c5adbfabc888fc9f2acbcf12036
.git/objects/c1/d4dc1683dc5b6dd3a4321f225bbcedc2175e73
.git/objects/c5/7f29e4e746d36f2f414bbb0b78d75ff41329ba
.git/objects/c5/8e54b976686494a92ba7a9bb1ea2a9e7f74933
.git/objects/cc/1796eb2ab1f44c6d849f1b7c40757e5525f192
.git/objects/ce/0cee66252f09b47d8457a7abb87744b4da361c
.git/objects/d1/7b0ae6667125620e4bca4dd54763036b610d98
.git/objects/d4/6582edd2aaaa1517e2e668df017e6cd4fe46f1
.git/objects/d6/7c6fd8f09bb9468918606f8d205070715b5fa6
.git/objects/d8/54be7961b388fb7374d1eaa774ba83e51826c5
.git/objects/d9/1eb7a0a73492fb23f583a1fdaf65863f5cb336
.git/objects/da/0413840634180c1f276f3eca99f99f024142b5
.git/objects/da/4c885454724e1854ceb6148e953ef045809dcf
.git/objects/da/7297b6620ee9e925ca3fc6e5a860ae38b1c6ba
.git/objects/de/4cc33e44b4554e7c9b13fc5567919cd54831d8
.git/objects/e2/2acd72bd6e9273fd63cb9d6b01d0352812cbfa
.git/objects/e2/f2cd05cd1b90278409e752667c697ab43a71f4
.git/objects/e5/6488f035b4a97f712d76827aacb50f90617181
.git/objects/e6/6c0d67aa3e71902d9697bf32b0685ea18307a4
.git/objects/e6/cd57b3555bcfb8cfc2d5bdff707df23a79183b
.git/objects/e7/db7ac35abd1c7c713b57682749ff984e19583a
.git/objects/ea/7cec14445c1a79bfe2072f67a28abf7523c827
.git/objects/eb/61c7676909465cd409b5ec754f27ecc674b6f7
.git/objects/eb/897c87f87b89df48e3d02fc4bedf4041f2e061
.git/objects/ec/c726ba57b37e5ca47c8cb11f2553c6f36b8c3b
.git/objects/ec/cd7af8ea782607b5e4abba25fb69b209b7695b
.git/objects/ec/d0f644771f64907f2d8872e3f48f9231f11d8c
.git/objects/ed/4e725aae99d6295b5fd7d08e4aef066f5a9e4d
.git/objects/ed/88ccfea6e3d3920ce4bc99c37642420bda46e9
.git/objects/f2/53026ba6da536fbda9ef3eee6856e5233b0954
.git/objects/f5/c7a65fce38e6a1b4a5353d336efbcfafcb7368
.git/objects/f7/44fd675a082ac3d5bd3ad66aa6b97afce5884d
.git/objects/f7/e7af6820516fd16a4bdb0ab0fd68beaf1a64e1
.git/objects/f8/4ea0c7af82a97b0cd8a7d735a546e57e267c6a
.git/objects/fb/395964679d95f989d906be1d1e7eb11a3d2129
.git/objects/pack/pack-0ccaa128f7e7d5bbb0c55f40886a413b1e4e66b0.idx
.git/objects/pack/pack-0ccaa128f7e7d5bbb0c55f40886a413b1e4e66b0.pack
.git/packed-refs
.git/refs/heads/backup/desktop-ros-stt
.git/refs/heads/feature/llm
.git/refs/heads/feature/ui
.git/refs/heads/feature/ui-runtime-integration
.git/refs/heads/fix/llm-runtime-guards
.git/refs/heads/main
.git/refs/remotes/origin/HEAD
.git/refs/remotes/origin/feature/llm
.git/refs/remotes/origin/feature/ui-runtime-integration
.git/refs/remotes/origin/fix/llm-runtime-guards
.git/refs/remotes/origin/main
llm.zip
llm/.pytest_cache/.gitignore
llm/.pytest_cache/CACHEDIR.TAG
llm/.pytest_cache/README.md
llm/.pytest_cache/v/cache/lastfailed
llm/.pytest_cache/v/cache/nodeids
llm/__pycache__/checkout_manager.cpython-310.pyc
llm/__pycache__/checkout_manager.cpython-312.pyc
llm/__pycache__/compound_order_fastpath.cpython-312.pyc
llm/__pycache__/drive_thru_app.cpython-310.pyc
llm/__pycache__/drive_thru_app.cpython-312.pyc
llm/__pycache__/eval_router_gold.cpython-312.pyc
llm/__pycache__/eval_router_smoke.cpython-312.pyc
llm/__pycache__/explicit_order_parser.cpython-312.pyc
llm/__pycache__/finalize_router_gold_v1.cpython-310.pyc
llm/__pycache__/make_router_context_gold_v1.cpython-310.pyc
llm/__pycache__/make_router_correction_gold_v1.cpython-310.pyc
llm/__pycache__/make_router_coverage_gold_v1.cpython-310.pyc
llm/__pycache__/make_router_gold_v1.cpython-310.pyc
llm/__pycache__/make_router_stt_gold_v1.cpython-310.pyc
llm/__pycache__/menu_knowledge.cpython-310.pyc
llm/__pycache__/menu_knowledge.cpython-312.pyc
llm/__pycache__/modifier_selection.cpython-312.pyc
llm/__pycache__/order_runtime_final.cpython-310.pyc
llm/__pycache__/order_runtime_final.cpython-312.pyc
llm/__pycache__/order_schema.cpython-310.pyc
llm/__pycache__/order_schema.cpython-312.pyc
llm/__pycache__/order_update_schema.cpython-312.pyc
llm/__pycache__/price_calorie_info_engine.cpython-312.pyc
llm/__pycache__/qwen_stt_adapter.cpython-310.pyc
llm/__pycache__/qwen_stt_adapter.cpython-312.pyc
llm/__pycache__/ros_stt_udp_bridge.cpython-310.pyc
llm/__pycache__/ros_stt_udp_bridge.cpython-312.pyc
llm/__pycache__/ros_stt_udp_input.cpython-310.pyc
llm/__pycache__/ros_stt_udp_input.cpython-312.pyc
llm/__pycache__/router_client.cpython-310.pyc
llm/__pycache__/router_client.cpython-312.pyc
llm/__pycache__/router_deterministic_resolver.cpython-310.pyc
llm/__pycache__/router_deterministic_resolver.cpython-312.pyc
llm/__pycache__/router_fastpath.cpython-312.pyc
llm/__pycache__/router_gold_canonical.cpython-310.pyc
llm/__pycache__/router_normalizer.cpython-310.pyc
llm/__pycache__/router_normalizer.cpython-312.pyc
llm/__pycache__/router_policy.cpython-310.pyc
llm/__pycache__/router_policy.cpython-312.pyc
llm/__pycache__/router_pre_fastpath.cpython-310.pyc
llm/__pycache__/router_pre_fastpath.cpython-312.pyc
llm/__pycache__/router_prompt.cpython-310.pyc
llm/__pycache__/router_prompt.cpython-312.pyc
llm/__pycache__/router_recommendation_canonicalizer.cpython-312.pyc
llm/__pycache__/router_runtime_bridge.cpython-312.pyc
llm/__pycache__/router_safety_guard.cpython-310.pyc
llm/__pycache__/router_safety_guard.cpython-312.pyc
llm/__pycache__/router_schema.cpython-310.pyc
llm/__pycache__/router_schema.cpython-312.pyc
llm/__pycache__/run_app_regression.cpython-312.pyc
llm/__pycache__/runtime_worker.cpython-312.pyc
llm/__pycache__/soomac_io.launch.cpython-310.pyc
llm/__pycache__/speech_input_worker.cpython-310.pyc
llm/__pycache__/speech_input_worker.cpython-312.pyc
llm/__pycache__/stt_guard.cpython-310.pyc
llm/__pycache__/stt_guard.cpython-312.pyc
llm/__pycache__/stt_session_controller.cpython-310.pyc
llm/__pycache__/stt_session_controller.cpython-312.pyc
llm/__pycache__/test_individual_items.cpython-312.pyc
llm/__pycache__/test_modifier_selection.cpython-312-pytest-9.1.1.pyc
llm/__pycache__/test_router_gold.cpython-310.pyc
llm/__pycache__/test_stt_guard.cpython-310.pyc
llm/__pycache__/tts_text_publisher.cpython-310.pyc
llm/__pycache__/ui_runtime_bridge.cpython-310.pyc
llm/__pycache__/ui_runtime_bridge.cpython-312.pyc
llm/__pycache__/validate_router_gold_all.cpython-310.pyc
llm/checkout_manager.py.bak_20261008_000747
llm/checkout_manager.py.bak_20261008_001708
llm/compound_order_fastpath.py.bak_before_correction_v1
llm/compound_order_fastpath.py.bak_before_set_v2
llm/drive_thru_app.py.STABLE_80PASS
llm/drive_thru_app.py.bak_20261007_031030
llm/drive_thru_app.py.bak_20261007_031457
llm/drive_thru_app.py.bak_20261007_032011
llm/drive_thru_app.py.bak_20261007_211822
llm/drive_thru_app.py.bak_20261007_212500
llm/drive_thru_app.py.bak_20261007_212859
llm/drive_thru_app.py.bak_20261007_213039
llm/drive_thru_app.py.bak_20261007_213343
llm/drive_thru_app.py.bak_20261007_214015
llm/drive_thru_app.py.bak_20261007_214737
llm/drive_thru_app.py.bak_20261007_215107
llm/drive_thru_app.py.bak_20261007_215813
llm/drive_thru_app.py.bak_20261007_220210
llm/drive_thru_app.py.bak_20261007_220420
llm/drive_thru_app.py.bak_20261007_220425
llm/drive_thru_app.py.bak_20261007_220621
llm/drive_thru_app.py.bak_20261007_220855
llm/drive_thru_app.py.bak_20261007_221248
llm/drive_thru_app.py.bak_20261007_221800
llm/drive_thru_app.py.bak_20261007_222618
llm/drive_thru_app.py.bak_20261007_222620
llm/drive_thru_app.py.bak_20261007_222621
llm/drive_thru_app.py.bak_20261007_223045
llm/drive_thru_app.py.bak_20261007_223251
llm/drive_thru_app.py.bak_20261007_223631
llm/drive_thru_app.py.bak_20261007_224549
llm/drive_thru_app.py.bak_20261007_225657
llm/drive_thru_app.py.bak_20261007_230109
llm/drive_thru_app.py.bak_20261007_230737
llm/drive_thru_app.py.bak_20261007_231324
llm/drive_thru_app.py.bak_20261007_234032
llm/drive_thru_app.py.bak_20261007_234036
llm/drive_thru_app.py.bak_20261007_234040
llm/drive_thru_app.py.bak_20261008_000747
llm/drive_thru_app.py.bak_20261008_001626
llm/drive_thru_app.py.bak_20261008_001708
llm/drive_thru_app.py.bak_20261008_002958
llm/drive_thru_app.py.bak_20261008_003003
llm/drive_thru_app.py.bak_20261008_003544
llm/drive_thru_app.py.bak_20261008_202454
llm/drive_thru_app.py.bak_20261008_202751
llm/drive_thru_app.py.bak_20261008_203440
llm/drive_thru_app.py.bak_20261008_203450
llm/drive_thru_app.py.bak_20261008_203451
llm/drive_thru_app.py.bak_20261008_204609
llm/drive_thru_app.py.bak_before_cancel_hook_reconnect
llm/drive_thru_app.py.bak_before_cancel_target_flow
llm/drive_thru_app.py.bak_before_command_normalize_fix
llm/drive_thru_app.py.bak_before_complex_add_runtime_original
llm/drive_thru_app.py.bak_before_criteria
llm/drive_thru_app.py.bak_before_disable_prerouter
llm/drive_thru_app.py.bak_before_explicit_topping_target_guard
llm/drive_thru_app.py.bak_before_fastpath
llm/drive_thru_app.py.bak_before_fastpath_modify_slot_fix
llm/drive_thru_app.py.bak_before_final_correction_fix
llm/drive_thru_app.py.bak_before_fix_knowledge_location
llm/drive_thru_app.py.bak_before_info_engine_v1
llm/drive_thru_app.py.bak_before_menu_board
llm/drive_thru_app.py.bak_before_menu_knowledge
llm/drive_thru_app.py.bak_before_missing_burger_modify_guard
llm/drive_thru_app.py.bak_before_mobile_confirmation_fix
llm/drive_thru_app.py.bak_before_mobile_fastpath_restore
llm/drive_thru_app.py.bak_before_new_burger_rescue
llm/drive_thru_app.py.bak_before_option_capability_priority
llm/drive_thru_app.py.bak_before_pending_closed_world
llm/drive_thru_app.py.bak_before_possibility_capability_fix
llm/drive_thru_app.py.bak_before_prerouter_fast
llm/drive_thru_app.py.bak_before_real_menu_knowledge_hook
llm/drive_thru_app.py.bak_before_recommendation_reply
llm/drive_thru_app.py.bak_before_reference_repair_v2
llm/drive_thru_app.py.bak_before_reference_state_repair
llm/drive_thru_app.py.bak_before_restore_v14_router
llm/drive_thru_app.py.bak_before_router_integration
llm/drive_thru_app.py.bak_before_router_runtime_bridge
llm/drive_thru_app.py.bak_before_topping_capability_guard
llm/drive_thru_app.py.bak_context_safety_final_v1
llm/drive_thru_app.py.bak_empty_topping_prerouter_v1
llm/drive_thru_app.py.bak_fastpath_recovery
llm/drive_thru_app.py.bak_fullset_prefast_20261005_233539
llm/drive_thru_app.py.bak_general_chat_guard_v1
llm/drive_thru_app.py.bak_info_engine_v1_done
llm/drive_thru_app.py.bak_merge_hotfix_v1
llm/drive_thru_app.py.bak_multi_burger_topping_ambiguity_v1
llm/drive_thru_app.py.bak_pre_router_unsupported_option_v1
llm/drive_thru_app.py.bak_recommend_fix2
llm/drive_thru_app.py.bak_simple_speed_v2
llm/drive_thru_app.py.bak_speed_recommend_v1
llm/drive_thru_app.py.bak_speed_v1
llm/drive_thru_app.py.bak_topping_guard_regression_fix_v1
llm/drive_thru_app.py.bak_topping_put_on_v1
llm/drive_thru_app.py.bak_unknown_external_menu_v2
llm/drive_thru_app.py.bak_unknown_menu_guard_v1
llm/drive_thru_app.py.bak_unsupported_dessert_v1
llm/explicit_order_parser.py.bak_before_burger_alias
llm/explicit_order_parser.py.before_rollback
llm/explicit_order_parser.py.disabled
llm/menu_knowledge.py.bak_before_criteria
llm/menu_knowledge.py.bak_before_full_menu
llm/menu_knowledge.py.bak_before_menu_opinion_fix
llm/menu_knowledge.py.bak_before_natural_reply
llm/menu_knowledge.py.bak_before_nutrition_compare_fix
llm/menu_knowledge.py.bak_before_unified_resolver
llm/menu_knowledge.py.bak_explicit_recommendation_target_v1
llm/menu_knowledge.py.bak_other_recommendation_v1
llm/modifier_backup_20261008_215239_417557/drive_thru_app.py
llm/modifier_backup_20261008_215239_417557/new_files.json
llm/modifier_backup_20261008_215239_417557/order_schema.py
llm/modifier_backup_20261008_215239_417557/router_fastpath.py
llm/modifier_backup_20261008_220737_569302/drive_thru_app.py
llm/modifier_backup_20261008_220737_569302/new_files.json
llm/modifier_backup_20261008_220737_569302/test_modifier_selection.py
llm/modifier_backup_20261008_222252_946788/drive_thru_app.py
llm/modifier_backup_20261008_222252_946788/new_files.json
llm/modifier_backup_20261008_222252_946788/test_modifier_selection.py
llm/modifier_backup_20261008_222551_642000/drive_thru_app.py
llm/modifier_backup_20261008_222551_642000/new_files.json
llm/modifier_backup_20261008_223440_508577/drive_thru_app.py
llm/modifier_backup_20261008_223440_508577/new_files.json
llm/modifier_backup_20261008_224122_082599/menu_knowledge.py
llm/modifier_backup_20261008_224122_082599/new_files.json
llm/modifier_backup_20261008_225141_289329/drive_thru_app.py
llm/modifier_backup_20261008_225141_289329/new_files.json
llm/modifier_backup_20261008_232608_655068/drive_thru_app.py
llm/modifier_backup_20261008_232608_655068/modifier_selection.py
llm/modifier_backup_20261008_232608_655068/new_files.json
llm/modifier_backup_20261008_232608_655068/test_modifier_selection.py
llm/order_runtime_final.py.STABLE_80PASS
llm/order_runtime_final.py.bak_20261007_031030
llm/order_runtime_final.py.bak_20261008_000747
llm/order_runtime_final.py.bak_20261008_001708
llm/order_runtime_final.py.bak_before_burger_add_modifier_repair
llm/order_runtime_final.py.bak_before_final_topping_semantic_fix
llm/order_runtime_final.py.bak_before_pending_group_eligibility
llm/order_runtime_final.py.bak_before_pending_group_restore
llm/order_runtime_final.py.bak_before_restore_missing_burger_modifier
llm/order_runtime_final.py.bak_before_single_extra_split
llm/order_runtime_final.py.bak_broken_20261005_152137
llm/order_runtime_final.py.bak_cross_option_20261005_205124
llm/order_runtime_final.py.bak_cross_type_20261005_180417
llm/order_runtime_final.py.bak_merge_hotfix_v1
llm/order_runtime_final.py.bak_multi_modify_topping_20261005_193319
llm/order_runtime_final.py.bak_nonburger_grounding_retry_v1
llm/order_runtime_final.py.bak_nonburger_grounding_v1
llm/order_runtime_final.py.bak_quantity_remove_guard_v1
llm/order_runtime_final.py.bak_split_quantity_remove_v1
llm/order_runtime_final.py.bak_topping_put_on_v1
llm/order_schema.py.bak_20261008_001708
llm/order_schema.py.bak_20261008_002317
llm/order_schema.py.bak_20261008_002319
llm/order_schema.py.bak_20261008_002958
llm/order_schema.py.bak_20261008_202454
llm/order_schema.py.bak_20261008_202751
llm/order_schema.py.bak_20261008_203440
llm/order_schema.py.bak_20261008_203450
llm/order_schema.py.bak_20261008_203451
llm/order_schema.py.bak_20261008_203555
llm/price_calorie_info_engine.py.bak_v1_done
llm/router_client.py.ab_current_20261006_022257
llm/router_client.py.bak_20261007_210600
llm/router_client.py.bak_20261007_210602
llm/router_client.py.bak_20261007_210706
llm/router_client.py.bak_20261007_211119
llm/router_client.py.bak_20261007_211235
llm/router_client.py.bak_adaptive_thinking_20261006_013054
llm/router_client.py.bak_before_criteria_tokens
llm/router_client.py.bak_before_recommendation_semantic_lock
llm/router_client.py.bak_before_speed_fix
llm/router_client.py.bak_telemetry_20261005_221241
llm/router_client.py.bak_thinking_20261005_212734
llm/router_client.py.bak_thinking_false_20261006_012429
llm/router_deterministic_resolver.py.bak_20261008_001708
llm/router_deterministic_resolver.py.bak_before_mobile_pickup
llm/router_deterministic_resolver.py.bak_before_real_v2
llm/router_deterministic_resolver.py.bak_before_single_set_fix
llm/router_deterministic_resolver.py.bak_before_type_override_fix
llm/router_deterministic_resolver.py.bak_blind_v1_final
llm/router_deterministic_resolver.py.bak_c053_v2_force
llm/router_deterministic_resolver.py.bak_cancel_fix
llm/router_deterministic_resolver.py.bak_fix_conditional
llm/router_deterministic_resolver.py.bak_gold14_context
llm/router_deterministic_resolver.py.bak_gold14_remaining7
llm/router_deterministic_resolver.py.bak_gold718_c053
llm/router_deterministic_resolver.py.bak_gold718_chatboundary3
llm/router_deterministic_resolver.py.bak_gold718_deterministic3
llm/router_deterministic_resolver.py.bak_gold718_last2
llm/router_deterministic_resolver.py.bak_gold718_policy2_final
llm/router_deterministic_resolver.py.bak_gold718_policy4
llm/router_deterministic_resolver.py.bak_off_safety_v1
llm/router_fastpath.py.bak_20261008_001708
llm/router_fastpath.py.bak_before_complex_burger_add_guard
llm/router_fastpath.py.bak_before_correction_v1
llm/router_fastpath.py.bak_before_multi_fastpath
llm/router_fastpath.py.bak_before_segment_parser
llm/router_fastpath.py.bak_compound_connect_v2
llm/router_fastpath.py.bak_compound_v1
llm/router_fastpath.py.bak_context_safety_final_v1
llm/router_fastpath.py.bak_contextual_topping_add_v1
llm/router_fastpath.py.bak_contextual_topping_add_v2
llm/router_fastpath.py.bak_merge_hotfix_v1
llm/router_fastpath.py.bak_pending_size_speed_v1
llm/router_fastpath.py.bak_remove_fastpath_v1
llm/router_fastpath.py.bak_topping_put_on_v1
llm/router_fastpath.py.before_rollback
llm/router_policy8_single.json~
llm/router_pre_fastpath.py.bak_before_all_explicit_parser
llm/router_pre_fastpath.py.bak_before_compound_v2_cleanup
llm/router_pre_fastpath.py.bak_before_correction_v1
llm/router_pre_fastpath.py.bak_before_multi_explicit_pre_fastpath
llm/router_pre_fastpath.py.bak_before_recommendation_fast
llm/router_pre_fastpath.py.bak_before_segment_parser
llm/router_pre_fastpath.py.bak_compound_connect_v2
llm/router_pre_fastpath.py.bak_compound_guard_v1
llm/router_pre_fastpath.py.bak_compound_v1
llm/router_pre_fastpath.py.bak_drink_speed_v1
llm/router_pre_fastpath.py.bak_fullset_20261005_233322
llm/router_pre_fastpath.py.bak_quantity_speed_v1
llm/router_pre_fastpath.py.bak_recommend_fix2
llm/router_pre_fastpath.py.bak_simple_speed_v2
llm/router_pre_fastpath.py.bak_speed_v1
llm/router_pre_fastpath.py.before_rollback
llm/router_prompt.py.ab_current_20261006_021417
llm/router_prompt.py.bak_20261008_001708
llm/router_prompt.py.bak_before_criteria
llm/router_prompt.py.bak_before_menu_semantics
llm/router_prompt.py.bak_before_recommendation_priority
llm/router_prompt.py.bak_cancel_fix
llm/router_prompt.py.bak_history_scope_20261005_214617
llm/router_prompt.py.bak_modify_min_20261005_233828
llm/router_prompt.py.failed_modify_min_20261005_235158
llm/router_safety_guard.py.bak_cancel_fix
llm/router_schema.py.bak_20261008_001708
llm/router_schema.py.bak_before_criteria
llm/run_app_regression.py.bak_before_strict_item_match
llm/runtime_worker.py.bak_before_fastpath
modifier_patch_repo/.git/FETCH_HEAD
modifier_patch_repo/.git/HEAD
modifier_patch_repo/.git/ORIG_HEAD
modifier_patch_repo/.git/config
modifier_patch_repo/.git/description
modifier_patch_repo/.git/hooks/applypatch-msg.sample
modifier_patch_repo/.git/hooks/commit-msg.sample
modifier_patch_repo/.git/hooks/fsmonitor-watchman.sample
modifier_patch_repo/.git/hooks/post-update.sample
modifier_patch_repo/.git/hooks/pre-applypatch.sample
modifier_patch_repo/.git/hooks/pre-commit.sample
modifier_patch_repo/.git/hooks/pre-merge-commit.sample
modifier_patch_repo/.git/hooks/pre-push.sample
modifier_patch_repo/.git/hooks/pre-rebase.sample
modifier_patch_repo/.git/hooks/pre-receive.sample
modifier_patch_repo/.git/hooks/prepare-commit-msg.sample
modifier_patch_repo/.git/hooks/push-to-checkout.sample
modifier_patch_repo/.git/hooks/update.sample
modifier_patch_repo/.git/index
modifier_patch_repo/.git/info/exclude
modifier_patch_repo/.git/logs/HEAD
modifier_patch_repo/.git/logs/refs/heads/main
modifier_patch_repo/.git/logs/refs/remotes/origin/HEAD
modifier_patch_repo/.git/logs/refs/remotes/origin/main
modifier_patch_repo/.git/objects/02/65ef62d3eb604bcd1e199eb6f60ba0c36ff546
modifier_patch_repo/.git/objects/06/3ad895f7d22aad23da34d74898570311ea0ccc
modifier_patch_repo/.git/objects/07/aa5505bf948dfc26a5fd3cd5820dbf4f0b9bd8
modifier_patch_repo/.git/objects/09/e5d8e3a7f7338a95e897ca6dc6dade318ffd5d
modifier_patch_repo/.git/objects/0a/070f4576612fc3641d4e97c6044f71513734ad
modifier_patch_repo/.git/objects/0e/1db18dcd297bfbe6ef9dfd808dfa9508578ac9
modifier_patch_repo/.git/objects/10/f7fabacba89719c5bfbbfbd2e4a25404a668ad
modifier_patch_repo/.git/objects/13/173999aec1ff5dc030370208a399440d9b4316
modifier_patch_repo/.git/objects/14/039c013317e1f84bb106bb3b0db5b429d84f8a
modifier_patch_repo/.git/objects/15/6260b430fc9da785b6f42f4ff498457de938e7
modifier_patch_repo/.git/objects/15/75a39ab73daee89d988fa740488e4213fecba9
modifier_patch_repo/.git/objects/20/db592f2cfc6b5aea82dd47023954f4ea3b5e89
modifier_patch_repo/.git/objects/25/a522eccf1a117a61d8c9cf903b59e71aa4d45c
modifier_patch_repo/.git/objects/27/3ec36b8b1e3c5089efd722f9eeb3936d754dc5
modifier_patch_repo/.git/objects/2b/b7a6ee5b805022a5ff3b60e3ab8d3df3140032
modifier_patch_repo/.git/objects/2f/cac95d0ada1d454efcf3f069455b20a3124130
modifier_patch_repo/.git/objects/30/7e0314f9c95a589f20cd21b8f43f65cedd720d
modifier_patch_repo/.git/objects/30/c80e8896ba549d49528c2f97129375cc818806
modifier_patch_repo/.git/objects/31/d1a9e0d8616697bcaa0962fca60dae2996657b
modifier_patch_repo/.git/objects/33/0b50c8985464d2eec02c5825e787bf259f40cc
modifier_patch_repo/.git/objects/35/732c49090757761f1d32ad830ec117c554de41
modifier_patch_repo/.git/objects/3c/289adc4be3c09a043ee0736575c5c8180c6fd4
modifier_patch_repo/.git/objects/44/2009f0bc25d249a9b724a1a487b26c29c44f79
modifier_patch_repo/.git/objects/4b/307816835848a9a7fbd7df2e1daa766fffd9ba
modifier_patch_repo/.git/objects/4f/8d6a81c3cb76827740059b1d0f3956937af7a5
modifier_patch_repo/.git/objects/54/77991b271f627bc8281c67f856d29edc543d3b
modifier_patch_repo/.git/objects/5a/e48814c3b06a594c6ea155d69c2f782429baeb
modifier_patch_repo/.git/objects/64/d278308f66d275b24e1d4996e032f5fd47b7ab
modifier_patch_repo/.git/objects/65/5e1117b5aac2325dd8173e5edf74ab35e4cda2
modifier_patch_repo/.git/objects/6a/6201ae14b9d238dbe13d5d827a7c9f625ceae2
modifier_patch_repo/.git/objects/6f/033cc85e33ca4d4b481dc15eb17da2d19af63a
modifier_patch_repo/.git/objects/6f/d0239533d0569cd0d8f88a3e6e56340262a440
modifier_patch_repo/.git/objects/82/0d8c32f6f9bec06f18ae39d290be5d18764686
modifier_patch_repo/.git/objects/82/f489c1236212c912121c7085b6653b52baffe9
modifier_patch_repo/.git/objects/83/f8c1823915bda398b56d6c0bf05f066891cdec
modifier_patch_repo/.git/objects/84/5f8c4334f1d5911b29e7baf18c1e7e175798b4
modifier_patch_repo/.git/objects/8a/2bd5a29b1175194dd1f4ba10eeebf9080ba835
modifier_patch_repo/.git/objects/8a/b926b478b25be258c07d3b1d8c13f026d36d49
modifier_patch_repo/.git/objects/8b/a0dcfb594e5f10715d2dfd6c50c6b825be17d5
modifier_patch_repo/.git/objects/8d/bc31970325f23dd94ef0e841365e8756818fec
modifier_patch_repo/.git/objects/90/4b1629c6ccaab3115624b49db958598e99d70d
modifier_patch_repo/.git/objects/93/6f679d2e14050169306b5092cdec0e4b369443
modifier_patch_repo/.git/objects/94/9e4c4fb2330662b24ff4bcfd65856aeaa9075a
modifier_patch_repo/.git/objects/95/2a535a2378cdfa856b37d87809c62bf7c0bc00
modifier_patch_repo/.git/objects/96/14a6885dcaf8825b733b347917493ebd3a915a
modifier_patch_repo/.git/objects/98/668c3767dddffc6f994686bb623fdcbdfb9f96
modifier_patch_repo/.git/objects/9b/20dc59858724c22245d6cd29aa91aa2e393808
modifier_patch_repo/.git/objects/9e/9701706c3a2c525096051786f3026aa50a659e
modifier_patch_repo/.git/objects/a2/c3bdfb241bc17064cdbd3671b78b8cffc088e3
modifier_patch_repo/.git/objects/a2/ed2b1ab4ee0e6ce806f9fa30ee96c877018e56
modifier_patch_repo/.git/objects/a3/b2c90354e09ece8f91785be10c95ecfcb1906c
modifier_patch_repo/.git/objects/ab/c2354226e34c23c5b6e78251d6807fb09fa1f9
modifier_patch_repo/.git/objects/af/d2ec9222250fa95a22f46d9ef54f851c48708c
modifier_patch_repo/.git/objects/b2/52e20fee91ef3f86cbda83c72dee92c0caa261
modifier_patch_repo/.git/objects/b7/54e0a06bb565d83f6b19f7cf6fcaae80c2fbb9
modifier_patch_repo/.git/objects/bb/381181f1021cf27adc7902aba56f8b4d2e51ba
modifier_patch_repo/.git/objects/be/03327ed1c7e133763787dbad95cee254273159
modifier_patch_repo/.git/objects/c8/fe21ecc95c45394eca7569def52702cd09d152
modifier_patch_repo/.git/objects/d0/d7893e1b7c2ad046253e569eadf12a64e4b3fa
modifier_patch_repo/.git/objects/d3/67a9fb76a5591c5d704630dccd143c9d2b69b5
modifier_patch_repo/.git/objects/d3/daeadcf36abebd1dacc6a325fe955110f60328
modifier_patch_repo/.git/objects/d6/051233088698be30bd95a8b18e549914c7e729
modifier_patch_repo/.git/objects/df/2396b35c930dd160f52e056c8c240647d52f27
modifier_patch_repo/.git/objects/df/ea3a377ab58eca74c88d8f7e15359d41e3dcb9
modifier_patch_repo/.git/objects/e3/20f25084ae9c59145169a4eaab213807512e01
modifier_patch_repo/.git/objects/e7/2113e8281ee7944a3d2a44636d1323df87c916
modifier_patch_repo/.git/objects/e8/2e46693c7b7f10ba6dd05e94b6b06ac3cb4810
modifier_patch_repo/.git/objects/eb/86caba973c6fd70834bee8e070e7592b4a3fb5
modifier_patch_repo/.git/objects/f1/eb279bce82bc0eef4a884459f5a0ec4402762a
modifier_patch_repo/.git/objects/f7/6465694d663e06add0d25fcad96575492d80b5
modifier_patch_repo/.git/objects/f8/60496b74029e762ecb1fdbefb483de8e21e151
modifier_patch_repo/.git/objects/fa/49f9f9fd9698216c3b4e88d9438d9a9de93296
modifier_patch_repo/.git/objects/fd/0813809d94d7f956c9c8a92cc92159e358c6e8
modifier_patch_repo/.git/objects/fd/61ba592f3563a4848c7dd890995430bccea765
modifier_patch_repo/.git/objects/pack/pack-3c96c19e37959c738a4bfb77238553235978e2f6.idx
modifier_patch_repo/.git/objects/pack/pack-3c96c19e37959c738a4bfb77238553235978e2f6.pack
modifier_patch_repo/.git/packed-refs
modifier_patch_repo/.git/refs/heads/main
modifier_patch_repo/.git/refs/remotes/origin/HEAD
modifier_patch_repo/.git/refs/remotes/origin/main
modifier_patch_repo/modifier_patch/README_KO.md
modifier_patch_repo/modifier_patch/apply_patch.py
modifier_patch_repo/modifier_patch/files/drive_thru_app.py
modifier_patch_repo/modifier_patch/files/menu_knowledge.py
modifier_patch_repo/modifier_patch/files/modifier_selection.py
modifier_patch_repo/modifier_patch/files/order_schema.py
modifier_patch_repo/modifier_patch/files/router_fastpath.py
modifier_patch_repo/modifier_patch/files/test_modifier_selection.py
modifier_patch_repo/modifier_patch/manifest.json
modifier_patch_repo/tools/README_KO.md
modifier_patch_repo/tools/archive_backups.py
stt/__pycache__/qwen_live_ver_2.cpython-310.pyc
stt/__pycache__/qwen_live_ver_2.cpython-312.pyc
```

### 사용자 추가 정리 단계 제외 (99개)

```text
llm/eval_v14_blind_results.jsonl
llm/regression_cases/app_regression_final_edge_v1.json.bak_before_expect_fix
llm/regression_cases/app_regression_final_edge_v1.json.bak_merge_hotfix_v1
llm/regression_cases/app_regression_v1.json.bak_T081_20261005_194217
llm/regression_cases/app_regression_v1.json.bak_before_T061_T080
llm/regression_cases/app_regression_v1.json.bak_before_cancel_quantity_reference
llm/regression_cases/app_regression_v1.json.bak_before_set_pending_suite
llm/regression_results/app_regression_20261004_231024.json
llm/regression_results/app_regression_20261004_232455.json
llm/regression_results/app_regression_20261004_233853.json
llm/regression_results/app_regression_20261004_235714.json
llm/regression_results/app_regression_20261005_002600.json
llm/regression_results/app_regression_20261005_005228.json
llm/regression_results/app_regression_20261005_015426.json
llm/regression_results/app_regression_20261005_021918.json
llm/regression_results/app_regression_20261005_033400.json
llm/regression_results/app_regression_20261005_143748.json
llm/regression_results/app_regression_20261005_152137.json
llm/regression_results/app_regression_20261005_161703.json
llm/regression_results/app_regression_20261005_194647.json
llm/regression_results/app_regression_20261005_194802.json
llm/regression_results/app_regression_20261005_205158.json
llm/regression_results/app_regression_20261005_220355.json
llm/regression_results/app_regression_20261005_221249.json
llm/regression_results/app_regression_20261005_221604.json
llm/regression_results/app_regression_20261005_225031.json
llm/regression_results/app_regression_20261005_231435.json
llm/regression_results/app_regression_20261005_233547.json
llm/regression_results/app_regression_20261005_233838.json
llm/regression_results/app_regression_20261006_025828.json
llm/regression_results/app_regression_20261006_032427.json
llm/regression_results/app_regression_20261006_032642.json
llm/regression_results/app_regression_20261006_040330.json
llm/regression_results/app_regression_20261006_040807.json
llm/regression_results/app_regression_20261006_041207.json
llm/regression_results/app_regression_20261006_041223.json
llm/regression_results/app_regression_20261006_041527.json
llm/regression_results/app_regression_20261006_041956.json
llm/regression_results/app_regression_20261006_042153.json
llm/regression_results/app_regression_20261006_043345.json
llm/regression_results/app_regression_20261006_043443.json
llm/regression_results/app_regression_20261006_153353.json
llm/regression_results/app_regression_20261006_153441.json
llm/regression_results/app_regression_20261006_153715.json
llm/regression_results/app_regression_20261006_205338.json
llm/regression_results/app_regression_20261006_210529.json
llm/regression_results/app_regression_20261006_211022.json
llm/regression_results/app_regression_20261006_211306.json
llm/regression_results/app_regression_20261006_211505.json
llm/regression_results/app_regression_20261006_212635.json
llm/regression_results/app_regression_20261006_212750.json
llm/regression_results/app_regression_20261006_212946.json
llm/regression_results/app_regression_20261006_214649.json
llm/regression_results/app_regression_20261006_215508.json
llm/regression_results/app_regression_20261006_215802.json
llm/regression_results/app_regression_20261006_234658.json
llm/regression_results/app_regression_20261007_000249.json
llm/regression_results/app_regression_20261007_000756.json
llm/regression_results/app_regression_20261007_002215.json
llm/regression_results/app_regression_20261007_003825.json
llm/router_blind_v1_after_patch.json
llm/router_blind_v1_first_result.json
llm/router_context6_after_patch.json
llm/router_gold_adaptive_w1.json
llm/router_gold_after_context_patch_718.json
llm/router_gold_after_resolver_718.json
llm/router_gold_final_718.json
llm/router_gold_final_718_v2.json
llm/router_gold_final_718_v3.json
llm/router_gold_final_718_v4.json
llm/router_gold_final_718_v5.json
llm/router_gold_final_718_w1_afterrollback.json
llm/router_gold_final_after_policy4_718.json
llm/router_gold_policy_recheck_results.json
llm/router_gold_regressions_39_current.json
llm/router_gold_regressions_39_off_safety_v1.json
llm/router_gold_regressions_39_off_safety_v2_final.json
llm/router_gold_regressions_39_old_client.json
llm/router_gold_regressions_39_prompt_before_criteria.json
llm/router_gold_remaining_13_off_safety_v2.json
llm/router_gold_remaining_13_off_safety_v2_real.json
llm/router_gold_results.json
llm/router_gold_results_718_parallel.json
llm/router_gold_stable_718_w1.json
llm/router_gold_thinking_probe_12_on.json
llm/router_last2_after_patch.json
llm/router_policy3_after_patch.json
llm/router_policy4_after_patch.json
llm/router_policy8_after_deterministic3.json
llm/router_policy_after_guard.json
llm/router_policy_after_resolver.json
llm/router_policy_fail_14_context.json
llm/router_policy_fail_46_after_v2.json
llm/router_policy_fail_46_final.json
llm/router_policy_fail_46_final2.json
llm/router_remaining9_after_patch.json
llm/router_remaining9_before_patch.json
llm/router_smoke_after_guard.json
llm/router_smoke_results.json
```
