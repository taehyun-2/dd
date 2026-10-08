#!/usr/bin/env python3
"""Preview or archive top-level backup files without deleting project data."""
import argparse
from datetime import datetime
import json
from pathlib import Path
import shutil
import tempfile


def candidates(target):
    result = []
    for path in sorted(target.iterdir()):
        if path.is_symlink():
            continue
        name = path.name
        if path.is_file() and (
            name.endswith(('.bak', '.backup', '~')) or '.bak_' in name
        ):
            result.append(path)
        elif path.is_dir() and name.startswith('modifier_backup_'):
            result.append(path)
    return result


def move_all(pairs):
    # All destinations must be absent; roll back completed moves on failure.
    for source, destination in pairs:
        if not source.exists() or source.is_symlink():
            raise ValueError(f'원본을 확인해주세요: {source}')
        if destination.exists() or destination.is_symlink():
            raise ValueError(f'이미 있는 파일을 덮어쓰지 않습니다: {destination}')
    completed = []
    try:
        for source, destination in pairs:
            shutil.move(str(source), str(destination))
            completed.append((source, destination))
    except BaseException:
        for source, destination in reversed(completed):
            shutil.move(str(destination), str(source))
        raise


def restore(archive):
    manifest = json.loads((archive / 'manifest.json').read_text())
    target = Path(manifest['target'])
    if not target.is_absolute() or not target.is_dir():
        raise ValueError('복원할 원래 프로젝트 폴더를 찾을 수 없습니다.')
    names = manifest['names']
    if not names or len(set(names)) != len(names) or any(
        not isinstance(name, str) or Path(name).name != name or name in ('.', '..')
        for name in names
    ):
        raise ValueError('보관 목록의 파일 이름이 올바르지 않습니다.')
    move_all([(archive / name, target / name) for name in names])
    print(f'{len(names)}개 항목 복원 완료: {target}')


def main():
    parser = argparse.ArgumentParser(description='백업 목록 확인 → 별도 폴더로 이동 (삭제 없음)')
    parser.add_argument('--target', type=Path, default=Path.home() / 'soomac_3.0-IRC_ASZ/llm')
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument('--apply', action='store_true', help='목록의 백업을 실제로 옮깁니다.')
    actions.add_argument('--restore', type=Path, help='보관 폴더를 지정해 원래 위치로 복원합니다.')
    args = parser.parse_args()
    if args.restore:
        restore(args.restore.expanduser().resolve())
        return
    target = args.target.expanduser().resolve()
    if not target.is_dir():
        raise ValueError(f'프로젝트 폴더가 없습니다: {target}')
    selected = candidates(target)
    for path in selected:
        print(path.name + ('/' if path.is_dir() else ''))
    print(f'보관 대상: {len(selected)}개 항목')
    if not args.apply:
        print('미리보기입니다. 실제로 옮기려면 같은 명령에 --apply를 붙이세요.')
        return
    if not selected:
        return
    parent = target.parent / (target.name + '_backups')
    parent.mkdir(exist_ok=True)
    archive = Path(tempfile.mkdtemp(prefix=datetime.now().strftime('%Y%m%d_%H%M%S_'), dir=parent))
    manifest = {'target': str(target), 'names': [path.name for path in selected]}
    (archive / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    move_all([(path, archive / path.name) for path in selected])
    print(f'보관 완료: {archive}')
    print('복원하려면 이 스크립트에 --restore와 위 보관 폴더 경로를 지정하세요.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit(f'정리 중단: {exc}')
