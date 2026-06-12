"""kramer.py — Kramer library specs."""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "VM-4H2 1:2",
        "name": "Kramer VM-4H2 1:2",
        "subtitle": "4K HDMI 1:2 DA",
        "tags": ["Video", "Distribution"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "HDMI In",
        ],
        "outputs": [
            "HDMI Out 1",
            "HDMI Out 2",
        ],
    },
    {
        "title": "VM-4H2 1:4",
        "name": "Kramer VM-4H2 1:4",
        "subtitle": "4K HDMI 1:4 DA",
        "tags": ["Video", "Distribution"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "HDMI In",
        ],
        "outputs": [
            "HDMI Out 1",
            "HDMI Out 2",
            "HDMI Out 3",
            "HDMI Out 4",
        ],
    },
    {
        "title": "HDMI Line RX",
        "name": "Kramer HDMI Line Receiver",
        "subtitle": "HDBaseT Receiver",
        "tags": ["Video", "Extender"],
        "width": 160,
        "inputs": ["HDBT In (Cat6)"],
        "outputs": ["HDMI Out"],
        "control": ["RS-232", "IR"],
    },
    {
        "title": "VIA Connect2",
        "name": "Kramer VIA Connect²",
        "subtitle": "Wireless Content Solution",
        "tags": ["Video", "Wireless"],
        "width": 170,
        "loose_ports": ["IP:", "WiFi Casting"],
        "outputs": ["HDMI Out"],
        "control": ["LAN", "USB"],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "kramer.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
