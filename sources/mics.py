"""
mics.py — Generic and other-vendor wired mic library.

Devices:
    - DPA 6066 Core Omni Headset (beige & black)
    - Rode NTG2 shotgun
    - Generic Lapel Mic       — wildcard for unbranded lavs
    - Bluetooth DJI Lapel
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


def mic(title, name, subtitle, conn="3.5mm"):
    return {
        "title": title,
        "name": name,
        "subtitle": subtitle,
        "tags": ["Audio", "Mic"],
        "width": 160,
        "info_row": True,
        "outputs": [f"Mic Out ({conn})"],
    }


DEVICES = [
    mic("DPA 6066 (beige)", "DPA 6066 Core", "Omni Headset (beige)"),
    mic("DPA 6066 (black)", "DPA 6066 Core", "Omni Headset (black)"),
    mic("Rode NTG2", "Rode NTG2", "Shotgun (XLR)", conn="XLR"),
    mic("Lapel Mic", "Lapel Mic", "Generic"),
    mic("DJI Lapel BT", "DJI Bluetooth Lapel", "Wireless Bluetooth Mic", conn="BT"),
]


if __name__ == "__main__":
    out = REPO / "libraries" / "mics.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
