"""
cameras.py — Cameras: mirrorless, camcorders, webcams, NDI sources.
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "Canon EOS R50",
        "name": "Canon EOS R50",
        "subtitle": "Mirrorless 4K Camera",
        "tags": ["Video", "Camera", "Source"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Battery"],
        "outputs": [
            "HDMI (mini)",
            "USB-C",
            "Mic In (3.5mm)",
            "Phones",
        ],
        "control": [
            "WiFi",
            "Bluetooth",
        ],
    },
    {
        "title": "Lumix GH6",
        "name": "Panasonic Lumix GH6",
        "subtitle": "Mirrorless 4K Camera",
        "tags": ["Video", "Camera", "Source"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Battery"],
        "outputs": [
            "HDMI (Type A)",
            "USB-C",
            "Mic In (3.5mm)",
            "Phones",
            "TC In/Out (3.5mm)",
        ],
        "control": [
            "WiFi",
            "Bluetooth",
        ],
    },
    {
        "title": "Sony PXW-Z150",
        "name": "Sony PXW-Z150",
        "subtitle": "4K Pro Camcorder",
        "tags": ["Video", "Camera", "Source"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Battery", "DC In"],
        "inputs": [
            "Mic 1 (XLR)",
            "Mic 2 (XLR)",
            "Genlock In",
        ],
        "outputs": [
            "SDI Out (3G)",
            "HDMI Out",
            "Phones",
        ],
        "control": [
            "Network",
            "USB",
            "Remote (LANC)",
        ],
    },
    {
        "title": "Logitech BRIO 4K",
        "name": "Logitech BRIO 4K",
        "subtitle": "USB Webcam",
        "tags": ["Video", "Camera", "Source"],
        "width": 160,
        "info_row": True,
        "outputs": [
            "USB-A",
        ],
    },
    {
        "title": "BirdDog Studio NDI",
        "name": "BirdDog Studio NDI",
        "subtitle": "NDI Camera/Encoder",
        "tags": ["Video", "Camera", "NDI", "Source"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "HDMI In",
            "SDI In",
        ],
        "outputs": [
            "HDMI Out",
            "SDI Out",
        ],
        "control": [
            "NDI / Network",
            "Tally",
            "USB",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "cameras.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
