"""
_cables.py — Build the cable-styles draw.io library.

Each entry is a small "sample" graph: two anchor dots connected by a styled
edge, plus a label. When the team drags one onto a canvas, they get a clean
pre-styled edge ready to attach between device ports.

Run: python3 sources/_cables.py  →  libraries/_cables.xml
"""

from __future__ import annotations

import html
import json
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from cable_styles import CABLE_STYLES  # noqa: E402


SAMPLE_W = 220
SAMPLE_H = 30
DOT_STYLE = (
    "ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=none;"
    "aspect=fixed;"
)
LABEL_STYLE = (
    "text;html=1;align=center;verticalAlign=middle;resizable=0;"
    "points=[];autosize=1;strokeColor=none;fillColor=none;"
)


def _build_sample_xml(style: str, label: str) -> str:
    label_attr = html.escape(label, quote=True)
    return (
        '<mxGraphModel><root>'
        '<mxCell id="0"/>'
        '<mxCell id="1" parent="0"/>'
        # Left dot
        f'<mxCell id="2" style="{DOT_STYLE}" vertex="1" parent="1">'
        f'<mxGeometry x="0" y="13" width="6" height="6" as="geometry"/>'
        '</mxCell>'
        # Right dot
        f'<mxCell id="3" style="{DOT_STYLE}" vertex="1" parent="1">'
        f'<mxGeometry x="214" y="13" width="6" height="6" as="geometry"/>'
        '</mxCell>'
        # Edge between
        f'<mxCell id="4" style="{style}" edge="1" parent="1" source="2" target="3">'
        '<mxGeometry relative="1" as="geometry"/>'
        '</mxCell>'
        # Label
        f'<mxCell id="5" value="{label_attr}" style="{LABEL_STYLE}" vertex="1" parent="1">'
        f'<mxGeometry x="60" y="-2" width="100" height="14" as="geometry"/>'
        '</mxCell>'
        '</root></mxGraphModel>'
    )


def build() -> str:
    entries = []
    for key, meta in CABLE_STYLES.items():
        if key == "generic":
            continue  # No need to expose a "generic black line" tile
        xml = _build_sample_xml(meta["style"], meta["label"])
        entries.append(
            {
                "xml": html.escape(xml, quote=False),
                "w": SAMPLE_W,
                "h": SAMPLE_H,
                "aspect": "fixed",
                "title": meta["label"],
            }
        )
    return f"<mxlibrary>{json.dumps(entries, indent=2, ensure_ascii=False)}</mxlibrary>\n"


if __name__ == "__main__":
    out = REPO / "libraries" / "_cables.xml"
    out.write_text(build(), encoding="utf-8")
    print(f"Wrote {out} ({len(CABLE_STYLES) - 1} cable styles)")
