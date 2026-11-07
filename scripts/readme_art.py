#!/usr/bin/env python3
"""Generate the glitch-punk SVG components under assets/readme/.

Everything is standalone SVG (no external fonts, images, scripts or CSS) so GitHub renders it
through <img>. Palette tokens live in scripts/theme.py (GLITCH). Run: python scripts/readme_art.py
"""
from __future__ import annotations

import random
from pathlib import Path

from theme import GLITCH as G

OUT = Path(__file__).resolve().parent.parent / "assets" / "readme"
R, C, M = G["red"], G["cyan"], G["magenta"]
N, P, T, S, B = G["ink"], G["panel"], G["text"], G["text2"], G["border"]
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
HEAD = "'Arial Black',Impact,'Segoe UI',system-ui,sans-serif"
W = 900


def svg(w: int, h: int, body: str, label: str, defs: str = "") -> str:
    d = f"<defs>{defs}</defs>" if defs else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{label}"><title>{label}</title>{d}{body}</svg>\n')


def write(rel: str, text: str) -> None:
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")


def scan(h: int, opacity: float = 0.04) -> tuple[str, str]:
    """Scanline pattern def + overlay rect."""
    d = f'<pattern id="sc" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="{T}"/></pattern>'
    return d, f'<rect width="{W}" height="{h}" fill="url(#sc)" opacity="{opacity}"/>'


