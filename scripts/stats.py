#!/usr/bin/env python3
"""Fetch GitHub activity and regenerate the heatmap SVGs plus the README stats block.

Env:  GH_TOKEN (required for a live fetch), GH_LOGIN (default: prnvvv).
Flow: GraphQL -> data/stats.json (cache) -> assets/heatmap-{dark,light}.svg
      -> text between <!-- STATS:START --> and <!-- STATS:END --> in README.md.
Fallback: if the API call fails, the cached data is re-rendered (a no-op when
nothing changed); with no cache, every committed file is left untouched. Never raises.
Requires: Python 3.11+, requests.
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
LOGIN = os.environ.get("GH_LOGIN", "prnvvv")
CACHE = ROOT / "data" / "stats.json"
README = ROOT / "README.md"
START, END = "<!-- STATS:START -->", "<!-- STATS:END -->"

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    repositories(privacy: PUBLIC, ownerAffiliations: OWNER) { totalCount }
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount weekday } }
      }
    }
  }
}
"""

# Five levels (tokens from scripts/theme.py GLITCH): empty panel -> red ramp -> cyan peak. The SVG carries
# its own navy panel, so both theme files share one palette.
_LEVELS = ["#161b22", "#3a0c2a", "#9c0a3c", "#ff0033", "#00e5ff"]
PALETTE = {
    "dark": {"levels": _LEVELS, "label": "#aab4c3"},
    "light": {"levels": _LEVELS, "label": "#aab4c3"},
}
PAD = 14
CELL, GAP, LEFT, TOP = 10, 3, 30, 18
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def streaks(days: list[dict], today: str) -> tuple[int, int]:
    """(current, longest). An empty *today* does not break the current streak."""
    longest = run = 0
    for d in days:
        run = run + 1 if d["count"] else 0
        longest = max(longest, run)
    cur = 0
    for d in reversed([d for d in days if d["date"] <= today]):
        if d["count"]:
            cur += 1
        elif d["date"] == today:
            continue
        else:
            break
    return cur, longest


def fetch(login: str, token: str) -> dict:
    now = datetime.now(timezone.utc)
    variables = {
        "login": login,
        "from": (now - timedelta(days=364)).strftime("%Y-%m-%dT00:00:00Z"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    r = requests.post("https://api.github.com/graphql", json={"query": QUERY, "variables": variables},
                      headers={"Authorization": f"bearer {token}"}, timeout=30)
    r.raise_for_status()
    body = r.json()
    user = (body.get("data") or {}).get("user")
    if body.get("errors") or not user:
        raise RuntimeError(f"GraphQL error: {body.get('errors')}")
    cal = user["contributionsCollection"]["contributionCalendar"]
    weeks = [[(d["date"], d["contributionCount"]) for d in w["contributionDays"]]
             for w in cal["weeks"] if w["contributionDays"]]
    flat = [{"date": d, "count": c} for w in weeks for d, c in w]
    cur, longest = streaks(flat, now.date().isoformat())
    return {
        "login": login, "synced": now.date().isoformat(), "total": cal["totalContributions"],
        "repos": user["repositories"]["totalCount"], "current_streak": cur, "longest_streak": longest,
        "weeks": weeks,
    }


def level_fn(counts: list[int]):
    """Map a daily count to 0-4 using quartiles of the non-zero days."""
    nz = sorted(c for c in counts if c)
    if not nz:
        return lambda c: 0
    cuts = [nz[min(len(nz) - 1, int(len(nz) * q))] for q in (0.25, 0.5, 0.75)]
    return lambda c: 0 if c == 0 else 1 + sum(c > t for t in cuts)


def heatmap(data: dict, theme: str) -> str:
    pal = PALETTE[theme]
    weeks = data["weeks"][-53:]
    lvl = level_fn([c for w in weeks for _, c in w])
    pitch = CELL + GAP
    width, height = LEFT + len(weeks) * pitch - GAP, TOP + 7 * pitch - GAP
    groups: list[list[str]] = [[] for _ in range(5)]
    for i, w in enumerate(weeks):
        for d, c in w:
            wd = (date.fromisoformat(d).weekday() + 1) % 7  # Sunday = 0
            groups[min(4, lvl(c))].append(f'<rect x="{LEFT + i * pitch}" y="{TOP + wd * pitch}" width="{CELL}" height="{CELL}" rx="2"/>')
    labels, last = [], -9
    for i, w in enumerate(weeks):
        month = date.fromisoformat(w[0][0]).month
        prev = date.fromisoformat(weeks[i - 1][0][0]).month if i else None
        if month != prev and i - last >= 3 and i <= len(weeks) - 3:
            labels.append(f'<text x="{LEFT + i * pitch}" y="10">{MONTHS[month - 1]}</text>')
            last = i
    days = "".join(f'<text x="0" y="{TOP + r * pitch + 9}">{n}</text>' for r, n in ((1, "Mon"), (3, "Wed"), (5, "Fri")))
    cells = "".join(f'<g fill="{pal["levels"][k]}">{"".join(g)}</g>' for k, g in enumerate(groups))
    css = ("@keyframes f{from{opacity:0}to{opacity:1}}.c{animation:f 1.2s ease-out both}"
           "@media (prefers-reduced-motion:reduce){.c{animation:none}}"
           f"text{{font:10px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:{pal['label']}}}")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
            f'role="img" aria-label="Contribution heatmap, last 12 months"><style>{css}</style>'
            f'{"".join(labels)}{days}<g class="c">{cells}</g></svg>\n')


def stats_block(d: dict) -> str:
    th = "".join(f'<th align="left" width="250">{h}</th>' for h in ("Contributions", "Current streak", "Longest streak", "Public repos"))
    vals = (f"{d['total']:,}", f"{d['current_streak']} days", f"{d['longest_streak']} days", str(d["repos"]))
    td = "".join(f'<td width="250">{v}</td>' for v in vals)
    return (f"<table>\n<tr>{th}</tr>\n<tr>{td}</tr>\n</table>\n\n"
            f"<sub>Last 12 months, synced {d['synced']}. Live graph: "
            f"[github.com/{d['login']}](https://github.com/{d['login']}).</sub>")


def write_if_changed(path: Path, text: str) -> None:
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8", newline="\n")


def render(d: dict) -> None:
    for theme in PALETTE:
        write_if_changed(ROOT / "assets" / f"heatmap-{theme}.svg", heatmap(d, theme))
    text = README.read_text(encoding="utf-8")
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pat.search(text):
        raise RuntimeError("stats markers not found in README.md")
    write_if_changed(README, pat.sub(lambda _: f"{START}\n{stats_block(d)}\n{END}", text))


def main() -> int:
    data = None
    try:
        token = os.environ.get("GH_TOKEN", "")
        if not token:
            raise RuntimeError("GH_TOKEN not set")
        data = fetch(LOGIN, token)
        write_if_changed(CACHE, json.dumps(data, separators=(",", ":")) + "\n")
        print(f"fetched {LOGIN}: {data['total']} contributions")
    except Exception as e:  # keep what is committed; never fail the workflow
        print(f"fetch skipped: {e}", file=sys.stderr)
        try:
            data = json.loads(CACHE.read_text(encoding="utf-8"))
            print("using cached stats", file=sys.stderr)
        except Exception:
            print("no cache; leaving committed files untouched", file=sys.stderr)
    if data:
        try:
            render(data)
        except Exception as e:
            print(f"render skipped: {e}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
