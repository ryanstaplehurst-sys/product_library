"""
touchscreens.py — IIYAMA Prolite touchscreen range.

Touchscreens have a USB return path for touch coordinates back to the host
PC. Modelled as: HDMI/DP inputs + USB out for touch.
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


def touchscreen(size_inches):
    return {
        "title": f"IIYAMA Touch {size_inches}\"",
        "name": f"IIYAMA Prolite {size_inches}\"",
        "subtitle": "Touchscreen Display",
        "tags": ["Video", "Display", "Touch"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "HDMI 1",
            "HDMI 2",
            "DisplayPort",
            "USB-C (DP-Alt)",
            "VGA",
        ],
        "outputs": [
            "Audio Out (3.5mm)",
        ],
        "control": [
            "Touch Out (USB-B)",
            "RS-232",
            "Network",
        ],
    }


DEVICES = [
    touchscreen(size) for size in ["15", "27", "32", "43", "49", "55", "65", "75"]
] + [
    {
        "title": "Touchscreen Remote",
        "name": "IIYAMA Prolite Touchscreen Remote",
        "subtitle": "IR Remote",
        "tags": ["Video", "Control"],
        "width": 160,
        "info_row": True,
        "outputs": [
            "IR (line-of-sight)",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "touchscreens.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
