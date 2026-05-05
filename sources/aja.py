"""aja.py — AJA library specs."""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "1x6 SDI DA",
        "name": "AJA 1×6 SDI DA",
        "subtitle": "SDI Distribution Amp",
        "tags": ["Video", "Distribution"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "SDI In",
        ],
        "outputs": [
            "SDI Out 1",
            "SDI Out 2",
            "SDI Out 3",
            "SDI Out 4",
            "SDI Out 5",
            "SDI Out 6",
        ],
    },
    {
        "title": "C10DA",
        "name": "AJA C10DA",
        "subtitle": "Analog 1×6 DA + Sync Gen",
        "tags": ["Video", "Distribution", "Sync"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "Composite In",
        ],
        "outputs": [
            "Composite Out 1",
            "Composite Out 2",
            "Composite Out 3",
            "Composite Out 4",
            "Composite Out 5",
            "Composite Out 6",
            "Sync Out (BNC)",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "aja.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
