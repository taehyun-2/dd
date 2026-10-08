# 프로젝트 파일 정리

현재 GitHub 저장소는 전체 앱이 아니라 수정 파일을 배포하는 패치 저장소입니다.
Ubuntu의 `llm`을 이 저장소로 통째로 치환하지 마세요.

## 먼저 백업 사본만 보관

```bash
cd ~/soomac_3.0-IRC_ASZ/modifier_patch_repo
git pull origin main
python3 tools/archive_backups.py --target ~/soomac_3.0-IRC_ASZ/llm
python3 tools/archive_backups.py --target ~/soomac_3.0-IRC_ASZ/llm --apply
```

첫 명령은 대상 목록만 출력합니다. `--apply`를 붙이면 `llm` 바로 아래의
`*.bak`, `*.bak_*`, `*.backup`, 편집기 백업 `*~` 파일과 `modifier_backup_*`
폴더를 `~/soomac_3.0-IRC_ASZ/llm_backups/날짜_시간_고유번호/`로 옮깁니다.
원래 파일명과 프로젝트 경로는 보관 폴더의 `manifest.json`에 기록합니다.
심볼릭 링크와 하위 폴더 내부의 파일은 검색하지 않습니다.

기존 보관 폴더를 재사용하지 않으며 파일을 삭제하지 않습니다. 이동 실패 시
이미 옮긴 항목을 원래 위치로 되돌립니다. 백업 파일을 쓰는 패치 적용 작업이
완료된 뒤 실행하세요. 보관 폴더가 기존 전체 백업 안에 없을 수도 있으므로
프로젝트 백업 시 `llm_backups`도 함께 보관하세요.

복원 예시 (실제 출력된 보관 폴더 경로 사용):

```bash
python3 tools/archive_backups.py --restore ~/soomac_3.0-IRC_ASZ/llm_backups/날짜_시간_고유번호
```

원래 위치에 같은 이름이 있으면 덮어쓰지 않고 중단합니다.

## 현재 위치에 유지할 항목

- 실행 코드 `*.py`, `start_app.sh`, `start_vllm.sh`, ROS launch 파일
- UI 파일 `ui/`, 주문 데이터 `runtime_data/`
- 학습·평가 데이터 `dataset_v14/`, `router_data/`, `regression_cases/`
- 테스트·학습·평가 스크립트, JSON 결과 파일, `regression_results/`
- 의존성 목록, README, 가상환경, 모델 파일

테스트·학습 코드는 상호 import와 상대 경로를 사용하므로 이름만 보고 폴더를
옮기면 실행이 깨질 수 있습니다. 결과 JSON도 테스트 입력으로 재사용될 수 있어
첫 정리에서는 유지합니다. `.disabled`, `.STABLE_80PASS`, `.before_rollback`
같은 별도 복구본도 유지합니다. 캐시는 이번 도구에서 변경하지 않습니다.

정리 도구는 앱·vLLM 프로세스를 종료하거나 Git 명령을 실행하지 않습니다.
