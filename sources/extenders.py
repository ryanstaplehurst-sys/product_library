"""
extenders.py — HDMI/USB extenders + small video switchers.
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "LINDY USB CAT5 TX",
        "name": "LINDY USB 2.0 CAT5",
        "subtitle": "USB Extender (TX)",
        "tags": ["USB", "Extender"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "USB-B (PC)",
        ],
        "outputs": [
            "Cat5 Out (RJ45)",
        ],
    },
    {
        "title": "LINDY USB CAT5 RX",
        "name": "LINDY USB 2.0 CAT5",
        "subtitle": "USB Extender (RX)",
        "tags": ["USB", "Extender"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "Cat5 In (RJ45)",
        ],
        "outputs": [
            "USB-A 1",
            "USB-A 2",
        ],
    },
    {
        "title": "Neoteck HDMI Ext RX",
        "name": "Neoteck HDMI Extender",
        "subtitle": "HDMI over Cat (RX)",
        "tags": ["Video", "Extender"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "Cat5/6 In (RJ45)",
        ],
        "outputs": [
            "HDMI Out",
        ],
    },
    {
        "title": "HDMI Switch 3:1",
        "name": "Generic 3:1 HDMI Switch",
        "subtitle": "3-input HDMI Switch",
        "tags": ["Video", "Switcher"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "HDMI In 1",
            "HDMI In 2",
            "HDMI In 3",
        ],
        "outputs": [
            "HDMI Out",
        ],
    },
    {
        "title": "Pro Signal 4x4 4K",
        "name": "Pro Signal 4×4 4K HDMI 2.0",
        "subtitle": "HDMI Matrix Switch",
        "tags": ["Video", "Switcher", "Matrix"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "HDMI In 1",
            "HDMI In 2",
            "HDMI In 3",
            "HDMI In 4",
        ],
        "outputs": [
            "HDMI Out 1",
            "HDMI Out 2",
            "HDMI Out 3",
            "HDMI Out 4",
        ],
        "control": [
            "Network",
            "RS-232",
            "IR",
        ],
    },
    {
        "title": "Datapath FX4/H",
        "name": "Datapath FX4/H",
        "subtitle": "4-output Display Wall",
        "tags": ["Video", "Processor", "Display Wall"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "HDMI In 1",
            "HDMI In 2",
            "DP In",
        ],
        "outputs": [
            "HDMI Out 1",
            "HDMI Out 2",
            "HDMI Out 3",
            "HDMI Out 4",
        ],
        "control": [
            "Network",
            "RS-232",
            "USB",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "extenders.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
