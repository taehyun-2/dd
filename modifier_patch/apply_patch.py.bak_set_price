#!/usr/bin/env python3
"""Apply only to the exact uploaded source version; back up before writing."""
import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description="원본 해시 검증 → 백업 → modifier 패치 적용 (Git/프로세스 조작 없음)")
    parser.add_argument("--target", type=Path, default=Path.home() / "soomac_3.0-IRC_ASZ" / "llm")
    parser.add_argument("--check", action="store_true", help="파일을 바꾸지 않고 적용 가능 여부만 확인")
    args = parser.parse_args()
    target = args.target.expanduser().resolve()
    if not target.is_dir():
        raise SystemExit(f"프로젝트 폴더가 없습니다: {target}")
    source = Path(__file__).resolve().parent
    manifest = json.loads((source / "manifest.json").read_text())
    changes = []
    for name, hashes in manifest.items():
        if Path(name).name != name:
            raise SystemExit("잘못된 파일 이름입니다.")
        path = target / name
        if path.is_symlink():
            raise SystemExit(f"심볼릭 링크는 변경하지 않습니다: {path}")
        data = (source / "files" / name).read_bytes()
        if sha(data) != hashes["patched_sha256"]:
            raise SystemExit(f"패치 파일 무결성 검사 실패: {name}")
        compile(data, name, "exec")
        current = sha(path.read_bytes()) if path.exists() else None
        if current == hashes["patched_sha256"]:
            continue
        accepted = set(hashes.get("accepted_sha256", []))
        if current != hashes["original_sha256"] and current not in accepted:
            raise SystemExit(f"원본과 다른 파일이 있어 중단했습니다 (아직 변경 없음): {path}\n현재 파일을 먼저 비교해주세요.")
        changes.append((name, data, path.exists()))
    if not changes:
        print("이미 같은 패치가 적용되어 있습니다.")
        return
    print("변경 대상:", ", ".join(name for name, _, _ in changes))
    if args.check:
        print("검증 통과. 파일은 변경하지 않았습니다.")
        return
    backup = target / ("modifier_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S_%f"))
    backup.mkdir()
    for name, _, existed in changes:
        if existed:
            shutil.copy2(target / name, backup / name)
    (backup / "new_files.json").write_text(json.dumps([name for name, _, existed in changes if not existed]))
    written = []
    try:
        for name, data, existed in changes:
            fd, temp = tempfile.mkstemp(prefix=".modifier_patch_", dir=target)
            try:
                with os.fdopen(fd, "wb") as stream:
                    stream.write(data)
                if existed:
                    shutil.copymode(target / name, temp)
                os.replace(temp, target / name)
                written.append((name, existed))
            finally:
                Path(temp).unlink(missing_ok=True)
    except BaseException:
        for name, existed in reversed(written):
            if existed:
                shutil.copy2(backup / name, target / name)
            else:
                (target / name).unlink(missing_ok=True)
        raise
    print(f"적용 완료. 백업: {backup}")
    print("vLLM/앱 프로세스와 Git은 조작하지 않았습니다. README_KO.md의 테스트를 실행해주세요.")


if __name__ == "__main__":
    main()
