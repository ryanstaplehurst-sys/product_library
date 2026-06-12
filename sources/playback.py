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
    {
        "title": "Cyclone 4K",
        "name": "Cyclone 4K Media Player",
        "subtitle": "Media Player",
        "tags": ["Video", "Playback"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "HDMI Out",
            "Audio Out (3.5mm)",
        ],
        "control": [
            "USB-A",
            "SD Card",
            "IR Remote",
        ],
    },
    {
        "title": "HD224",
        "name": "BrightSign HD224",
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
            "MicroSD",
        ],
    },
    {
        "title": "ScreenBeam 1100+",
        "name": "ScreenBeam 1100 Plus",
        "subtitle": "Wireless Presentation RX",
        "tags": ["Video", "Wireless"],
        "width": 180,
        "loose_ports": ["IP:", "Miracast / AirPlay / Cast"],
        "outputs": ["HDMI Out"],
        "control": ["LAN 1", "LAN 2"],
    },
    {
        "title": "APC Mini",
        "name": "Akai APC Mini",
        "subtitle": "MIDI Control Surface",
        "tags": ["Control", "MIDI"],
        "width": 160,
        "control": ["USB-B (MIDI)"],
    },
    {
        "title": "PlaybackPro Kit",
        "name": "DT Videolabs PlaybackPro Kit",
        "subtitle": "Mac Playback System",
        "tags": ["Video", "Playback"],
        "width": 180,
        "loose_ports": ["IP:"],
        "outputs": [
            "Program Out (HDMI/SDI)",
            "Audio Out",
        ],
        "control": ["Network", "USB"],
    },
    {
        "title": "QLab Rack",
        "name": "QLab Playback Rack",
        "subtitle": "Mac Audio/Video Playback",
        "tags": ["Audio", "Playback"],
        "width": 180,
        "loose_ports": ["IP:"],
        "outputs": [
            "Audio Out 1-8",
            "Video Out (HDMI)",
        ],
        "control": ["Network", "MIDI", "USB"],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "playback.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
