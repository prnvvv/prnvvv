"""Design tokens shared by the asset generators and the palette audit.

Neutrals carry about 90% of the page. Two accents only: amber marks AI/ML, numerals and
active states; teal marks systems, data and infrastructure.
"""
from __future__ import annotations

TOKENS: dict[str, dict[str, str]] = {
    "dark": {
        "ink": "#0d1117", "surface": "#12171f", "hairline": "#262e38",
        "text": "#e6edf3", "muted": "#8b949e", "dim": "#6e7681",
        "amber": "#f0883e", "amber_tint": "#3a2616",
        "teal": "#4db6c6", "teal_tint": "#11303a",
    },
    "light": {
        "ink": "#ffffff", "surface": "#f6f8fa", "hairline": "#d0d7de",
        "text": "#1f2328", "muted": "#59636e", "dim": "#6e7781",
        "amber": "#c2570c", "amber_tint": "#fbe4d2",
        "teal": "#0e7490", "teal_tint": "#d3eef3",
    },
}

# Colours owned by the two existing generators (globe, heatmap); kept here so the audit knows them.
EXTRA = {
    "#c9d1d9", "#57606a", "#30363d",                  # globe dots / limb
    "#161b22", "#7a4421", "#ffb77a",                  # heatmap dark: empty, mid amber, peak
    "#eaeef2", "#f3b98c", "#8a3d08",                  # heatmap light: empty, mid amber, peak
}

# Glitch-punk README theme (assets/readme/ and the heatmap). Neutrals plus red, cyan and magenta.
GLITCH = {
    "ink": "#0d0d2b", "panel": "#161b22", "border": "#30363d",
    "text": "#e6edf3", "text2": "#aab4c3", "muted": "#8b949e",
    "red": "#ff0033", "cyan": "#00e5ff", "magenta": "#e6007e",
    "red_lo": "#3a0c2a", "red_mid": "#9c0a3c",   # heatmap ramp steps between panel and red
}

ALLOWED = {c for t in TOKENS.values() for c in t.values()} | EXTRA | set(GLITCH.values())

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SANS = "-apple-system,'Segoe UI',system-ui,sans-serif"
