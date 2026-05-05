"""elgato.py — Elgato Streamdeck and capture products."""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "Streamdeck Mini",
        "name": "Elgato Streamdeck Mini",
        "subtitle": "6-key USB Control Surface",
        "tags": ["Control"],
        "width": 160,
        "info_row": True,
        "outputs": [
            "USB-A (PC)",
        ],
    },
    {
        "title": "Streamdeck XL",
        "name": "Elgato Streamdeck XL",
        "subtitle": "32-key USB Control Surface",
        "tags": ["Control"],
        "width": 160,
        "info_row": True,
        "outputs": [
            "USB-C (PC)",
        ],
    },
    {
        "title": "HD60 Pro Capture",
        "name": "Elgato HD60 Pro",
        "subtitle": "1080p60 Game Capture",
        "tags": ["Video", "Capture"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "HDMI In",
        ],
        "outputs": [
            "HDMI Out (passthrough)",
            "USB-C (PC)",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "elgato.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
