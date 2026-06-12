"""
barco.py — Barco screen management library specs.

Devices (port layouts verified against Barco spec sheets, June 2026):
    - E2 4K (Gen 2)    — Event Master screen management system
    - S3 4K Gen 2      — Tri-combo configuration
    - PDS 4K           — Presentation switcher (HDMI + 12G-SDI variant)
    - E2 Jr 4K         — stock 16-in / 8-out + 2 MV configuration
    - EC-30, EC-50     — Event Master controllers
    - PDS902           — legacy DVI/VGA/SDI presentation switcher
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "E2 4K",
        "name": "Barco E2 Gen 2",
        "subtitle": "Event Master 4K SMS",
        "tags": ["Video", "Switcher"],
        "width": 190,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "SDI In 1-16 (12G)",
            "HDMI In 1-12 (2.0)",
            "DP In 1-12 (1.2)",
        ],
        "outputs": [
            "SDI Out 1-4 (12G)",
            "HDMI Out 1-12 (2.0)",
            "DP Out (1.2)",
            "Multiview 1-4 (HDMI)",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "S3 4K Gen 2",
        "name": "Barco S3-4K Gen 2",
        "subtitle": "Tri-combo SMS",
        "tags": ["Video", "Switcher"],
        "width": 190,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "SDI In 1-4 (12G)",
            "HDMI In 1-5 (2.0)",
            "DP In 1-5 (1.2)",
        ],
        "outputs": [
            "SDI Out 1-4 (12G)",
            "HDMI Out 1-8 (2.0)",
            "Multiview 1-4 (HDMI)",
        ],
        "control": [
            "Network",
        ],
    },
    {
        "title": "PDS 4K",
        "name": "Barco PDS-4K",
        "subtitle": "Presentation Switcher 4K",
        "tags": ["Video", "Switcher"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": [
            "HDMI In 1-6 (2.0)",
            "SDI In 1-2 (12G, SDI variant)",
        ],
        "outputs": [
            "PGM Out 1-4 (HDMI 2.0)",
            "SDI Out 1-2 (12G, SDI variant)",
            "Multiview (HDMI UHD)",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "E2 Jr",
        "name": "Barco E2 Jr 4K",
        "subtitle": "Screen Management System",
        "tags": ["Video", "Switcher"],
        "width": 190,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "Input 1-16 (SDI/HDMI/DP)",
        ],
        "outputs": [
            "Output 1-8 (SDI/HDMI)",
            "Multiview 1-2 (HDMI)",
        ],
        "control": ["Network"],
    },
    {
        "title": "EC-30",
        "name": "Barco EC-30",
        "subtitle": "Event Controller",
        "tags": ["Video", "Control"],
        "width": 170,
        "control": ["USB (Host PC)"],
    },
    {
        "title": "EC-50",
        "name": "Barco EC-50",
        "subtitle": "Event Controller",
        "tags": ["Video", "Control"],
        "width": 170,
        "outputs": ["DVI-D Monitor Out"],
        "control": ["USB-B (Host)", "USB-A 1", "USB-A 2"],
    },
    {
        "title": "PDS902",
        "name": "Barco PDS-902 3G",
        "subtitle": "Seamless Presentation Switcher",
        "tags": ["Video", "Switcher"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": [
            "DVI-I 1-4",
            "VGA 5-8 (Analog)",
            "SDI 9 (3G)",
        ],
        "outputs": [
            "PGM (DVI)",
            "PGM (VGA)",
            "PGM (SDI 3G)",
            "PVW (DVI)",
            "PVW (VGA)",
        ],
        "control": ["Network", "USB"],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "barco.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
