#!/usr/bin/env python3
"""Install the bundled skill without overwriting existing installations."""

import argparse
import os
from pathlib import Path
import shutil
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--client', required=True, choices=('claude', 'codex', 'both'))
    parser.add_argument('--scope', default='user', choices=('user', 'project'))
    parser.add_argument('--project', type=Path, help='Existing project directory; required for project scope')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    if args.scope == 'project' and args.project is None:
        parser.error('--project is required for project scope')
    if args.scope == 'user' and args.project is not None:
        parser.error('--project requires --scope project')
    base = args.project.expanduser().resolve() if args.scope == 'project' else Path.home()
    if not base.is_dir():
        parser.error(f'Installation root is not an existing directory: {base}')
    source = Path(__file__).resolve().parent / 'instagram-edits-desktop'
    if not (source / 'SKILL.md').is_file() or not (source / 'references').is_dir():
        parser.error('Skill source is incomplete. Extract the entire release ZIP first.')
    clients = ('claude', 'codex') if args.client == 'both' else (args.client,)
    locations = {'claude': '.claude', 'codex': '.agents'}
    destinations = [base / locations[c] / 'skills' / source.name for c in clients]
    # Preflight every target before installing either client.
    for destination in destinations:
        if os.path.lexists(destination):
            parser.error(f'Refusing to overwrite existing path: {destination}')
        ancestor = destination.parent
        while not os.path.lexists(ancestor):
            ancestor = ancestor.parent
        if not ancestor.is_dir():
            parser.error(f'Destination parent is not a directory: {ancestor}')
    if args.dry_run:
        for client, destination in zip(clients, destinations):
            print(f'Would install for {client}: {destination}')
        return 0
    created = []
    try:
        for destination in destinations:
            destination.parent.mkdir(parents=True, exist_ok=True)
            # Reserve the leaf so an existing path is never replaced.
            destination.mkdir()
            created.append(destination)
            shutil.copytree(source, destination, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
    except OSError as exc:
        for destination in reversed(created):
            shutil.rmtree(destination)
        print(f'Installation failed; new skill copies rolled back: {exc}', file=sys.stderr)
        return 1
    for client, destination in zip(clients, destinations):
        print(f'Installed for {client}: {destination}')
    print('Refresh your client. Connect Edits MCP separately using the setup in Edits Settings.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
