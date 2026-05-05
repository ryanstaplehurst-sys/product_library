"""
allen-heath.py — Allen & Heath audio library specs.

Run: python3 sources/allen-heath.py

Devices:
    - SQ5           — 48-channel digital mixing console
    - CQ-12T        — compact digital console with touchscreen
    - DX168         — 16-in / 8-out DX-protocol stagebox
    - Zedi 10       — analogue mixer with USB
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "SQ5",
        "name": "Allen & Heath SQ5",
        "subtitle": "48-ch Digital Console",
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
            "AES In",
            "Word Clock In",
        ],
        "outputs": [
            "Output 1 (XLR)",
            "Output 2 (XLR)",
            "Output 3 (XLR)",
            "Output 4 (XLR)",
            "Output 5 (XLR)",
            "Output 6 (XLR)",
            "Output 7 (XLR)",
            "Output 8 (XLR)",
            "AES Out",
            "Phones 1",
            "Phones 2",
        ],
        "control": [
            "DX Link 1",
            "DX Link 2",
            "SLink (96k AES50)",
            "Option Card Slot",
            "Network",
            "USB-A",
            "USB-B",
            "MIDI",
            "Footswitch",
        ],
    },
    {
        "title": "CQ-12T",
        "name": "Allen & Heath CQ-12T",
        "subtitle": "Compact Digital Console",
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
            "Stereo In L (TRS)",
            "Stereo In R (TRS)",
        ],
        "outputs": [
            "Output 1 (XLR)",
            "Output 2 (XLR)",
            "Output 3 (XLR)",
            "Output 4 (XLR)",
            "Stereo Out L (TRS)",
            "Stereo Out R (TRS)",
            "Phones",
        ],
        "control": [
            "SLink",
            "Network",
            "USB-A",
            "Bluetooth",
        ],
    },
    {
        "title": "DX168",
        "name": "Allen & Heath DX168",
        "subtitle": "16-in / 8-out Stagebox",
        "tags": ["Audio", "Stagebox"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
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
        ],
        "outputs": [
            "Output 1",
            "Output 2",
            "Output 3",
            "Output 4",
            "Output 5",
            "Output 6",
            "Output 7",
            "Output 8",
        ],
        "control": [
            "DX In",
            "DX Out",
        ],
    },
    {
        "title": "Zedi 10",
        "name": "Allen & Heath Zedi 10",
        "subtitle": "Analogue Mixer + USB",
        "tags": ["Audio", "Console"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Mic/Line 1",
            "Mic/Line 2",
            "Mic/Line 3 (Mono/Stereo)",
            "Mic/Line 4 (Mono/Stereo)",
            "St 5/6 (RCA)",
            "St 7/8 (RCA)",
        ],
        "outputs": [
            "Main Out L (XLR)",
            "Main Out R (XLR)",
            "Aux 1 Out",
            "Aux 2 Out",
            "Phones",
        ],
        "control": [
            "USB",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "allen-heath.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
