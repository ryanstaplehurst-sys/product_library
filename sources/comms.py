"""
comms.py — Production communications and cueing.

Devices:
    - GreenGo Switch 5         — comms hub
    - GreenGo Wired Beltpack
    - GreenGo Wireless Beltpack
    - GreenGo Active Antenna
    - GreenGo Headset
    - Motorola GP340           — two-way radio
    - Motorola Handheld Radio
    - 4-way EarTech Wireless Comms Kit
    - Interspace Cueing Toolbox
    - Interspace MicroCue3 Kit
    - Interspace MicroCue3 Clicker
    - Interspace Balance Box (USB)
    - Interspace PC Balance Box
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "GreenGo Switch 5",
        "name": "GreenGo Switch 5",
        "subtitle": "Comms Hub (5-port)",
        "tags": ["Comms", "Hub"],
        "width": 170,
        "loose_ports": ["IP:", "Mains In"],
        "inputs": [
            "Beltpack 1 (RJ45)",
            "Beltpack 2 (RJ45)",
            "Beltpack 3 (RJ45)",
            "Beltpack 4 (RJ45)",
            "Beltpack 5 (RJ45)",
        ],
        "control": [
            "Network",
            "AES67",
        ],
    },
    {
        "title": "GreenGo Wired Beltpack",
        "name": "GreenGo Wired Beltpack",
        "subtitle": "Comms Beltpack",
        "tags": ["Comms"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "Network In (RJ45)",
        ],
        "outputs": [
            "Headset (4-pin)",
            "Network Loop (RJ45)",
        ],
    },
    {
        "title": "GreenGo Wireless Beltpack",
        "name": "GreenGo Wireless Beltpack",
        "subtitle": "Wireless Comms Beltpack",
        "tags": ["Comms", "Wireless"],
        "width": 160,
        "info_row": True,
        "outputs": [
            "Headset (4-pin)",
        ],
    },
    {
        "title": "GreenGo Active Antenna",
        "name": "GreenGo Active Antenna",
        "subtitle": "Active Comms Antenna",
        "tags": ["Comms", "Wireless"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "RF Out (BNC)",
        ],
    },
    {
        "title": "GreenGo Headset",
        "name": "GreenGo Headset",
        "subtitle": "Comms Headset",
        "tags": ["Comms"],
        "width": 160,
        "info_row": True,
        "outputs": [
            "Connector (4-pin/XLR)",
        ],
    },
    {
        "title": "Motorola GP340",
        "name": "Motorola GP340",
        "subtitle": "Two-way Radio",
        "tags": ["Comms", "Radio"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Battery"],
        "outputs": [
            "Audio (3.5mm/Hirose)",
            "RF (Antenna)",
        ],
    },
    {
        "title": "Motorola Handheld",
        "name": "Motorola Handheld Radio",
        "subtitle": "Two-way Radio",
        "tags": ["Comms", "Radio"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Battery"],
        "outputs": [
            "Audio (3.5mm/Hirose)",
            "RF (Antenna)",
        ],
    },
    {
        "title": "EarTech 4-way",
        "name": "EarTech 4-way Wireless Comms",
        "subtitle": "4-way Wireless Comms Kit",
        "tags": ["Comms", "Wireless"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "outputs": [
            "Headset 1",
            "Headset 2",
            "Headset 3",
            "Headset 4",
            "Antenna",
        ],
    },
    {
        "title": "Cueing Toolbox",
        "name": "Interspace Cueing Toolbox",
        "subtitle": "Speaker Cueing Hub",
        "tags": ["Cueing", "Control"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Mic In (XLR)",
            "Aux In (3.5mm)",
        ],
        "outputs": [
            "PFL Out (3.5mm)",
            "Mix Out (XLR)",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "MicroCue3 Kit",
        "name": "Interspace MicroCue3 Kit",
        "subtitle": "Speaker Cueing Kit",
        "tags": ["Cueing", "Control"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "USB Out (PC link)",
        ],
        "control": [
            "RF Receiver",
        ],
    },
    {
        "title": "MicroCue3 Clicker",
        "name": "Interspace MicroCue3 Clicker",
        "subtitle": "Wireless Clicker",
        "tags": ["Cueing", "Control", "Wireless"],
        "width": 160,
        "info_row": True,
        "outputs": [
            "RF (to MicroCue RX)",
        ],
    },
    {
        "title": "Balance Box USB",
        "name": "Interspace Balance Box",
        "subtitle": "USB Audio Balance Box",
        "tags": ["Audio", "Balun"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "USB-B (PC)",
        ],
        "outputs": [
            "Mic Out L (XLR)",
            "Mic Out R (XLR)",
        ],
    },
    {
        "title": "PC Balance Box",
        "name": "Interspace PC Balance Box",
        "subtitle": "PC Line Balance Box",
        "tags": ["Audio", "Balun"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "PC Line In (3.5mm)",
        ],
        "outputs": [
            "Out L (XLR)",
            "Out R (XLR)",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "comms.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
