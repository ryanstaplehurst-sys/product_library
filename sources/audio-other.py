"""
audio-other.py — Audio kit too small to deserve its own manufacturer library.

Devices:
    - QSC CP8                — 8" powered speaker
    - QSC GXD 4              — DSP amplifier
    - BSS AR133              — active DI box
    - Behringer UMC202HD     — 2-in/2-out USB audio interface
    - Behringer UMC404HD     — 4-in/4-out USB audio interface
    - Tascam DR-701D         — 6-track field recorder
    - Sonifex RB-DA6G        — 6-output stereo DA
    - Sonos AMP              — streaming amplifier
    - Sonos Era 100          — wireless streaming speaker
    - Sonos Move             — bluetooth speaker
    - Bose Smart Soundbar    — soundbar
    - LD MAUI 28 G2          — column PA system
    - LD MAUI 28 G2 W + Sub  — column + subwoofer combo
    - Lynx Pro QB-5          — passive 5" speaker
    - RED 505                — analogue line splitter
    - Pioneer DM-40D         — active monitor (each)
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "QSC CP8",
        "name": "QSC CP8",
        "subtitle": "8\" Powered Speaker",
        "tags": ["Audio", "Speaker"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Input 1 (XLR/TRS)",
            "Input 2 (RCA L)",
            "Input 3 (RCA R)",
        ],
        "outputs": [
            "Mix Out (XLR Thru)",
        ],
    },
    {
        "title": "QSC GXD 4",
        "name": "QSC GXD 4",
        "subtitle": "DSP Amplifier",
        "tags": ["Audio", "Amplifier"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Input A (XLR)",
            "Input B (XLR)",
        ],
        "outputs": [
            "Out A (NL4)",
            "Out B (NL4)",
        ],
        "control": [
            "USB",
            "Aux In/Out",
        ],
    },
    {
        "title": "BSS AR133",
        "name": "BSS AR133",
        "subtitle": "Active DI Box",
        "tags": ["Audio", "DI"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "Input (TS/TRS)",
        ],
        "outputs": [
            "Thru (TS)",
            "Out (XLR Mic-level)",
        ],
    },
    {
        "title": "UMC202HD",
        "name": "Behringer UMC202HD",
        "subtitle": "2×2 USB Audio Interface",
        "tags": ["Audio", "Interface"],
        "width": 170,
        "info_row": True,
        "inputs": [
            "Mic/Line 1 (XLR/TRS)",
            "Mic/Line 2 (XLR/TRS)",
        ],
        "outputs": [
            "Out L (TRS)",
            "Out R (TRS)",
            "Phones",
        ],
        "control": [
            "USB to Host",
        ],
    },
    {
        "title": "UMC404HD",
        "name": "Behringer UMC404HD",
        "subtitle": "4×4 USB Audio Interface",
        "tags": ["Audio", "Interface"],
        "width": 170,
        "info_row": True,
        "inputs": [
            "Mic/Line 1 (XLR/TRS)",
            "Mic/Line 2 (XLR/TRS)",
            "Mic/Line 3 (XLR/TRS)",
            "Mic/Line 4 (XLR/TRS)",
            "MIDI In",
        ],
        "outputs": [
            "Out 1 (TRS)",
            "Out 2 (TRS)",
            "Out 3 (TRS)",
            "Out 4 (TRS)",
            "Phones 1",
            "Phones 2",
            "MIDI Out",
        ],
        "control": [
            "USB to Host",
        ],
    },
    {
        "title": "DR-701D",
        "name": "Tascam DR-701D",
        "subtitle": "6-track Field Recorder",
        "tags": ["Audio", "Recorder"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "Mic/Line 1 (XLR)",
            "Mic/Line 2 (XLR)",
            "Mic/Line 3 (XLR)",
            "Mic/Line 4 (XLR)",
            "HDMI In (TC)",
            "Slate Mic",
        ],
        "outputs": [
            "Camera Out L (3.5mm)",
            "Camera Out R (3.5mm)",
            "HDMI Out (TC)",
            "Phones",
        ],
        "control": [
            "USB",
            "TC In/Out (BNC)",
        ],
    },
    {
        "title": "RB-DA6G",
        "name": "Sonifex RB-DA6G",
        "subtitle": "6-Output Stereo DA",
        "tags": ["Audio", "Distribution"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "In L (XLR)",
            "In R (XLR)",
        ],
        "outputs": [
            "Out 1 L/R",
            "Out 2 L/R",
            "Out 3 L/R",
            "Out 4 L/R",
            "Out 5 L/R",
            "Out 6 L/R",
        ],
    },
    {
        "title": "Sonos AMP",
        "name": "Sonos AMP",
        "subtitle": "Streaming Amp 2×125W",
        "tags": ["Audio", "Amplifier", "Streaming"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Line In L/R (RCA)",
            "HDMI ARC",
        ],
        "outputs": [
            "Speaker A (binding posts)",
            "Speaker B (binding posts)",
            "Sub Out (RCA)",
        ],
        "control": [
            "Network",
            "WiFi",
        ],
    },
    {
        "title": "Sonos Era 100",
        "name": "Sonos Era 100",
        "subtitle": "Wireless Streaming Speaker",
        "tags": ["Audio", "Speaker", "Streaming"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "Line In (USB-C/3.5mm adapter)",
        ],
        "control": [
            "WiFi",
            "Bluetooth",
        ],
    },
    {
        "title": "Sonos Move",
        "name": "Sonos Move",
        "subtitle": "Portable Bluetooth Speaker",
        "tags": ["Audio", "Speaker", "Streaming"],
        "width": 160,
        "info_row": True,
        "control": [
            "WiFi",
            "Bluetooth",
        ],
    },
    {
        "title": "Bose Soundbar",
        "name": "Bose Smart Soundbar",
        "subtitle": "Smart Soundbar",
        "tags": ["Audio", "Speaker"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "HDMI eARC",
            "Optical In",
            "Aux In (3.5mm)",
        ],
        "control": [
            "Network",
            "WiFi",
            "Bluetooth",
        ],
    },
    {
        "title": "MAUI 28 G2",
        "name": "LD MAUI 28 G2",
        "subtitle": "Column PA System",
        "tags": ["Audio", "Speaker"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Mic/Line 1 (XLR/TRS)",
            "Mic/Line 2 (XLR/TRS)",
            "Hi-Z 3 (TRS)",
            "Hi-Z 4 (TRS)",
            "Stereo In L/R (RCA)",
            "Bluetooth In",
        ],
        "outputs": [
            "Mix Out (XLR Thru)",
        ],
    },
    {
        "title": "MAUI 28 G2 W + Sub",
        "name": "LD MAUI 28 G2 W",
        "subtitle": "Column PA + Sub",
        "tags": ["Audio", "Speaker"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In (Sub)"],
        "inputs": [
            "Mic/Line 1 (XLR/TRS)",
            "Mic/Line 2 (XLR/TRS)",
            "Stereo In L/R (RCA)",
            "Bluetooth In",
        ],
        "outputs": [
            "Mix Out (XLR Thru)",
            "Column Out (TRS)",
        ],
    },
    {
        "title": "Lynx QB-5",
        "name": "Lynx Pro QB-5",
        "subtitle": "5\" Passive Speaker",
        "tags": ["Audio", "Speaker"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "Speaker In (NL4/binding posts)",
        ],
    },
    {
        "title": "RED 505",
        "name": "RED 505",
        "subtitle": "Analogue Line Splitter",
        "tags": ["Audio", "Distribution"],
        "width": 160,
        "info_row": True,
        "inputs": [
            "Line In (XLR)",
        ],
        "outputs": [
            "Out 1 (XLR)",
            "Out 2 (XLR)",
            "Out 3 (XLR)",
            "Out 4 (XLR)",
            "Out 5 (XLR)",
        ],
    },
    {
        "title": "DM-40D",
        "name": "Pioneer DM-40D",
        "subtitle": "Active Monitor (each)",
        "tags": ["Audio", "Speaker"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Input (XLR/TRS)",
            "RCA L/R",
            "Aux (3.5mm)",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "audio-other.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
