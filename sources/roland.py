"""
roland.py — Roland video switcher library specs.

Run from the repo root:
    python3 sources/roland.py
which writes libraries/roland.xml.

Devices included (June 2026 stock sync):
    - V-40HD  — multi-format switcher
    - V-60HD  — multi-format switcher
    - XS-84H  — 8x4 matrix switcher
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "V-40HD",
        "name": "Roland V-40HD",
        "subtitle": "Multi-Format Switcher",
        "tags": ["Video", "Switcher"],
        "width": 170,
        "info_row": True,
        "inputs": [
            "HDMI 1",
            "HDMI 2",
            "HDMI 3",
            "HDMI 4",
            "RGB/Component 1-4",
            "Composite 1-4",
            "Audio In (TRS)",
        ],
        "outputs": [
            "PGM HDMI 1",
            "PGM HDMI 2",
            "PVW HDMI",
            "RGB/Component Out 1-2",
            "Composite Out",
        ],
        "control": ["RS-232", "Tally (D-sub 15)", "MIDI In/Out"],
    },
    {
        "title": "V-60HD",
        "name": "Roland V-60HD",
        "subtitle": "Multi-Format Switcher",
        "tags": ["Video", "Switcher"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["IP:"],
        "inputs": [
            "SDI 1",
            "SDI 2",
            "SDI 3",
            "SDI 4",
            "HDMI 5",
            "HDMI 6",
            "Audio In (XLR)",
        ],
        "outputs": [
            "SDI Out 1 (PGM)",
            "SDI Out 2 (AUX)",
            "HDMI Out 1 (PGM)",
            "HDMI Out 2",
            "Multiview HDMI",
            "Audio Out (XLR)",
        ],
        "control": ["LAN", "Tally / GPIO", "RS-232"],
    },
    {
        "title": "XS-84H",
        "name": "Roland XS-84H",
        "subtitle": "8x4 AV Matrix Switcher",
        "tags": ["Video", "Matrix"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["IP:"],
        "inputs": [
            "HDMI In 1-8",
            "Audio In 1-8 (2x Mic)",
        ],
        "outputs": [
            "HDMI Out 1-4 (HDMI/HDBT)",
            "Audio Out 1-4",
        ],
        "control": ["LAN", "RS-232C", "Remote"],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "roland.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
