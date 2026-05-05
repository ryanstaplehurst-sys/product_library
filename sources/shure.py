"""shure.py — Shure mic library specs."""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "MX412",
        "name": "Shure MX412",
        "subtitle": "Lectern Gooseneck Mic",
        "tags": ["Audio", "Mic"],
        "width": 160,
        "info_row": True,
        "outputs": [
            "Mic Out (XLR)",
        ],
    },
    {
        "title": "SM58",
        "name": "Shure SM58",
        "subtitle": "Wired Handheld Mic",
        "tags": ["Audio", "Mic"],
        "width": 160,
        "info_row": True,
        "outputs": [
            "Mic Out (XLR)",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "shure.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