def halftone(x: int, y: int, w: int, h: int, color: str, pid: str, opacity: float = 0.55) -> tuple[str, str]:
    """Dot field that fades out to the left (gradient mask)."""
    d = (f'<pattern id="{pid}" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="3.5" cy="3.5" r="1.25" fill="{color}"/></pattern>'
         f'<linearGradient id="{pid}g" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="{T}" stop-opacity="0"/><stop offset="1" stop-color="{T}"/></linearGradient>'
         f'<mask id="{pid}m"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{pid}g)"/></mask>')
    return d, f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{pid})" mask="url(#{pid}m)" opacity="{opacity}"/>'


# ---- section headers -------------------------------------------------------------------------
SECTIONS = [("01", "About Me", "about"), ("02", "Experience & Leadership", "experience"), ("03", "Education", "education"),
            ("04", "Projects", "projects"), ("05", "Tech Arsenal", "tech-arsenal"),
            ("06", "Achievements & Certifications", "achievements"), ("07", "System Metrics", "metrics"),
            ("08", "Establish Connection", "connect")]


def esc(t: str) -> str:
    return t.replace("&", "&amp;")


def header(num: str, title: str, odd: bool) -> str:
    acc, alt = (R, C) if odd else (C, R)
    ink = T if odd else N
    h = 64
    sd, so = scan(h)
    hd, ho = halftone(560, 8, 340, 48, acc, "ht")
    t = esc(title.upper())
    fs = 28 if len(title) <= 16 else 22
    body = (
        f'<rect width="{W}" height="{h}" fill="{N}"/>{ho}'
        # speed streaks
        f'<g transform="skewX(-30)" opacity=".9"><rect x="740" y="16" width="64" height="3" fill="{C}"/>'
        f'<rect x="700" y="27" width="110" height="3" fill="{R}"/><rect x="760" y="38" width="48" height="3" fill="{M}"/></g>'
        # glitch fragments
        f'<rect x="548" y="14" width="22" height="4" fill="{alt}"/><rect x="560" y="20" width="12" height="3" fill="{M}"/>'
        # tab with RGB-split edge
        f'<polygon points="5,8 129,8 113,56 5,56" fill="none" stroke="{M}" stroke-width="1.5"/>'
        f'<polygon points="0,8 124,8 108,56 0,56" fill="{acc}"/>'
        f'<text x="14" y="44" font-family="{MONO}" font-size="30" font-weight="800" font-style="italic" fill="{ink}">{num}</text>'
        # title: cyan/red + magenta split behind the main fill
        f'<g font-family="{HEAD}" font-size="{fs}" font-weight="900" font-style="italic" letter-spacing="1">'
        f'<text x="145.5" y="43" fill="{alt}">{t}</text><text x="150.5" y="43" fill="{M}">{t}</text>'
        f'<text x="148" y="43" fill="{T}">{t}</text></g>'
        # baseline: hairline + accent run
        f'<rect y="60" width="{W}" height="1" fill="{B}"/><polygon points="0,58 232,58 226,62 0,62" fill="{acc}"/>{so}'
    )
    return svg(W, h, body, f"{num} {esc(title)}", sd + hd)


def title_svg() -> str:
    h = 158
    name = "PRANNAVAKHANTH"
    role = "AI ENGINEER // SOFTWARE DEVELOPER // RESEARCHER"
    sd, so = scan(h, 0.05)
    hd, ho = halftone(0, 0, 300, h, C, "ht", 0.35)
    hd2, ho2 = halftone(600, 0, 300, h, R, "hu", 0.35)
    hd2 = hd2.replace('x1="0" x2="1"', 'x1="1" x2="0"')
    font = f'font-family="{HEAD}" font-size="58" font-weight="900" font-style="italic" letter-spacing="2" text-anchor="middle"'
    body = (
        f'<rect width="{W}" height="{h}" fill="{N}"/>{ho}{ho2}'
        f'<g transform="skewX(-30)"><rect x="170" y="38" width="70" height="3" fill="{C}"/><rect x="120" y="50" width="120" height="3" fill="{R}"/>'
        f'<rect x="180" y="62" width="60" height="3" fill="{M}"/>'
        f'<rect x="690" y="86" width="70" height="3" fill="{M}"/><rect x="650" y="98" width="120" height="3" fill="{C}"/>'
        f'<rect x="710" y="110" width="60" height="3" fill="{R}"/></g>'
        f'<g {font}><text x="447" y="86" fill="{C}">{name}</text><text x="453" y="86" fill="{M}">{name}</text>'
        f'<text x="450" y="86" fill="{R}">{name}</text>'
        f'<clipPath id="sl"><rect x="500" y="64" width="150" height="6"/></clipPath>'
        f'<g clip-path="url(#sl)"><text x="462" y="86" fill="{T}">{name}</text></g></g>'
        f'<text x="450" y="124" text-anchor="middle" font-family="{MONO}" font-size="15" font-weight="700" letter-spacing="3" fill="{C}">{role}</text>'
        f'<rect x="0" y="148" width="{W}" height="1" fill="{B}"/><polygon points="0,146 300,146 292,150 0,150" fill="{R}"/>'
        f'<polygon points="900,146 640,146 648,150 900,150" fill="{C}"/>{so}'
    )
    return svg(W, h, body, f"{name}: {role}", sd + hd + hd2)


def metric(value: str, label: str, acc: str) -> str:
    ink = R if acc == R else C
    body = (f'<polygon points="6,1 147,1 141,57 1,57" fill="{P}" stroke="{B}"/>'
            f'<polygon points="6,1 14,1 8,57 1,57" fill="{acc}"/>'
            f'<g font-family="{HEAD}" font-size="24" font-weight="900" font-style="italic">'
            f'<text x="23" y="29" fill="{M}">{value}</text>'
            f'<text x="22" y="28" fill="{T}">{value}</text></g>'
            f'<text x="22" y="46" font-family="{MONO}" font-size="8" font-weight="700" letter-spacing=".6" fill="{S}">{esc(label)}</text>'
            f'<rect x="22" y="50" width="26" height="2" fill="{acc}"/>')
    return svg(148, 58, body, esc(f"{value} {label}"))


# ---- dividers ---------------------------------------------------------------------------------
def dividers() -> dict[str, str]:
    rnd = random.Random(7)
    h = 28
    sd, so = scan(h, 0.05)
    frags = "".join(
        f'<rect x="{rnd.randint(320, 860)}" y="{rnd.choice([6, 10, 15, 19])}" width="{rnd.randint(8, 30)}" height="{rnd.choice([2, 3, 4])}" fill="{rnd.choice([C, M, R])}"/>'
        for _ in range(7))
    glitch = (f'<rect y="13" width="{W}" height="1" fill="{B}"/>'
              f'<polygon points="0,11 330,11 322,16 0,16" fill="{R}"/><polygon points="6,13 332,13 328,15 6,15" fill="{M}" opacity=".8"/>'
              f'{frags}{so}')
    red_cyan = (f'<rect y="13" width="{W}" height="1" fill="{B}"/>'
                f'<polygon points="0,6 540,6 530,11 0,11" fill="{R}"/><polygon points="360,17 900,17 900,22 350,22" fill="{C}"/>'
                f'<rect x="350" y="12" width="190" height="5" fill="{M}" opacity=".85"/>')
    lines = "".join(f'<rect y="{4 + i * 4}" width="{W}" height="1" fill="{B}" opacity="{1 - i * 0.14:.2f}"/>' for i in range(6))
    scanline = (f'{lines}<polygon points="0,4 60,4 56,24 0,24" fill="none"/>'
                f'<polygon points="420,10 480,10 476,17 416,17" fill="{C}"/><rect x="492" y="10" width="14" height="7" fill="{R}"/>')
    angular = (f'<polyline points="0,20 300,20 320,8 580,8 600,20 900,20" fill="none" stroke="{B}" stroke-width="2"/>'
               f'<polyline points="320,8 580,8" fill="none" stroke="{C}" stroke-width="3"/>'
               f'<polyline points="0,20 120,20" fill="none" stroke="{R}" stroke-width="3"/>'
               f'<polygon points="792,16 840,16 836,22 788,22" fill="{M}"/>')
    return {
        "dividers/glitch-divider.svg": svg(W, h, glitch, "Glitch divider", sd),
        "dividers/red-cyan-divider.svg": svg(W, h, red_cyan, "Red and cyan divider"),
        "dividers/scanline-divider.svg": svg(W, h, scanline, "Scanline divider"),
        "dividers/angular-divider.svg": svg(W, h, angular, "Angular divider"),
    }


# ---- frames & card edges ------------------------------------------------------------------
def frames() -> dict[str, str]:
    hd, ho = halftone(620, 0, 280, 30, C, "ht", 0.4)
    top = (f'<polygon points="0,0 {W},0 {W},30 0,30" fill="{N}"/>{ho}'
           f'<rect x="16" y="11" width="8" height="8" fill="{R}"/><rect x="30" y="11" width="8" height="8" fill="{C}"/>'
           f'<rect x="44" y="11" width="8" height="8" fill="{M}"/>'
           f'<text x="68" y="20" font-family="{MONO}" font-size="12" fill="{S}">dossier.txt</text>'
           f'<rect y="29" width="{W}" height="1" fill="{B}"/><polygon points="0,27 180,27 174,31 0,31" fill="{R}"/>')
    bottom = (f'<rect width="{W}" height="14" fill="{N}"/><rect width="{W}" height="1" fill="{B}"/>'
              f'<polygon points="900,0 720,0 726,4 900,4" fill="{C}"/><rect x="706" y="0" width="10" height="4" fill="{M}"/>')
    out = {"frames/dossier-top.svg": svg(W, 30, top, "dossier.txt", hd),
           "frames/dossier-bottom.svg": svg(W, 14, bottom, "End of dossier")}
    for name, acc in (("red", R), ("cyan", C)):
        edge = (f'<rect y="4" width="{W}" height="1" fill="{B}"/><polygon points="0,0 240,0 232,8 0,8" fill="{acc}"/>'
                f'<rect x="246" y="0" width="14" height="5" fill="{M}"/>')
        out[f"frames/card-top-{name}.svg"] = svg(W, 8, edge, "Card edge")
    return out


# ---- tags -------------------------------------------------------------------------------------
def num_tag(n: str, word: str, acc: str) -> str:
    ink = T if acc == R else N
    body = (f'<polygon points="5,2 62,2 56,50 5,50" fill="none" stroke="{M}" stroke-width="1.5"/>'
            f'<polygon points="0,2 58,2 52,50 0,50" fill="{acc}"/>'
            f'<text x="8" y="30" font-family="{HEAD}" font-size="22" font-weight="900" font-style="italic" fill="{ink}">{n}</text>'
            f'<text x="8" y="43" font-family="{MONO}" font-size="8" font-weight="700" letter-spacing="1" fill="{ink}">{word}</text>')
    return svg(64, 52, body, f"{word.title()} {n}")


def pill(label: str, acc: str) -> tuple[str, int]:
    w = int(len(label) * 7.6 + 48)
    body = (f'<polygon points="12,1 {w - 1},1 {w - 13},25 1,25" fill="{P}" stroke="{acc}" stroke-width="1.5"/>'
            f'<polygon points="12,1 28,1 16,25 1,25" fill="{acc}"/>'
            f'<text x="36" y="17" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing=".5" fill="{T}">{esc(label)}</text>')
    return svg(w, 26, body, esc(label)), w


def tags() -> dict[str, str]:
    out = {}
    for i in range(1, 4):
        out[f"tags/num-{i:02d}.svg"] = num_tag(f"{i:02d}", "FEATURED", R if i % 2 else C)
    items = {  # slug: (label, accent)
        "2026-present": ("2026 PRESENT", R), "2026-intern": ("2026 INTERN", C), "2025-research": ("2025 RESEARCH", C),
        "leadership-ospc": ("LEADERSHIP OSPC", R), "leadership-ieee": ("LEADERSHIP IEEE RAS", C), "leadership-vit": ("LEADERSHIP VIT", R),
        "win-2026": ("WIN 2026", R), "win-2025": ("WIN 2025", R), "recognition-2024": ("RECOGNITION 2024", C),
        "patent-2025": ("PATENT 2025", C), "patents-filed": ("PATENTS FILED", C),
        "papers-under-review": ("PAPERS UNDER REVIEW", C), "award-2026": ("AWARD 2026", R),
        "edu-vit": ("2023 — 2027", C), "edu-ps": ("CLASS XII · 2023", R), "cgpa": ("CGPA 9.08 / 10", R), "score-12": ("97.2%", C),
        "ach-vashisht": ("FIRST PLACE · VASHISHT", C), "ach-6l": ("₹6 LAKHS", R), "private": ("PRIVATE REPO", C),
        "grp-professional": ("PROFESSIONAL", R), "grp-leadership": ("LEADERSHIP", C),
        "grp-featured": ("FEATURED PROJECTS", R), "grp-additional": ("ADDITIONAL PROJECTS", C), "grp-oss": ("OPEN SOURCE & RESEARCH", R),
        "grp-hackathons": ("HACKATHONS & COMPETITIONS", R), "grp-patent": ("PATENTS, PAPERS & AWARDS", C), "grp-certs": ("CERTIFICATIONS", R),
    }
    for i, (v, l) in enumerate([("4", "ENTERPRISE PROJECTS"), ("10+", "AI/ML & SOFTWARE MODULES"), ("1,000+", "HOSPITAL DATASETS"),
                                ("97.5%", "RETRIEVAL ACCURACY"), ("73%", "FRAUD DETECTION ACCURACY")], 1):
        out[f"tags/metric-{i}.svg"] = metric(v, l, R if i % 2 else C)
    for slug, (label, acc) in items.items():
        out[f"tags/{slug}.svg"] = pill(label, acc)[0]
    cats = ["LANGUAGES", "WEB", "CORE CS", "AI & ML", "FRAMEWORKS & TOOLS", "DATA & CLOUD"]
    for i, c in enumerate(cats, 1):
        out[f"tags/cat-{i}.svg"] = pill(f"{i:02d} {c}", R if i % 2 else C)[0]
    return out


def main() -> None:
    for i, (num, title, slug) in enumerate(SECTIONS):
        write(f"headers/h{num}-{slug}.svg", header(num, title, i % 2 == 0))
    write("headers/title.svg", title_svg())
    for rel, text in {**dividers(), **frames(), **tags()}.items():
        write(rel, text)
    print("wrote", len(list(OUT.rglob("*.svg"))), "svgs to", OUT)


if __name__ == "__main__":
    main()
