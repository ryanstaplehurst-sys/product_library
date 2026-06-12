"""
dnb.py — d&b audiotechnik library specs.

Devices:
    - D12              — legacy 2-channel amplifier (CAN only)
    - D20, D40, D80    — 4-channel amplifiers (4x switchable analog/AES3 in)
    - Passive cabinets — NL4 pair wired parallel (1 in + 1 link) unless noted
    - B2               — single EP5, no link
    - C4, C7           — EP5 pair wired parallel
    - DS10             — Dante > AES3 network bridge
    - R70              — Ethernet-CAN interface

Port layouts verified against d&b hardware manuals, June 2026.
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


def amp4(model, name_suffix="4-ch Amplifier"):
    return {
        "title": f"d&b {model}",
        "name": f"d&b {model}",
        "subtitle": name_suffix,
        "tags": ["Audio", "Amplifier"],
        "width": 170,
        "loose_ports": ["IP:", "Mains In"],
        "inputs": [
            "Input 1 (XLR Analog/AES3)",
            "Input 2 (XLR Analog/AES3)",
            "Input 3 (XLR Analog/AES3)",
            "Input 4 (XLR Analog/AES3)",
        ],
        "outputs": [
            "Link 1-4 (XLR)",
            "Out 1 (NL4)",
            "Out 2 (NL4)",
            "Out 3 (NL4)",
            "Out 4 (NL4)",
        ],
        "control": [
            "Ethernet 1 (etherCON)",
            "Ethernet 2 (etherCON)",
            "CAN 1 (RJ45)",
            "CAN 2 (RJ45)",
        ],
    }


def speaker(model, subtitle, connector="NL4", link=True):
    d = {
        "title": f"d&b {model}",
        "name": f"d&b {model}",
        "subtitle": subtitle,
        "tags": ["Audio", "Speaker"],
        "width": 160,
        "info_row": True,
        "inputs": [f"Speaker In ({connector})"],
    }
    if link:
        d["outputs"] = [f"Speaker Link ({connector})"]
    return d


DEVICES = [
    {
        "title": "d&b D12",
        "name": "d&b D12",
        "subtitle": "Legacy 2-ch Amp",
        "tags": ["Audio", "Amplifier"],
        "width": 170,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Analog In A (XLR)",
            "Analog In B (XLR)",
            "AES In D1/D2 (XLR)",
        ],
        "outputs": [
            "Link A (XLR)",
            "Link B (XLR)",
            "AES Link (XLR)",
            "Out A (NL4)",
            "Out B (NL4)",
        ],
        "control": [
            "CAN Remote 1 (RJ45)",
            "CAN Remote 2 (RJ45)",
        ],
    },
    amp4("D20"),
    amp4("D40"),
    amp4("D80", name_suffix="High-power 4-ch Amp"),
    speaker("E8", "8\" Point Source"),
    speaker("M4", "Stage Monitor"),
    speaker("T10", "Line Array Element"),
    speaker("V-Sub", "Flown Subwoofer"),
    speaker("Y10P", "10\" Point Source"),
    speaker("Y7P", "7\" Point Source"),
    speaker("E6", "Compact Loudspeaker"),
    speaker("MAX 15", "Stage Monitor"),
    speaker("Q1", "Line-Array Loudspeaker"),
    speaker("Q7", "Point-Source Loudspeaker"),
    speaker("Q-Sub", "Subwoofer"),
    speaker("Y8", "Line-Array Loudspeaker"),
    speaker("Y-Sub", "Subwoofer"),
    speaker("B2", "Subwoofer", connector="EP5", link=False),
    speaker("B6", "Subwoofer"),
    speaker("B22", "Subwoofer"),
    speaker("C4", "Loudspeaker", connector="EP5"),
    speaker("C7", "Full-Range Loudspeaker", connector="EP5"),
    {
        "title": "d&b DS10",
        "name": "d&b DS10",
        "subtitle": "Audio Network Bridge",
        "tags": ["Audio", "Network"],
        "width": 180,
        "loose_ports": ["IP:"],
        "inputs": [
            "Dante Primary",
            "Dante Secondary",
            "AES3 In 1/2",
            "AES3 In 3/4",
        ],
        "outputs": [
            "AES3 Out 1/2",
            "AES3 Out 3/4",
            "AES3 Out 5/6",
            "AES3 Out 7/8",
            "AES3 Out 9/10",
            "AES3 Out 11/12",
            "AES3 Out 13/14",
            "AES3 Out 15/16",
        ],
        "control": ["Ethernet 1-5 (etherCON switch)"],
    },
    {
        "title": "d&b R70",
        "name": "d&b R70",
        "subtitle": "Ethernet-CAN Interface",
        "tags": ["Audio", "Control"],
        "width": 170,
        "loose_ports": ["IP:"],
        "inputs": ["Ethernet"],
        "outputs": ["CAN 1", "CAN 2"],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "dnb.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
