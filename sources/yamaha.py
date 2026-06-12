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
            "Talkback In",
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
            "MY Slot 1",
            "MY Slot 2",
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
            "Mic/Line 13 (Combo)",
            "Mic/Line 14 (Combo)",
            "Mic/Line 15 (Combo)",
            "Mic/Line 16 (Combo)",
        ],
        "outputs": [
            "Omni Out 1 (XLR)",
            "Omni Out 2 (XLR)",
            "Omni Out 3 (XLR)",
            "Omni Out 4 (XLR)",
            "Omni Out 5 (XLR)",
            "Omni Out 6 (XLR)",
            "Omni Out 7 (XLR)",
            "Omni Out 8 (XLR)",
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
    {
        "title": "CL5",
        "name": "Yamaha CL5",
        "subtitle": "72-ch Digital Console",
        "tags": ["Audio", "Console"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": [
            "Omni In 1-8",
            "Talkback In",
            "Dante In (64ch)",
            "Word Clock In",
        ],
        "outputs": [
            "Omni Out 1-8",
            "Dante Out (64ch)",
            "AES/EBU Out",
            "Word Clock Out",
        ],
        "control": ["Dante Primary", "Dante Secondary", "MY Slot 1-3", "Network", "MIDI / GPI"],
    },
    {
        "title": "QL5",
        "name": "Yamaha QL5",
        "subtitle": "64-ch Digital Console",
        "tags": ["Audio", "Console"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": [
            "Omni In 1-32",
            "Talkback In",
            "Dante In (64ch)",
            "Word Clock In",
        ],
        "outputs": [
            "Omni Out 1-16",
            "Dante Out (64ch)",
            "AES/EBU Out",
            "Word Clock Out",
        ],
        "control": ["Dante Primary", "Dante Secondary", "MY Slot 1-2", "Network", "MIDI / GPI"],
    },
    {
        "title": "LS9-32",
        "name": "Yamaha LS9-32",
        "subtitle": "32-ch Digital Console",
        "tags": ["Audio", "Console"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": [
            "Omni In 1-32",
            "2TR In",
            "Word Clock In",
        ],
        "outputs": [
            "Omni Out 1-16",
            "2TR Out",
        ],
        "control": ["MY Slot 1", "MY Slot 2", "Network", "MIDI"],
    },
    {
        "title": "M7CL",
        "name": "Yamaha M7CL",
        "subtitle": "32/48-ch Digital Console",
        "tags": ["Audio", "Console"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": [
            "Input 1-32 (48)",
            "ST In 1-4 (XLR pairs)",
            "Word Clock In",
        ],
        "outputs": [
            "Omni Out 1-16",
            "2TR Out Digital",
        ],
        "control": ["MY Slot 1", "MY Slot 2", "MY Slot 3", "Network", "MIDI"],
    },
    {
        "title": "RIO1608-D",
        "name": "Yamaha RIO1608-D",
        "subtitle": "Dante Stagebox 16/8",
        "tags": ["Audio", "Stagebox"],
        "width": 170,
        "loose_ports": ["IP:"],
        "inputs": [
            "Mic/Line 1-16",
        ],
        "outputs": [
            "Line Out 1-8",
        ],
        "control": ["Dante Primary", "Dante Secondary"],
    },
    {
        "title": "RIO3224-D",
        "name": "Yamaha RIO3224-D",
        "subtitle": "Dante Stagebox 32/24",
        "tags": ["Audio", "Stagebox"],
        "width": 170,
        "loose_ports": ["IP:"],
        "inputs": [
            "Mic/Line 1-32",
        ],
        "outputs": [
            "Line Out 1-16",
            "AES/EBU Out 1-4 (8ch)",
        ],
        "control": ["Dante Primary", "Dante Secondary"],
    },
    {
        "title": "DM7C",
        "name": "Yamaha DM7 Compact",
        "subtitle": "72-ch Dante Console (on order)",
        "tags": ["Audio", "Console", "On Order"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": [
            "Omni In 1-16",
            "TC In (XLR)",
            "Dante In (144ch)",
            "Word Clock In",
        ],
        "outputs": [
            "Omni Out 1-16",
            "Dante Out (144ch)",
            "AES/EBU Out",
            "Word Clock Out",
        ],
        "control": [
            "Dante Primary",
            "Dante Secondary",
            "PY Slot",
            "Network",
            "USB-C to Host",
            "GPI 5/5",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "yamaha.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
