"""dj-kit.py — Pioneer DJ kit and accessories."""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "CDJ-3000",
        "name": "Pioneer CDJ-3000",
        "subtitle": "Pro DJ Multiplayer",
        "tags": ["Audio", "DJ"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "outputs": [
            "Audio Out L (RCA)",
            "Audio Out R (RCA)",
            "Digital Out (S/PDIF)",
        ],
        "control": [
            "Pro DJ Link (RJ45)",
            "USB-A",
            "USB-B",
        ],
    },
    {
        "title": "DJM-A9",
        "name": "Pioneer DJM-A9",
        "subtitle": "4-channel DJ Mixer",
        "tags": ["Audio", "DJ", "Console"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Ch1 Line (RCA)",
            "Ch1 Phono (RCA)",
            "Ch1 Digital",
            "Ch2 Line (RCA)",
            "Ch2 Digital",
            "Ch3 Line (RCA)",
            "Ch3 Digital",
            "Ch4 Line (RCA)",
            "Ch4 Digital",
            "Mic 1 (XLR/TRS)",
            "Mic 2 (TRS)",
            "Aux In",
            "Return L (TRS)",
            "Return R (TRS)",
        ],
        "outputs": [
            "Master Out 1 (XLR)",
            "Master Out 2 (RCA)",
            "Booth Out (TRS)",
            "Rec Out (RCA)",
            "Send L (TRS)",
            "Send R (TRS)",
            "Phones 1",
            "Phones 2",
            "Digital Master Out",
        ],
        "control": [
            "Pro DJ Link (RJ45)",
            "USB-A 1",
            "USB-A 2",
            "USB-B 1",
            "USB-B 2",
            "MIDI",
        ],
    },
    {
        "title": "Pioneer DJ Kit",
        "name": "Pioneer DJ Kit",
        "subtitle": "Decks + Mixer + Riser (bundle)",
        "tags": ["Audio", "DJ"],
        "width": 170,
        "info_row": True,
        "outputs": [
            "Master L (XLR)",
            "Master R (XLR)",
        ],
        "control": [
            "Pro DJ Link",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "dj-kit.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
