"""
disguise.py — disguise media server library specs.

ON ORDER (purchase list, May 2026). Port layouts verified against disguise
spec sheets, June 2026:
    - EX 3+  — 2U RenderStream render node (RTX 4000 Ada)
    - GX 2c  — 4U generative/Notch server, 2x VFC output slots
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "EX 3+",
        "name": "disguise EX 3+",
        "subtitle": "RenderStream Render Node",
        "tags": ["Video", "Media Server", "On Order"],
        "width": 190,
        "info_row": True,
        "loose_ports": ["IP:", "Genlock In (BNC)"],
        "inputs": [
            "SDI Capture (1x12G / 4x3G HD-BNC)",
            "HDMI 2.0 Capture",
        ],
        "outputs": [
            "DP 1.4 Out 1",
            "DP 1.4 Out 2",
            "DP 1.4 Out 3",
            "DP 1.4 GUI",
        ],
        "control": [
            "10GbE A",
            "10GbE B",
            "100G QSFP28 C",
            "100G QSFP28 D",
            "Mgmt Ethernet",
            "USB 3.2 x2",
        ],
    },
    {
        "title": "GX 2c",
        "name": "disguise GX 2c",
        "subtitle": "Generative Media Server",
        "tags": ["Video", "Media Server", "On Order"],
        "width": 190,
        "info_row": True,
        "loose_ports": ["IP:", "Genlock In (BNC)", "Genlock Loop"],
        "inputs": [
            "SDI Capture 1-8 (3G HD-BNC)",
            "Audio In L/R (XLR)",
            "ADAT/SPDIF In",
            "MIDI In",
        ],
        "outputs": [
            "VFC Slot 1 (HDMI 2.0)",
            "VFC Slot 2 (HDMI 2.0)",
            "DP 1.2 GUI",
            "Audio Out L/R (XLR)",
            "ADAT/SPDIF Out",
            "MIDI Out",
        ],
        "control": [
            "GbE (d3Net)",
            "GbE (Art-Net)",
            "10GbE Media x2",
            "USB 3.0 x5",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "disguise.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
