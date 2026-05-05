"""
novastar.py — Novastar LED processor library specs.

Run: python3 sources/novastar.py

Devices:
    - MCTRL4K       — workhorse 4K controller
    - MCTRL R5      — newer all-in-one controller
    - MCTRL660      — legacy 1080p controller
    - MX40 Pro      — popular all-in-one 4K
    - MX30          — mid-range all-in-one
    - MX20          — entry all-in-one
    - MX2000 Pro    — flagship 8K all-in-one (COEX)
    - H Series (H9) — modular video wall processor
    - NovaPro UHD Jr — legacy 4K
    - VX1000        — all-in-one with screen mgmt
    - VX6S          — compact all-in-one
    - VX4U          — 4K all-in-one
    - VX4           — basic 4K all-in-one
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
    {
        "title": "mctrl660",
        "name": "Novastar MCTRL660",
        "subtitle": "1080p Controller",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:"],
        "inputs": [
            "HDMI 1.3",
            "DVI",
            "DP 1.1",
            "SDI Loop In",
        ],
        "outputs": [
            "DATA 1",
            "DATA 2",
            "DVI Loop",
        ],
        "control": [
            "Network",
            "USB",
        ],
    },
    {
        "title": "MX20",
        "name": "Novastar MX20",
        "subtitle": "Entry All-in-one",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:", "Genlock"],
        "inputs": [
            "HDMI 2.0",
            "DP 1.2",
            "SDI (12G)",
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
            "Audio",
        ],
    },
    {
        "title": "MX30",
        "name": "Novastar MX30",
        "subtitle": "Mid-range All-in-one",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "HDMI 2.0 1",
            "HDMI 2.0 2",
            "DP 1.2",
            "SDI (12G)",
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
            "Network 1",
            "Network 2",
            "USB",
            "Audio",
        ],
    },
    {
        "title": "VX1000",
        "name": "Novastar VX1000",
        "subtitle": "All-in-one + Screen Mgmt",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:", "Genlock In", "Genlock Loop"],
        "inputs": [
            "HDMI 2.0 1",
            "HDMI 2.0 2",
            "DP 1.2",
            "DVI",
            "SDI (3G)",
            "VGA",
            "CVBS",
        ],
        "outputs": [
            "DATA 1",
            "DATA 2",
            "DATA 3",
            "DATA 4",
            "DATA 5",
            "DATA 6",
            "HDMI Mon",
        ],
        "control": [
            "Network",
            "USB",
            "Audio",
        ],
    },
    {
        "title": "VX6S",
        "name": "Novastar VX6S",
        "subtitle": "Compact All-in-one",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:"],
        "inputs": [
            "HDMI 1.3",
            "DVI",
            "DP 1.1",
            "VGA",
            "CVBS",
        ],
        "outputs": [
            "DATA 1",
            "DATA 2",
            "DATA 3",
            "DATA 4",
            "DATA 5",
            "DATA 6",
            "HDMI Mon",
        ],
        "control": [
            "Network",
            "USB",
            "Audio",
        ],
    },
    {
        "title": "VX4U",
        "name": "Novastar VX4U",
        "subtitle": "4K All-in-one",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:", "Genlock"],
        "inputs": [
            "HDMI 2.0 1",
            "HDMI 2.0 2",
            "DP 1.2",
            "SDI (12G)",
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
        "title": "VX4",
        "name": "Novastar VX4",
        "subtitle": "4K All-in-one (basic)",
        "tags": ["LED", "Processor"],
        "width": 160,
        "loose_ports": ["IP:"],
        "inputs": [
            "HDMI 2.0",
            "DP 1.2",
            "DVI",
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
]


if __name__ == "__main__":
    out = REPO / "libraries" / "novastar.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
