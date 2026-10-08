#!/usr/bin/env python3
"""Archive generated files and recovery copies; keep active project paths."""
import argparse
from collections import Counter
from datetime import datetime
import json
import os
from pathlib import Path
import re
import tempfile

from archive_backups import move_all


PRESERVE_DIRS = {
    '.git', '.venv', 'venv', 'env', 'node_modules', 'models', 'outputs',
    'checkpoints', 'runtime_data', 'dataset_v14', 'router_data',
    'regression_cases', 'regression_results', 'llm_backups',
}
CACHE_DIRS = {'__pycache__', '.pytest_cache'}
LEGACY = re.compile(r'\.py\.(?:STABLE_80PASS|before_rollback|disabled|ab_current_\d+_\d+|failed_modify_min_\d+_\d+)$')


def plan(target):
    entries = []
    for current, dirs, files in os.walk(target, followlinks=False):
        current = Path(current)
        for name in sorted(dirs[:]):
            path = current / name
            if path.is_symlink() or name in PRESERVE_DIRS or name.endswith('_venv'):
                dirs.remove(name)
                continue
            kind = '캐시' if name in CACHE_DIRS else '패치 백업' if name.startswith('modifier_backup_') else None
            if kind:
                entries.append({'path': path.relative_to(target).as_posix(), 'kind': kind})
                dirs.remove(name)
        for name in sorted(files):
            path = current / name
            if path.is_symlink():
                continue
            kind = None
            if name.endswith(('.bak', '.backup', '~')) or ('.bak_' in name and path.suffix not in {'.py', '.sh'}):
                kind = '백업 사본'
            elif LEGACY.search(name):
                kind = '이전 버전 사본'
            elif current == target and name == 'llm.zip':
                kind = '이전 프로젝트 압축본'
            if kind:
                entries.append({'path': path.relative_to(target).as_posix(), 'kind': kind})
    return sorted(entries, key=lambda entry: entry['path'])


def restore(archive, override):
    manifest = json.loads((archive / 'manifest.json').read_text())
    target = override.expanduser().resolve() if override else Path(manifest['target'])
    if not target.is_absolute() or not target.is_dir():
        raise ValueError('원래 프로젝트 폴더가 없습니다. --target으로 위치를 지정하세요.')
    pairs = []
    seen = set()
    for entry in manifest['entries']:
        relative = Path(entry['path'])
        if relative.is_absolute() or '..' in relative.parts or str(relative) in ('', '.') or relative in seen:
            raise ValueError('잘못된 복원 목록입니다.')
        seen.add(relative)
        destination = target / relative
        if not destination.resolve().is_relative_to(target.resolve()):
            raise ValueError('프로젝트 밖의 경로에는 복원하지 않습니다.')
        if not destination.parent.is_dir():
            raise ValueError(f'원래 폴더를 먼저 확인해주세요: {destination.parent}')
        pairs.append((archive / 'files' / relative, destination))
    move_all(pairs)
    print(f'{len(pairs)}개 항목 복원 완료: {target}')


def main():
    parser = argparse.ArgumentParser(description='전체 프로젝트의 백업·캐시를 별도 보관 (삭제 없음)')
    parser.add_argument('--target', type=Path, help='기본: ~/soomac_3.0-IRC_ASZ')
    parser.add_argument('--list', action='store_true', help='대상 경로 전체 표시')
    action = parser.add_mutually_exclusive_group()
    action.add_argument('--apply', action='store_true')
    action.add_argument('--restore', type=Path, help='보관 폴더에서 복원')
    args = parser.parse_args()
    if args.restore:
        restore(args.restore.expanduser().resolve(), args.target)
        return
    target = (args.target or Path.home() / 'soomac_3.0-IRC_ASZ').expanduser().resolve()
    if not target.is_dir():
        raise ValueError(f'프로젝트 폴더가 없습니다: {target}')
    entries = plan(target)
    for kind, count in sorted(Counter(entry['kind'] for entry in entries).items()):
        print(f'{kind}: {count}개 항목')
    if args.list:
        for entry in entries:
            print(entry['path'])
    print(f'총 보관 대상: {len(entries)}개 항목')
    if not args.apply:
        print('미리보기입니다. 실제로 옮기려면 --apply를 붙이세요.')
        return
    if not entries:
        return
    parent = target.parent / (target.name + '_archive')
    parent.mkdir(exist_ok=True)
    archive = Path(tempfile.mkdtemp(prefix=datetime.now().strftime('%Y%m%d_%H%M%S_'), dir=parent))
    (archive / 'manifest.json').write_text(json.dumps({'target': str(target), 'entries': entries}, ensure_ascii=False, indent=2) + '\n')
    pairs = []
    for entry in entries:
        destination = archive / 'files' / entry['path']
        destination.parent.mkdir(parents=True, exist_ok=True)
        pairs.append((target / entry['path'], destination))
    move_all(pairs)
    print(f'보관 완료: {archive}')
    print('복원: python3 tools/organize_project.py --restore 위_보관_폴더_경로')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit(f'정리 중단: {exc}')
