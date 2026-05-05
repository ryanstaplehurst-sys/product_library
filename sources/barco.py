"""
barco.py — Barco screen management library specs.

Devices:
    - E2 4K           — Event Master E2 4K screen management system
    - S3 4K Gen 2     — ImagePRO/S3 4K screen management system, 2nd gen
    - PDS 4K          — Presentation Switcher 4K
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "E2 4K",
        "name": "Barco E2 4K",
        "subtitle": "Event Master 4K SMS",
        "tags": ["Video", "Switcher"],
        "width": 180,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "SDI 1 (12G)",
            "SDI 2 (12G)",
            "SDI 3 (12G)",
            "SDI 4 (12G)",
            "HDMI 1 (2.0)",
            "HDMI 2 (2.0)",
            "HDMI 3 (2.0)",
            "HDMI 4 (2.0)",
            "DP 1 (1.2)",
            "DP 2 (1.2)",
            "DVI 1",
            "DVI 2",
        ],
        "outputs": [
            "PGM 1 (HDMI)",
            "PGM 2 (HDMI)",
            "PGM 3 (HDMI)",
            "PGM 4 (HDMI)",
            "PVW 1",
            "PVW 2",
            "AUX 1",
            "AUX 2",
            "AUX 3",
            "AUX 4",
            "MV 1",
            "MV 2",
        ],
        "control": [
            "Network 1",
            "Network 2",
            "USB",
        ],
    },
    {
        "title": "S3 4K Gen 2",
        "name": "Barco S3 4K Gen 2",
        "subtitle": "Screen Management System",
        "tags": ["Video", "Switcher"],
        "width": 180,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "SDI 1 (12G)",
            "SDI 2 (12G)",
            "SDI 3 (12G)",
            "SDI 4 (12G)",
            "HDMI 1",
            "HDMI 2",
            "DP 1",
            "DP 2",
        ],
        "outputs": [
            "PGM 1 (HDMI)",
            "PGM 2 (HDMI)",
            "PVW",
            "AUX 1",
            "AUX 2",
            "MV",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "PDS 4K",
        "name": "Barco PDS 4K",
        "subtitle": "Presentation Switcher 4K",
        "tags": ["Video", "Switcher"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": [
            "SDI 1",
            "SDI 2",
            "HDMI 1",
            "HDMI 2",
            "HDMI 3",
            "HDMI 4",
            "DP",
            "DVI",
        ],
        "outputs": [
            "PGM (HDMI)",
            "PGM (DVI)",
            "PVW (HDMI)",
        ],
        "control": [
            "Network",
            "RS-232",
            "USB",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "barco.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
