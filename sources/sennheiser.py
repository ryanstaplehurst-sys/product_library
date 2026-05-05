"""
sennheiser.py — Sennheiser library specs.

Run: python3 sources/sennheiser.py

Devices:
    - EW-DX EM 4 Dante      — 4-channel digital wireless receiver
    - EW-DX EM 4 Dante 8-way — 2× EM 4 in 19" rack (8 channels)
    - EW-D AS Active Splitter — active antenna splitter
    - ADP-UHF Passive Aerial  — passive directional antenna
    - EM 300-500 G4 Receiver  — analogue 2-ch receiver
    - EW-DX SK Beltpack       — wireless beltpack TX
    - EW-DX SKM Handheld      — wireless handheld TX
    - SK 500 G4 Beltpack      — analogue beltpack TX
    - ew300 G3 Handheld TX
    - ew300 G3 IEM RX         — in-ear monitor receiver (worn)
    - ew300 G3 IEM TX         — in-ear monitor transmitter
    - MAT 153-S               — gooseneck conference mic + base
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "EW-DX EM 4 Dante",
        "name": "Sennheiser EW-DX EM 4",
        "subtitle": "4-ch Wireless RX (Dante)",
        "tags": ["Audio", "Wireless", "Receiver"],
        "width": 180,
        "loose_ports": ["IP:", "Mains In"],
        "inputs": [
            "Antenna A (RF)",
            "Antenna B (RF)",
            "Booster DC Out",
        ],
        "outputs": [
            "Audio Out 1 (XLR)",
            "Audio Out 2 (XLR)",
            "Audio Out 3 (XLR)",
            "Audio Out 4 (XLR)",
        ],
        "control": [
            "Dante Primary",
            "Dante Secondary",
            "Network",
            "AES3 Out",
        ],
    },
    {
        "title": "EW-DX EM 4 Dante 8-way",
        "name": "Sennheiser EW-DX EM 4",
        "subtitle": "8-ch Rack (2× EM 4)",
        "tags": ["Audio", "Wireless", "Receiver"],
        "width": 180,
        "loose_ports": ["IP:", "Mains In"],
        "inputs": [
            "Antenna A (RF)",
            "Antenna B (RF)",
        ],
        "outputs": [
            "Audio Out 1 (XLR)",
            "Audio Out 2 (XLR)",
            "Audio Out 3 (XLR)",
            "Audio Out 4 (XLR)",
            "Audio Out 5 (XLR)",
            "Audio Out 6 (XLR)",
            "Audio Out 7 (XLR)",
            "Audio Out 8 (XLR)",
        ],
        "control": [
            "Dante Primary",
            "Dante Secondary",
            "Network",
        ],
    },
    {
        "title": "EW-D AS Active Splitter",
        "name": "Sennheiser EW-D AS",
        "subtitle": "Active Antenna Splitter",
        "tags": ["Audio", "Wireless", "Distribution"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Antenna A In (RF)",
            "Antenna B In (RF)",
        ],
        "outputs": [
            "RX 1 A",
            "RX 1 B",
            "RX 2 A",
            "RX 2 B",
            "RX 3 A",
            "RX 3 B",
            "RX 4 A",
            "RX 4 B",
        ],
    },
    {
        "title": "ADP-UHF Aerial",
        "name": "Sennheiser ADP-UHF",
        "subtitle": "Passive Directional Antenna",
        "tags": ["Audio", "Wireless", "Antenna"],
        "width": 160,
        "info_row": True,
        "outputs": [
            "RF Out (BNC)",
        ],
    },
    {
        "title": "EM 300-500 G4",
        "name": "Sennheiser EM 300-500 G4",
        "subtitle": "Analogue Wireless RX",
        "tags": ["Audio", "Wireless", "Receiver"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Antenna A (BNC)",
            "Antenna B (BNC)",
        ],
        "outputs": [
            "Audio Out (XLR)",
            "Audio Out (TRS)",
            "Loop Out (BNC)",
        ],
    },
    {
        "title": "EW-DX SK Beltpack",
        "name": "Sennheiser EW-DX SK",
        "subtitle": "Digital Wireless Beltpack TX",
        "tags": ["Audio", "Wireless", "Transmitter"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "Mic In (3.5mm)",
        ],
        "outputs": [
            "RF Out (Antenna)",
        ],
    },
    {
        "title": "EW-DX SKM Handheld",
        "name": "Sennheiser EW-DX SKM",
        "subtitle": "Digital Wireless Handheld TX",
        "tags": ["Audio", "Wireless", "Transmitter"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "Capsule (built-in)",
        ],
        "outputs": [
            "RF Out (Antenna)",
        ],
    },
    {
        "title": "SK 500 G4",
        "name": "Sennheiser SK 500 G4",
        "subtitle": "Analogue Beltpack TX",
        "tags": ["Audio", "Wireless", "Transmitter"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "Mic In (3.5mm)",
        ],
        "outputs": [
            "RF Out (Antenna)",
        ],
    },
    {
        "title": "ew300 G3 Handheld",
        "name": "Sennheiser ew300 G3",
        "subtitle": "Handheld TX",
        "tags": ["Audio", "Wireless", "Transmitter"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "Capsule (built-in)",
        ],
        "outputs": [
            "RF Out (Antenna)",
        ],
    },
    {
        "title": "ew300 G3 IEM RX",
        "name": "Sennheiser ew300 G3 IEM",
        "subtitle": "In-Ear Receiver (worn)",
        "tags": ["Audio", "Wireless", "Receiver"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "RF In (Antenna)",
        ],
        "outputs": [
            "Phones (3.5mm)",
        ],
    },
    {
        "title": "ew300 G3 IEM TX",
        "name": "Sennheiser ew300 G3 IEM",
        "subtitle": "In-Ear Transmitter",
        "tags": ["Audio", "Wireless", "Transmitter"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Audio In L (TRS)",
            "Audio In R (TRS)",
            "Loop In",
        ],
        "outputs": [
            "RF Out (BNC)",
            "Loop Out",
        ],
    },
    {
        "title": "MAT 153-S",
        "name": "Sennheiser MAT 153-S",
        "subtitle": "Gooseneck Mic + Base",
        "tags": ["Audio", "Mic"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "outputs": [
            "Mic Out (XLR)",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "sennheiser.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
