"""
playback.py — Media playback devices.
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "HD1024",
        "name": "BrightSign HD1024",
        "subtitle": "Entry Media Player",
        "tags": ["Video", "Playback"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "HDMI Out",
            "Audio Out (3.5mm)",
        ],
        "control": [
            "Network",
            "USB-A",
            "GPIO",
            "MicroSD",
        ],
    },
    {
        "title": "LS445",
        "name": "BrightSign LS445",
        "subtitle": "Mid Media Player",
        "tags": ["Video", "Playback"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "HDMI Out",
            "Audio Out (3.5mm)",
        ],
        "control": [
            "Network",
            "USB-A",
            "USB-C",
            "MicroSD",
        ],
    },
    {
        "title": "XT1144",
        "name": "BrightSign XT1144",
        "subtitle": "Pro Media Player",
        "tags": ["Video", "Playback"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "HDMI In",
        ],
        "outputs": [
            "HDMI Out",
            "Audio Out (3.5mm)",
        ],
        "control": [
            "Network 1G",
            "USB-A 1",
            "USB-A 2",
            "USB-C",
            "GPIO",
            "MicroSD (SDHC)",
            "RS-232",
        ],
    },
    {
        "title": "Apple TV",
        "name": "Apple TV",
        "subtitle": "Streaming Media Player",
        "tags": ["Video", "Playback"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "outputs": [
            "HDMI Out",
        ],
        "control": [
            "Network",
            "WiFi",
        ],
    },
    {
        "title": "Pro-Signal 4K MP",
        "name": "Pro-Signal 4K Media Player",
        "subtitle": "4K Media Player",
        "tags": ["Video", "Playback"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "HDMI Out",
            "Audio Out (3.5mm)",
        ],
        "control": [
            "Network",
            "USB-A",
            "MicroSD",
            "IR Remote",
        ],
    },
    {
        "title": "Sprite MP",
        "name": "Sprite Media Player",
        "subtitle": "Media Player",
        "tags": ["Video", "Playback"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "HDMI Out",
        ],
        "control": [
            "Network",
            "USB-A",
            "IR Remote",
        ],
    },
    {
        "title": "Mac Studio",
        "name": "Apple Mac Studio (M3 Ultra)",
        "subtitle": "Media Rack Workstation",
        "tags": ["Video", "Playback", "Computer"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "outputs": [
            "HDMI Out",
            "TB4 / DP 1",
            "TB4 / DP 2",
            "TB4 / DP 3",
            "TB4 / DP 4",
            "USB-C 5",
            "USB-C 6",
            "Audio Out (3.5mm)",
        ],
        "control": [
            "10G Ethernet",
            "USB-A 1",
            "USB-A 2",
            "WiFi",
            "Bluetooth",
        ],
    },
    {
        "title": "Workstation HE",
        "name": "Workstation - High End",
        "subtitle": "vMix / Pixera / Coolux PC",
        "tags": ["Video", "Playback", "Computer"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Capture Card In 1 (HDMI/SDI)",
            "Capture Card In 2 (HDMI/SDI)",
        ],
        "outputs": [
            "DP 1",
            "DP 2",
            "DP 3",
            "HDMI",
            "Audio Out",
        ],
        "control": [
            "Ethernet",
            "USB-A",
            "USB-C",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "playback.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
