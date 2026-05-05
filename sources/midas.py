"""midas.py — Midas digital stagebox library specs."""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "DL32",
        "name": "Midas DL32",
        "subtitle": "32/16 Digital Stagebox",
        "tags": ["Audio", "Stagebox"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "Mic/Line 1",
            "Mic/Line 2",
            "Mic/Line 3",
            "Mic/Line 4",
            "Mic/Line 5",
            "Mic/Line 6",
            "Mic/Line 7",
            "Mic/Line 8",
            "Mic/Line 9-16",
            "Mic/Line 17-24",
            "Mic/Line 25-32",
        ],
        "outputs": [
            "Output 1",
            "Output 2",
            "Output 3",
            "Output 4",
            "Output 5-8",
            "Output 9-16",
            "AES Out",
        ],
        "control": [
            "AES50 A",
            "AES50 B",
            "ULTRANET",
            "MIDI In",
            "MIDI Out",
            "Network",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "midas.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
