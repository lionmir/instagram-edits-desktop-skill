#!/usr/bin/env python3
"""Build the v0.1.0 public skill archive from an explicit file allowlist."""

import hashlib
from pathlib import Path
import zipfile


def main():
    root = Path(__file__).resolve().parents[1]
    skill = root / 'instagram-edits-desktop'
    files = [root / name for name in ('README.md', 'LICENSE', 'install.py')]
    files += [skill / 'SKILL.md', skill / 'agents/openai.yaml']
    files += sorted((skill / 'references').glob('*.md'))
    output = root / 'dist'
    output.mkdir(exist_ok=True)
    archive = output / 'instagram-edits-desktop-v0.1.0.zip'
    # The README's maintainer build command also works from the release ZIP.
    files.append(Path(__file__).resolve())
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as bundle:
        for path in files:
            relative = Path('instagram-edits-desktop-v0.1.0') / path.relative_to(root)
            info = zipfile.ZipInfo(str(relative), (2026, 11, 5, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, path.read_bytes())
    with zipfile.ZipFile(archive) as bundle:
        assert bundle.testzip() is None
        assert len(bundle.namelist()) == len(files)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / 'SHA256SUMS.txt').write_text(f'{digest}  {archive.name}\n')
    print(f'Built {archive.name}: {len(files)} files; SHA-256 {digest}')


if __name__ == '__main__':
    main()
