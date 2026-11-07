#!/usr/bin/env python3
"""Lint every SVG under assets/: well-formed XML, no scripts or external references, size budgets,
and a palette audit (every colour must be a token from scripts/theme.py).

Exit code 1 on any failure. Usage: python scripts/lint_assets.py
"""
from __future__ import annotations

import re
import sys
import xml.dom.minidom as minidom
from pathlib import Path

from theme import ALLOWED

ASSETS = Path(__file__).resolve().parent.parent / "assets"
BUDGET_KB = {"globe": 60, "heatmap": 40, "logos": 8}
COLOUR = re.compile(r"#[0-9a-fA-F]{6}(?![0-9a-fA-F])|#[0-9a-fA-F]{3}(?![0-9a-fA-F])")
FORBIDDEN = re.compile(r"<script|<foreignObject|<image\b|@import|xlink:href|\bhref=|url\((?!#)", re.I)


def budget(path: Path) -> int:
    if path.parent.name == "logos":
        return BUDGET_KB["logos"]
    return next((v for k, v in BUDGET_KB.items() if path.name.startswith(k)), 60)


def main() -> int:
    bad = 0
    for f in sorted(ASSETS.rglob("*.svg")):
        text = f.read_text(encoding="utf-8")
        problems = []
        try:
            minidom.parseString(text)
        except Exception as e:  # malformed XML
            problems.append(f"XML: {e}")
        if m := FORBIDDEN.search(text):
            problems.append(f"forbidden construct: {m.group(0)}")
        off = sorted({c.lower() for c in COLOUR.findall(text)} - ALLOWED)
        if off:
            problems.append(f"off-palette colours: {', '.join(off)}")
        kb = len(text.encode()) / 1024
        if kb > budget(f):
            problems.append(f"{kb:.1f} KB over {budget(f)} KB budget")
        print(("FAIL" if problems else "ok  "), f.relative_to(ASSETS.parent), f"{kb:.1f}KB", "; ".join(problems))
        bad += bool(problems)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
