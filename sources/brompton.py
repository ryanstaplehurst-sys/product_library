"""
brompton.py — Brompton Tessera LED processor library specs.

Run from the repo root:
    python3 sources/brompton.py
which writes libraries/brompton.xml.

Devices included:
    - Tessera SX40        — workhorse 4K processor
    - Tessera S8          — flagship 8K processor
    - Tessera M2          — compact processor
    - Tessera T1          — entry-level
    - Tessera XD          — 10G data distribution
    - Tessera 4-Port Switch — Brompton-recommended managed switch (generic)
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "tessera SX40",
        "name": "Brompton Tessera SX40",
        "subtitle": "4K LED Processor",
        "tags": ["LED", "Processor"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "SDI 1 (12G)",
            "SDI 2 (12G)",
            "SDI 3 (12G)",
            "SDI 4 (12G)",
            "HDMI 1 (2.0)",
            "HDMI 2 (2.0)",
            "DP 1 (1.2)",
            "DP 2 (1.2)",
            "DP 3 (1.2)",
            "DP 4 (1.2)",
        ],
        "outputs": [
            "DATA A (10G)",
            "DATA B (10G)",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "tessera S8",
        "name": "Brompton Tessera S8",
        "subtitle": "8K LED Processor",
        "tags": ["LED", "Processor"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "SDI 1 (12G)",
            "SDI 2 (12G)",
            "SDI 3 (12G)",
            "SDI 4 (12G)",
            "HDMI 1 (2.1)",
            "HDMI 2 (2.1)",
            "DP 1 (1.4)",
            "DP 2 (1.4)",
            "DP 3 (1.4)",
            "DP 4 (1.4)",
            "ST 2110 1",
            "ST 2110 2",
        ],
        "outputs": [
            "DATA A (10G)",
            "DATA B (10G)",
            "DATA C (10G)",
            "DATA D (10G)",
            "DATA E (10G)",
            "DATA F (10G)",
            "DATA G (10G)",
            "DATA H (10G)",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "tessera M2",
        "name": "Brompton Tessera M2",
        "subtitle": "Compact LED Processor",
        "tags": ["LED", "Processor"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["IP:", "Genlock"],
        "inputs": [
            "SDI 1 (12G)",
            "SDI 2 (12G)",
            "HDMI 1 (2.0)",
            "HDMI 2 (2.0)",
            "DP 1 (1.2)",
            "DP 2 (1.2)",
        ],
        "outputs": [
            "DATA A (10G)",
            "DATA B (10G)",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "tessera T1",
        "name": "Brompton Tessera T1",
        "subtitle": "Entry LED Processor",
        "tags": ["LED", "Processor"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["IP:"],
        "inputs": [
            "SDI 1 (3G)",
            "HDMI 1 (1.4)",
            "DP 1 (1.2)",
        ],
        "outputs": [
            "DATA A (1G)",
            "DATA B (1G)",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "tessera XD",
        "name": "Brompton Tessera XD",
        "subtitle": "10G Data Distribution",
        "tags": ["LED", "Distribution"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["IP:"],
        "inputs": [
            "DATA In A",
            "DATA In B",
        ],
        "outputs": [
            "DATA Out 1",
            "DATA Out 2",
            "DATA Out 3",
            "DATA Out 4",
            "DATA Out 5",
            "DATA Out 6",
            "DATA Out 7",
            "DATA Out 8",
        ],
        "control": [
            "Network",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "brompton.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
