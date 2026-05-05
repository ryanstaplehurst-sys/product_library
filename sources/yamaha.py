"""
yamaha.py — Yamaha audio library specs.

Run: python3 sources/yamaha.py

Devices:
    - QL1           — 32-channel digital mixing console (Dante)
    - DM3           — compact digital mixing console (Dante optional)
    - DXR12         — 12" active PA speaker
    - MSP3          — compact powered monitor speaker
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "QL1",
        "name": "Yamaha QL1",
        "subtitle": "32-ch Digital Console",
        "tags": ["Audio", "Console"],
        "width": 170,
        "loose_ports": ["IP:"],
        "inputs": [
            "Mic/Line 1",
            "Mic/Line 2",
            "Mic/Line 3",
            "Mic/Line 4",
            "Mic/Line 5",
            "Mic/Line 6",
            "Mic/Line 7",
            "Mic/Line 8",
            "Mic/Line 9",
            "Mic/Line 10",
            "Mic/Line 11",
            "Mic/Line 12",
            "Mic/Line 13",
            "Mic/Line 14",
            "Mic/Line 15",
            "Mic/Line 16",
            "AES/EBU In",
            "Word Clock In",
        ],
        "outputs": [
            "Omni Out 1",
            "Omni Out 2",
            "Omni Out 3",
            "Omni Out 4",
            "Omni Out 5",
            "Omni Out 6",
            "Omni Out 7",
            "Omni Out 8",
            "AES/EBU Out",
            "Phones",
            "Word Clock Out",
        ],
        "control": [
            "Dante Primary",
            "Dante Secondary",
            "Network",
            "USB-MIDI",
            "USB to Host",
        ],
    },
    {
        "title": "DM3",
        "name": "Yamaha DM3",
        "subtitle": "16-ch Digital Console",
        "tags": ["Audio", "Console"],
        "width": 170,
        "loose_ports": ["IP:"],
        "inputs": [
            "Mic/Line 1",
            "Mic/Line 2",
            "Mic/Line 3",
            "Mic/Line 4",
            "Mic/Line 5",
            "Mic/Line 6",
            "Mic/Line 7",
            "Mic/Line 8",
            "Mic/Line 9",
            "Mic/Line 10",
            "Mic/Line 11",
            "Mic/Line 12",
            "St In L (RCA)",
            "St In R (RCA)",
        ],
        "outputs": [
            "Output 1 (XLR)",
            "Output 2 (XLR)",
            "Output 3 (TRS)",
            "Output 4 (TRS)",
            "Output 5 (TRS)",
            "Output 6 (TRS)",
            "St Out L (RCA)",
            "St Out R (RCA)",
            "Phones",
        ],
        "control": [
            "Dante Primary",
            "Dante Secondary",
            "Network",
            "USB to Host",
        ],
    },
    {
        "title": "DXR12",
        "name": "Yamaha DXR12",
        "subtitle": "12\" Active PA Speaker",
        "tags": ["Audio", "Speaker"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Input 1 (XLR/TRS)",
            "Input 2 (XLR/TRS)",
        ],
        "outputs": [
            "Mix Out (XLR Thru)",
        ],
    },
    {
        "title": "MSP3",
        "name": "Yamaha MSP3",
        "subtitle": "Powered Monitor (each)",
        "tags": ["Audio", "Speaker"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Input 1 (XLR/TRS)",
            "Input 2 (RCA)",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "yamaha.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
