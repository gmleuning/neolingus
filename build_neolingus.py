#!/usr/bin/env python3
"""Wrap the BEOLINGUS/Ding source text file into neolingus-data.js so that
neolingus.html can load it straight from disk (browsers block reading
local .txt files from a page, but they allow a local <script src>).

Run it from the folder that holds the txt:
    py build_neolingus.py
or name the files explicitly:
    py build_neolingus.py chemnitz_beolingus_de-en.txt neolingus-data.js
Re-run whenever you replace the txt with a newer version.
"""
import json, sys
from pathlib import Path

here = Path(__file__).resolve().parent
src = Path(sys.argv[1]) if len(sys.argv) > 1 else here / 'chemnitz_beolingus_de-en.txt'
out = Path(sys.argv[2]) if len(sys.argv) > 2 else here / 'neolingus-data.js'

text = src.read_text(encoding='utf-8').replace('\r\n', '\n').replace('\r', '\n')
out.write_text('window.NEOLINGUS_DATA=' + json.dumps(text, ensure_ascii=False) + ';\n', encoding='utf-8')
lines = sum(1 for l in text.split('\n') if l and not l.startswith('#'))
print(f'{lines:,} dictionary lines -> {out.name} ({out.stat().st_size / 1e6:.1f} MB)')
