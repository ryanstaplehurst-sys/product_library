"""
dnb.py — d&b audiotechnik library specs.

Devices:
    - D12, D20, D40, D80   — 4-channel amplifiers
    - E8                    — point source loudspeaker (passive)
    - M4                    — stage monitor (passive)
    - T10                   — line array element (passive)
    - V-Sub                 — flown subwoofer (passive)
    - Y10P, Y7P             — point source loudspeakers (passive)

All speakers driven by d&b amps via NL4. Models with built-in amps would
have different chassis but Insert's stock here is passive.
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


def amp(model, channels=4, name_suffix="4-ch Amplifier"):
    return {
        "title": f"d&b {model}",
        "name": f"d&b {model}",
        "subtitle": name_suffix,
        "tags": ["Audio", "Amplifier"],
        "width": 170,
        "loose_ports": ["IP:", "Mains In"],
        "inputs": [
            "AES In A (XLR)",
            "AES In B (XLR)",
            "Analog In A (XLR)",
            "Analog In B (XLR)",
        ],
        "outputs": [
            "Out 1 (NL4)",
            "Out 2 (NL4)",
            "Out 3 (NL4)",
            "Out 4 (NL4)",
        ],
        "control": [
            "Network 1",
            "Network 2",
            "CAN-Bus",
        ],
    }


def speaker(model, subtitle, dual_input=False):
    return {
        "title": f"d&b {model}",
        "name": f"d&b {model}",
        "subtitle": subtitle,
        "tags": ["Audio", "Speaker"],
        "width": 160,
        "info_row": True,
        "inputs": (
            ["Speaker In 1 (NL4)", "Speaker In 2 (NL4)"]
            if dual_input
            else ["Speaker In (NL4)"]
        ),
        "outputs": ["Speaker Link (NL4)"],
    }


DEVICES = [
    amp("D12", name_suffix="Legacy 4-ch Amp"),
    amp("D20"),
    amp("D40"),
    amp("D80", name_suffix="High-power 4-ch Amp"),
    speaker("E8", "8\" Point Source"),
    speaker("M4", "Stage Monitor"),
    speaker("T10", "Line Array Element"),
    speaker("V-Sub", "Flown Subwoofer"),
    speaker("Y10P", "10\" Point Source"),
    speaker("Y7P", "7\" Point Source"),
    speaker("E6", "Compact Loudspeaker"),
    speaker("MAX 15", "Stage Monitor"),
    speaker("Q1", "Line-Array Loudspeaker", dual_input=True),
    speaker("Q7", "Point-Source Loudspeaker", dual_input=True),
    speaker("Q-Sub", "Subwoofer", dual_input=True),
    speaker("Y8", "Line-Array Loudspeaker", dual_input=True),
    speaker("Y-Sub", "Subwoofer", dual_input=True),
    speaker("B2", "Subwoofer", dual_input=True),
    speaker("B6", "Subwoofer", dual_input=True),
    speaker("B22", "Subwoofer", dual_input=True),
    speaker("C4", "Loudspeaker", dual_input=True),
    speaker("C7", "Full-Range Loudspeaker", dual_input=True),
    {
        "title": "d&b DS10",
        "name": "d&b DS10",
        "subtitle": "Audio Network Bridge",
        "tags": ["Audio", "Network"],
        "width": 170,
        "loose_ports": ["IP:"],
        "inputs": ["Dante Primary", "Dante Secondary"],
        "outputs": [
            "AES3 Out 1",
            "AES3 Out 2",
            "AES3 Out 3",
            "AES3 Out 4",
        ],
        "control": ["Ethernet Out 1", "Ethernet Out 2"],
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
