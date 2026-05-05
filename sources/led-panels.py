"""
led-panels.py — LED panel library.

Each panel is a sink with one DATA in and one DATA loop-through. Power is
real per-panel but typically not drawn at the panel level (it's at the
processor / distro level instead).

Devices:
    - Absen PL2.5 V2 (batch 11)         — workhorse 2.5mm
    - Absen PL2.5 V10 (batch 7)
    - Absen 2.5mm Polaris               — outdoor variant
    - Absen PL2.5 V2 corner panels       — left + right
    - Aluvision HiLED55+                 — fully integrated cabinet
    - BeMatrix LedSkin Wall              — 2.5mm bezel-less
    - LedSkin 1.9mm panel
    - LedSkin 2.5mm panel
    - Unilumin UPad IV XS                — 1.9mm
    - 3.9mm 500×500 (generic)            — outdoor 500×500 cabinet
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


def panel(title, name, subtitle, has_loop=True):
    d = {
        "title": title,
        "name": name,
        "subtitle": subtitle,
        "tags": ["LED", "Panel"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": ["DATA In (RJ45)"],
    }
    if has_loop:
        d["outputs"] = ["DATA Loop (RJ45)"]
    return d


DEVICES = [
    panel("Absen PL2.5 V2 b11", "Absen PL2.5 V2 Batch 11", "2.5mm Indoor"),
    panel("Absen PL2.5 V2 b11 L-corner", "Absen PL2.5 V2 Batch 11", "2.5mm Left Corner"),
    panel("Absen PL2.5 V2 b11 R-corner", "Absen PL2.5 V2 Batch 11", "2.5mm Right Corner"),
    panel("Absen PL2.5 V10 b7", "Absen PL2.5 V10 Batch 7", "2.5mm Indoor"),
    panel("Absen 2.5 Polaris", "Absen 2.5mm Polaris", "2.5mm Outdoor"),
    panel("Aluvision HiLED55+", "Aluvision HiLED55+", "Integrated Cabinet"),
    panel("BeMatrix LedSkin", "BeMatrix LedSkin Wall", "2.5mm Bezel-less"),
    panel("LedSkin 1.9mm", "LedSkin 1.9mm Panel", "1.9mm"),
    panel("LedSkin 2.5mm", "LedSkin 2.5mm Panel", "2.5mm"),
    panel("Unilumin UPad IV XS", "Unilumin UPad IV XS", "1.9mm"),
    panel("3.9mm 500x500", "3.9mm 500×500 Panel", "Outdoor Cabinet"),
]


if __name__ == "__main__":
    out = REPO / "libraries" / "led-panels.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
