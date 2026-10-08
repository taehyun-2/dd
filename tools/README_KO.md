# 프로젝트 파일 정리

## 전체 프로젝트 정리

```bash
cd ~/soomac_3.0-IRC_ASZ/modifier_patch_repo
git pull origin main
python3 tools/organize_project.py
python3 tools/organize_project.py --apply
```

기본 대상은 `~/soomac_3.0-IRC_ASZ` 전체입니다. 첫 명령은 종류별 개수만
표시하며 `--list`를 붙이면 모든 경로를 볼 수 있습니다. `--apply`는 백업,
`modifier_backup_*`, `__pycache__`, `.pytest_cache`, 이전 버전 사본
(`.STABLE_80PASS`, `.disabled`, `.before_rollback`, `.ab_current_*`,
`.failed_modify_min_*`), 프로젝트 최상위 `llm.zip`을 프로젝트 밖의
`~/soomac_3.0-IRC_ASZ_archive/날짜_시간_고유번호/`로 옮깁니다.

현재 실행 코드, STT 코드와 설정, UI, 주문 기록, 테스트·학습 데이터,
평가 결과, 모델, 가상환경, `.git`은 유지합니다. 패치 저장소도 계속 업데이트할
수 있도록 유지합니다. 명시한 패턴에 맞는 사본만 옮기며, 단순히 오래된 파일이나
다른 버전의 실행 파일이라는 이유로 분류하지 않습니다. 예를 들어
`qwen_live_ver_2.py`와 `qwen_live_ver_3.py`는 모두 유지합니다.

파일 내용과 기존 폴더 구조는 보관 폴더의 `files/`에 유지하며, 경로 목록은
`manifest.json`에 기록합니다. 정리 중에는 패치 적용·테스트·파일 편집을 피하세요.
도구 자체는 앱·vLLM을 종료하지 않습니다. 재생성되는 캐시는 이후 다시 생길 수 있습니다.

복원은 `python3 tools/organize_project.py --restore 보관폴더`로 실행합니다.
같은 이름의 파일이 현재 위치에 있으면 덮어쓰지 않고 중단합니다.
프로젝트 위치가 바뀌었으면 `--target 새_프로젝트_경로`를 함께 지정하세요.

## llm 백업만 정리

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
