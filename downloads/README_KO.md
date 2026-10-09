# 최신: 취소 후 메뉴 항목 연속 번호 (2026-10-09)

- [실사용용 ZIP](https://github.com/taehyun-2/dd/raw/refs/heads/main/downloads/soomac_3.0-IRC_ASZ_runtime_renumbered.zip)
- [GitHub용 ZIP](https://github.com/taehyun-2/dd/raw/refs/heads/main/downloads/soomac_3.0-IRC_ASZ_github_renumbered.zip)
- [번호 정리 적용 안내](LINE_NUMBERING_KO.md)

`1,2,3,4,5`에서 3번 취소 후 `1,2,3,4`로 정리됩니다. 다음 명령도 새 번호 기준입니다.
기존 PUB 기능을 포함합니다. 고객 접수 누적번호와 맥오더 예약번호는 바꾸지 않습니다.
직전 PUB 버전 대비 실행 코드 수정은 `llm/order_runtime_final.py` 한 파일입니다.
실사용용 테스트 322개, GitHub용 코드 외부 테스트 302개 및 기존 오프라인 스크립트 10개 통과.

```bash
cd ~/soomac_3.0-IRC_ASZ/modifier_patch_repo
git pull origin main
(cd downloads && sha256sum -c soomac_3.0-IRC_ASZ_runtime_renumbered.zip.sha256 && sha256sum -c soomac_3.0-IRC_ASZ_github_renumbered.zip.sha256)
mkdir -p ~/soomac_renumbered
unzip -n downloads/soomac_3.0-IRC_ASZ_runtime_renumbered.zip -d ~/soomac_renumbered
unzip -n downloads/soomac_3.0-IRC_ASZ_github_renumbered.zip -d ~/soomac_renumbered
```

기존 파일과 `runtime_data/`를 백업·유지하고 적용하세요. 앱을 다음 실행할 때 반영됩니다.

---

# 이전: 주문 완료 ROS PUB 추가 (2026-10-09)

- [실사용용 ZIP](https://github.com/taehyun-2/dd/raw/refs/heads/main/downloads/soomac_3.0-IRC_ASZ_runtime_order_pub.zip)
- [팀 GitHub 업로드용 ZIP](https://github.com/taehyun-2/dd/raw/refs/heads/main/downloads/soomac_3.0-IRC_ASZ_github_order_pub.zip)
- [연결·실행 안내](ROS_ORDER_PUB_KO.md)

주문 확정 시 메뉴/수량 요약과 총액을 `/order` (`std_msgs/msg/String`)로 발행합니다.
실사용용·GitHub용 각각 293개 오프라인 테스트 통과. 실제 ROS DDS/로봇은 현장에서 확인해야 합니다.
사용자가 마지막으로 올린 ZIP 두 개에 동일한 실행 코드를 반영했고 GitHub용에는 테스트를 넣지 않았습니다.
팀 저장소에는 직접 변경을 올리지 않았습니다. 메인 노드 맥오더 발화 수정 1줄 패치를 ZIP에 함께 넣었습니다.

기존 복제 저장소에서 받기:

```bash
cd ~/soomac_3.0-IRC_ASZ/modifier_patch_repo
git pull origin main
(cd downloads && sha256sum -c soomac_3.0-IRC_ASZ_runtime_order_pub.zip.sha256 && sha256sum -c soomac_3.0-IRC_ASZ_github_order_pub.zip.sha256)
mkdir -p ~/soomac_order_pub
unzip -n downloads/soomac_3.0-IRC_ASZ_runtime_order_pub.zip -d ~/soomac_order_pub
unzip -n downloads/soomac_3.0-IRC_ASZ_github_order_pub.zip -d ~/soomac_order_pub
```

기존 폴더는 보존됩니다. 실제 사용 경로는 `~/soomac_order_pub/soomac_3.0-IRC_ASZ_runtime`입니다.
앱과 ROS IO 런치는 반드시 이 새 사본을 함께 사용해야 합니다.
기존 주문 순번을 이어가려면 이전 `llm/runtime_data/handoffs/`도 보관·이전하세요.
IO 런치를 다시 실행해야 새 publisher가 기동됩니다. vLLM은 재시작할 필요 없습니다.

---

# 이전: 사용자 수정본 검토 패키지 (2026-10-08)

사용자가 직접 정리하고 런치 경로를 수정한 최신 두 ZIP을 기준으로 보완했습니다.
아래 **reviewed** 파일이 최신입니다. 기존 `clean.zip`은 그 이전 정리본으로 남겨두었습니다.

| 파일 | 용도 |
|---|---|
| [실제 사용용 ZIP](https://github.com/taehyun-2/dd/raw/refs/heads/main/downloads/soomac_3.0-IRC_ASZ_runtime_reviewed.zip) | Ubuntu 사용용. 사용자가 남긴 테스트·학습 데이터 포함, CLOVA 생성 파일 보완. 133개 파일. |
| [GitHub용 ZIP](https://github.com/taehyun-2/dd/raw/refs/heads/main/downloads/soomac_3.0-IRC_ASZ_github_reviewed.zip) | 소스 공유용. 실행 코드 중심, CLOVA 사용 전 생성 스크립트 실행 필요. 56개 파일. |

[상세 검토 결과](PACKAGE_REVIEW_KO.md)를 확인하세요. 각 ZIP 안에도 검토 결과와 파일별 SHA-256 비교표가 들어 있습니다.
원본 코드·런치·데이터는 모두 보존했고 문서와 누락된 CLOVA 준비 과정만 보완했습니다.
주문 처리 테스트는 양쪽 각각 270개 통과. 기존 별도 회귀 스크립트의 잡음 입력(`ㅋㅋㅋㅋ`) 차단 실패 1건은 남아 있습니다.
실제 ROS/GPU/마이크 구동은 별도 확인이 필요합니다.

## Ubuntu 터미널에서 받기

기존에 복제한 저장소에서:

```bash
cd ~/soomac_3.0-IRC_ASZ/modifier_patch_repo
git pull origin main
(cd downloads && sha256sum -c soomac_3.0-IRC_ASZ_runtime_reviewed.zip.sha256 && sha256sum -c soomac_3.0-IRC_ASZ_github_reviewed.zip.sha256)
mkdir -p ~/soomac_reviewed
unzip -n downloads/soomac_3.0-IRC_ASZ_runtime_reviewed.zip -d ~/soomac_reviewed
```

압축을 푼 실제 사용용 경로는 `~/soomac_reviewed/soomac_3.0-IRC_ASZ_runtime`입니다.
이 명령은 기존 프로젝트를 교체하거나 삭제하지 않습니다. 먼저 별도 폴더에서 확인하고 기존 프로젝트는 백업하세요.
기존 `~/drive_thru_venv`, 모델 폴더, 개인 `stt/env.sh`는 유지해야 합니다.

기존 저장소 경로가 다르면 위 `cd` 경로만 실제 복제 경로로 바꾸세요.
GitHub ZIP은 소스 파일 묶음이므로, 저장소 전체의 Code → Download ZIP과 구분하세요.

---

## 아래는 이전 정리본 안내

# 정리된 전체 프로젝트 다운로드

[정리본 ZIP 다운로드](https://github.com/taehyun-2/dd/raw/refs/heads/main/downloads/soomac_3.0-IRC_ASZ_clean.zip)

업로드된 전체 프로젝트를 기준으로 정리한 소스 226개 파일입니다.
`llm/`, `stt/`, UI, 테스트·학습 데이터, 평가 자료, 실행 스크립트가 포함됩니다.
백업·캐시·이전 코드 사본·기존 llm.zip은 분리했고, 배포본에서는 Git 내부 이력과
별도로 복제한 modifier_patch_repo도 제외했습니다. 원래 업로드 ZIP과 별도 보관본은
보존되어 있습니다. 배포본 ZIP에는 정리 도구의 보관본이 포함되지 않습니다.

앱 수정 파일 6개의 SHA-256이 현재 modifier_patch 패키지와 일치합니다.
정리된 소스에서 테스트 270개가 통과했습니다. 실제 ROS·vLLM 구동은 검증하지 않았습니다.
가상환경, 모델 가중치와 개인 인증 정보는 외부 설정을 사용합니다.

## 받기

GitHub ZIP 파일 페이지에서 **Download raw file** 버튼으로 받으세요.
이 저장소의 Code → Download ZIP은 패치와 도구까지 포함한 저장소 전체 다운로드입니다.

Ubuntu에서 기존 복제 저장소로도 받을 수 있습니다:

```bash
cd ~/soomac_3.0-IRC_ASZ/modifier_patch_repo
git pull origin main
ls downloads/soomac_3.0-IRC_ASZ_clean.zip
```

압축은 별도 폴더에 먼저 풀어 확인하세요. 기존 폴더 위에 덮어 풀면 오래된 파일은
자동으로 사라지지 않습니다. 기존 Ubuntu 폴더를 정리하려면 저장소의
`python3 tools/organize_project.py --apply`를 사용하세요.

SHA-256: `995a7539ec544c54e8c056e0c1f809b1df1685158e49e27e15adae84a92aa957`
