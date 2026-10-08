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
