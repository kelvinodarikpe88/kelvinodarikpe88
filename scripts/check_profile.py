#!/usr/bin/env python3
"""Check profile integrity offline; never fetch recruiter data or alter metrics."""
from pathlib import Path
import re
import runpy
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]

def main() -> None:
    errors = []
    for p in [ROOT/'README.md', *sorted((ROOT/'docs').glob('*.md'))]:
        for link in re.findall(r'\]\(([^)]+)\)', p.read_text()):
            target = link.split('#')[0].split('?')[0]
            if target and not urlparse(target).scheme and not (p.parent/unquote(target)).exists():
                errors.append(f'{p.relative_to(ROOT)}: missing {target}')
    for p in (ROOT/'assets').glob('*.svg'):
        try:
            tree = ET.parse(p)
            for e in tree.iter():
                if e.tag.split('}')[-1] in {'script','foreignObject'}:
                    errors.append(f'{p.name}: executable/embedded content')
        except ET.ParseError as e:
            errors.append(f'{p.name}: {e}')
    readme = (ROOT/'README.md').read_text()
    for url in re.findall(r'(?:src|srcset)="([^"]+)"', readme):
        parsed = urlparse(url)
        if parsed.hostname == 'raw.githubusercontent.com':
            prefix='/kelvinodarikpe88/kelvinodarikpe88/main/'
            if not parsed.path.startswith(prefix) or not (ROOT/parsed.path.removeprefix(prefix)).is_file():
                errors.append(f'Unresolved profile image: {url}')
    nav='[**Hiring brief**](docs/HIRING.md) · [**CISO brief**](docs/CISO-BRIEF.md) · [**Project index**](docs/PORTFOLIO.md)'
    if nav not in readme:
        errors.append('Primary navigation must retain the three requested index links')
    if 'prefers-reduced-motion: reduce' not in readme:
        errors.append('Missing reduced-motion still image')
    generated=runpy.run_path(str(ROOT/'build_profile_assets.py'))
    for name, builder in generated['BUILDERS'].items():
        if (ROOT/'assets'/name).read_text() != builder():
            errors.append(f'{name}: regenerate from build_profile_assets.py')
    motion=runpy.run_path(str(ROOT/'scripts'/'motion_svg.py'))
    if (ROOT/'assets'/'security-ai-motion.svg').read_text() != motion['frame'](18):
        errors.append('Motion still differs from generator')
    gif=(ROOT/'assets'/'security-ai-motion.gif').read_bytes()
    if gif[:6] not in (b'GIF87a',b'GIF89a') or b'NETSCAPE2.0\x03\x01\x02\x00\x00' not in gif:
        errors.append('Motion must be a GIF with three cycles (loop count 2)')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('PASS: links, local image targets, SVG safety, reproducible diagrams, navigation and finite motion.')

if __name__ == '__main__':
    main()
