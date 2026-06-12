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
    {
        "title": "SM7B",
        "name": "Shure SM7B",
        "subtitle": "Dynamic Studio Microphone",
        "tags": ["Audio", "Microphone"],
        "width": 160,
        "outputs": ["XLR Out"],
    },
    {
        "title": "ULX-D Quad RX",
        "name": "Shure ULXD4Q",
        "subtitle": "Quad Digital Receiver",
        "tags": ["Audio", "Wireless"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": ["Antenna A (BNC)", "Antenna B (BNC)"],
        "outputs": [
            "XLR Out 1",
            "XLR Out 2",
            "XLR Out 3",
            "XLR Out 4",
            "RF Cascade A (BNC)",
            "RF Cascade B (BNC)",
        ],
        "control": ["Dante/Ethernet Primary", "Dante/Ethernet Secondary"],
    },
    {
        "title": "ULX-D Beltpack",
        "name": "Shure ULXD1",
        "subtitle": "Digital Bodypack TX",
        "tags": ["Audio", "Wireless"],
        "width": 160,
        "inputs": ["Mic In (TA4)"],
        "outputs": ["RF Out"],
    },
    {
        "title": "ULX-D Handheld",
        "name": "Shure ULXD2",
        "subtitle": "Digital Handheld TX",
        "tags": ["Audio", "Wireless"],
        "width": 160,
        "outputs": ["RF Out"],
    },
    {
        "title": "Axient AD4D",
        "name": "Shure Axient AD4D",
        "subtitle": "Dual Digital Receiver",
        "tags": ["Audio", "Wireless"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": ["Antenna A (BNC)", "Antenna B (BNC)"],
        "outputs": [
            "XLR Out 1",
            "XLR Out 2",
            "1/4\" Out 1",
            "1/4\" Out 2",
            "AES3 Out",
            "RF Cascade C (BNC)",
            "RF Cascade D (BNC)",
        ],
        "control": [
            "Ethernet Ctrl 1",
            "Ethernet Ctrl 2",
            "Dante Primary",
            "Dante Secondary",
            "Word Clock In",
            "Word Clock Thru",
        ],
    },
    {
        "title": "Axient AD1",
        "name": "Shure Axient AD1",
        "subtitle": "Digital Bodypack TX",
        "tags": ["Audio", "Wireless"],
        "width": 160,
        "inputs": ["Mic In (TA4)"],
        "outputs": ["RF Out"],
    },
    {
        "title": "Axient AD2",
        "name": "Shure Axient AD2 / Beta 87",
        "subtitle": "Digital Handheld TX",
        "tags": ["Audio", "Wireless"],
        "width": 160,
        "outputs": ["RF Out"],
    },
    {
        "title": "UR4D+",
        "name": "Shure UR4D+",
        "subtitle": "UHF-R Dual Receiver",
        "tags": ["Audio", "Wireless"],
        "width": 170,
        "inputs": ["Antenna A (BNC)", "Antenna B (BNC)"],
        "outputs": [
            "XLR Out 1",
            "1/4\" Out 1",
            "XLR Out 2",
            "1/4\" Out 2",
            "RF A Out (BNC)",
            "RF B Out (BNC)",
        ],
        "control": ["Network", "USB"],
    },
    {
        "title": "UR4S+",
        "name": "Shure UR4S+",
        "subtitle": "UHF-R Single Receiver",
        "tags": ["Audio", "Wireless"],
        "width": 170,
        "inputs": ["Antenna A (BNC)", "Antenna B (BNC)"],
        "outputs": ["XLR Out", "1/4\" Out", "RF A Out (BNC)", "RF B Out (BNC)"],
        "control": ["Network", "USB"],
    },
    {
        "title": "UR1 Beltpack",
        "name": "Shure UR1",
        "subtitle": "UHF-R Bodypack TX",
        "tags": ["Audio", "Wireless"],
        "width": 160,
        "inputs": ["Mic In (TA4)"],
        "outputs": ["RF Out"],
    },
    {
        "title": "UR2 Handheld",
        "name": "Shure UR2 / Beta 87A",
        "subtitle": "UHF-R Handheld TX",
        "tags": ["Audio", "Wireless"],
        "width": 160,
        "outputs": ["RF Out"],
    },
    {
        "title": "UA845 Antenna DA",
        "name": "Shure UA845UWB",
        "subtitle": "Antenna Distribution",
        "tags": ["Audio", "Wireless"],
        "width": 170,
        "inputs": ["Antenna A In", "Antenna B In"],
        "outputs": [
            "A/B Out 1",
            "A/B Out 2",
            "A/B Out 3",
            "A/B Out 4",
            "Cascade A/B",
        ],
    },
    {
        "title": "UA874 Antenna",
        "name": "Shure UA874E",
        "subtitle": "Active Directional Antenna",
        "tags": ["Audio", "Wireless"],
        "width": 170,
        "outputs": ["RF Out (BNC)"],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "shure.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
