"""
projectors.py — Projector library specs.

Run from the repo root:
    python3 sources/projectors.py
which writes libraries/projectors.xml.

Devices included (June 2026 stock sync):
    - Epson EB-PU2010B          — 10K lumen laser
    - Panasonic PT-MZ770        — 8K lumen LCD laser
    - Panasonic PT-RZ970        — 10K lumen DLP laser
    - Panasonic PT-RZ120        — 12.5K lumen DLP laser
    - Panasonic PT-RZ12KEJ      — 12K lumen 3-chip DLP laser
    - Panasonic PT-RZ21K        — 21K lumen 3-chip DLP laser
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


def projector(title, name, subtitle, sdi=0, digital_link=True):
    inputs = ["HDMI In", "DVI-D In"]
    inputs += [f"SDI In {i}" if sdi > 1 else "SDI In" for i in range(1, sdi + 1)]
    inputs += ["Computer (VGA)"]
    if digital_link:
        inputs += ["DIGITAL LINK (HDBT)"]
    return {
        "title": title,
        "name": name,
        "subtitle": subtitle,
        "tags": ["Video", "Projector"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["IP:"],
        "inputs": inputs,
        "control": ["LAN", "RS-232", "Remote In"],
    }


DEVICES = [
    projector("Epson PU2010B", "Epson EB-PU2010B", "10K Lumen Laser"),
    projector("PT-MZ770", "Panasonic PT-MZ770", "8K Lumen LCD Laser"),
    projector("PT-RZ970", "Panasonic PT-RZ970", "10K Lumen DLP Laser", sdi=1),
    projector("PT-RZ120", "Panasonic PT-RZ120", "12.5K Lumen DLP Laser", sdi=1),
    projector("PT-RZ12K", "Panasonic PT-RZ12KEJ", "12K Lumen 3-Chip DLP", sdi=2),
    projector("PT-RZ21K", "Panasonic PT-RZ21K", "21K Lumen 3-Chip DLP", sdi=2),
]


if __name__ == "__main__":
    out = REPO / "libraries" / "projectors.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
