"""
projectors.py — Projector library specs.

Port layouts verified against Epson/Panasonic spec sheets, June 2026:
    - Epson EB-PU2010B   — HDMI/DVI-D/SDI(+loop)/VGA/HDBaseT
    - Panasonic PT-MZ770 — HDMI x2/RGB BNC/VGA/DIGITAL LINK (no DVI)
    - Panasonic PT-RZ970 — HDMI/DVI-D/SDI/VGA/DIGITAL LINK
    - Panasonic PT-RZ120 — HDMI/DVI-D/VGA/DIGITAL LINK (no SDI in family
      except RZ970)
    - Panasonic PT-RZ12K — HDMI/DVI-D/SDI x2/VGA/DIGITAL LINK
    - Panasonic PT-RZ21K — HDMI/DVI-D/SDI x2 only (DIGITAL LINK is an
      optional board; no VGA)
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


def projector(title, name, subtitle, inputs, outputs=None, control=None):
    return {
        "title": title,
        "name": name,
        "subtitle": subtitle,
        "tags": ["Video", "Projector"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["IP:"],
        "inputs": inputs,
        "outputs": outputs or [],
        "control": control or ["LAN", "RS-232", "Remote In"],
    }


DEVICES = [
    projector(
        "Epson PU2010B", "Epson EB-PU2010B", "10K Lumen Laser",
        ["HDMI In", "DVI-D In", "SDI In (3G)", "Computer (VGA)", "HDBaseT"],
        outputs=["SDI Out (Loop)"],
        control=["LAN", "RS-232", "USB"],
    ),
    projector(
        "PT-MZ770", "Panasonic PT-MZ770", "8K Lumen LCD Laser",
        ["HDMI 1 In", "HDMI 2 In", "RGB 1 In (BNC)", "Computer (VGA)",
         "DIGITAL LINK (HDBT)"],
    ),
    projector(
        "PT-RZ970", "Panasonic PT-RZ970", "10K Lumen DLP Laser",
        ["HDMI In", "DVI-D In", "SDI In", "RGB 1 In (BNC)", "Computer (VGA)",
         "DIGITAL LINK (HDBT)"],
    ),
    projector(
        "PT-RZ120", "Panasonic PT-RZ120", "12.5K Lumen DLP Laser",
        ["HDMI In", "DVI-D In", "Computer (VGA)", "DIGITAL LINK (HDBT)"],
    ),
    projector(
        "PT-RZ12K", "Panasonic PT-RZ12KEJ", "12K Lumen 3-Chip DLP",
        ["HDMI In", "DVI-D In", "SDI In 1", "SDI In 2", "Computer (VGA)",
         "DIGITAL LINK (HDBT)"],
    ),
    projector(
        "PT-RZ21K", "Panasonic PT-RZ21K", "21K Lumen 3-Chip DLP",
        ["HDMI In", "DVI-D In", "SDI In 1", "SDI In 2",
         "DIGITAL LINK (optional board)"],
        control=["LAN", "RS-232 In/Out", "Remote 1 In/Out", "Remote 2"],
    ),
]


if __name__ == "__main__":
    out = REPO / "libraries" / "projectors.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
