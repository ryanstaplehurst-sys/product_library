"""
novastar.py — Novastar LED processor library specs.

Run: python3 sources/novastar.py

Devices:
    - MCTRL4K       — workhorse 4K controller
    - MCTRL R5      — newer all-in-one controller
    - MX40 Pro      — popular all-in-one 4K
    - MX2000 Pro    — flagship 8K all-in-one (COEX)
    - H Series (H9) — modular video wall processor
    - NovaPro UHD Jr — legacy 4K
    - CVT 10        — fibre/cat6 distribution
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "mctrl4k",
        "name": "Novastar MCTRL4K",
        "subtitle": "4K LED Controller",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:", "Genlock In"],
        "inputs": [
            "SDI 1 (3G)",
            "SDI 2 (3G)",
            "HDMI 1.4 1",
            "HDMI 1.4 2",
            "HDMI 2.0",
            "DP 1.2",
            "DVI 1",
            "DVI 2",
            "DVI 3",
            "DVI 4",
        ],
        "outputs": [
            "DATA 1",
            "DATA 2",
            "DATA 3",
            "DATA 4",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "mctrl r5",
        "name": "Novastar MCTRL R5",
        "subtitle": "All-in-one Controller",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:", "Genlock In"],
        "inputs": [
            "HDMI 2.0 1",
            "HDMI 2.0 2",
            "SDI 1 (12G)",
            "DP 1.2",
        ],
        "outputs": [
            "DATA 1",
            "DATA 2",
            "DATA 3",
            "DATA 4",
            "DATA 5",
            "DATA 6",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "mx40 pro",
        "name": "Novastar MX40 Pro",
        "subtitle": "4K All-in-one Processor",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "HDMI 2.0 1",
            "HDMI 2.0 2",
            "DP 1.2 1",
            "DP 1.2 2",
            "SDI 1 (12G)",
            "SDI 2 (12G)",
        ],
        "outputs": [
            "DATA 1",
            "DATA 2",
            "DATA 3",
            "DATA 4",
            "DATA 5",
            "DATA 6",
            "DATA 7",
            "DATA 8",
        ],
        "control": [
            "Network 1",
            "Network 2",
            "USB",
            "Audio",
        ],
    },
    {
        "title": "mx2000 pro",
        "name": "Novastar MX2000 Pro",
        "subtitle": "8K COEX Processor",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "HDMI 2.1",
            "HDMI 2.0 1",
            "HDMI 2.0 2",
            "DP 1.4",
            "SDI 1 (12G)",
            "SDI 2 (12G)",
            "ST 2110",
        ],
        "outputs": [
            "DATA 1 (10G)",
            "DATA 2 (10G)",
            "DATA 3 (10G)",
            "DATA 4 (10G)",
            "DATA 5 (10G)",
            "DATA 6 (10G)",
            "DATA 7 (10G)",
            "DATA 8 (10G)",
        ],
        "control": [
            "Network 1",
            "Network 2",
            "USB",
            "Audio",
        ],
    },
    {
        "title": "H9",
        "name": "Novastar H Series H9",
        "subtitle": "Modular Video Wall",
        "tags": ["LED", "Processor"],
        "width": 170,
        "loose_ports": ["IP:", "Modular Slot Bay"],
        "inputs": [
            "HDMI 2.0 1",
            "HDMI 2.0 2",
            "HDMI 2.0 3",
            "HDMI 2.0 4",
            "DP 1.2 1",
            "DP 1.2 2",
            "SDI 1 (12G)",
            "SDI 2 (12G)",
        ],
        "outputs": [
            "DATA 1 (10G)",
            "DATA 2 (10G)",
            "DATA 3 (10G)",
            "DATA 4 (10G)",
            "HDMI Mon",
        ],
        "control": [
            "Network 1",
            "Network 2",
            "USB",
        ],
    },
    {
        "title": "novapro UHD jr",
        "name": "Novastar NovaPro UHD Jr",
        "subtitle": "Legacy 4K Processor",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:", "Genlock In"],
        "inputs": [
            "HDMI 2.0",
            "HDMI 1.4",
            "DP 1.2",
            "DVI 1",
            "DVI 2",
        ],
        "outputs": [
            "DATA 1",
            "DATA 2",
            "DATA 3",
            "DATA 4",
            "HDMI Mon",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "CVT 10",
        "name": "Novastar CVT 10",
        "subtitle": "Fibre Converter",
        "tags": ["LED", "Distribution"],
        "width": 160,
        "loose_ports": ["IP:"],
        "inputs": [
            "DATA In",
            "Fibre In",
        ],
        "outputs": [
            "DATA Out",
            "Fibre Out",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "novastar.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
