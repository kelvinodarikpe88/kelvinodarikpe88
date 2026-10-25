#!/usr/bin/env python3
"""Render an illustrative security/AI workflow; no live telemetry or model calls.
Requires rsvg-convert on PATH and Pillow. Run from any directory.
"""
from pathlib import Path
import io
import subprocess
import tempfile
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
from motion_svg import frame

def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    images = []
    with tempfile.TemporaryDirectory() as tmp:
        source = Path(tmp) / 'frame.svg'
        for t in range(36):
            source.write_text(frame(t))
            png = subprocess.check_output(['rsvg-convert', str(source)])
            images.append(Image.open(io.BytesIO(png)).convert('RGB'))
    (ASSETS/'security-ai-motion.svg').write_text(frame(18))
    images[18].save(ASSETS/'security-ai-motion.png')
    images[0].save(ASSETS/'security-ai-motion.gif', save_all=True, append_images=images[1:], duration=150, loop=2, optimize=True, disposal=2)
    print('Rendered 36 frames, three cycles, plus static SVG and PNG.')

if __name__ == '__main__':
    main()
