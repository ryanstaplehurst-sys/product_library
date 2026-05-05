"""decimator.py — Decimator video converter library specs."""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "MD-HX",
        "name": "Decimator MD-HX",
        "subtitle": "HDMI/SDI Cross Converter",
        "tags": ["Video", "Convert"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In", "USB"],
        "inputs": [
            "HDMI In",
            "SDI In",
        ],
        "outputs": [
            "HDMI Out",
            "SDI Out",
        ],
    },
    {
        "title": "MD-Cross v3",
        "name": "Decimator MD-Cross v3",
        "subtitle": "HDMI/SDI Bi-Directional",
        "tags": ["Video", "Convert"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In", "USB"],
        "inputs": [
            "HDMI In",
            "SDI In",
        ],
        "outputs": [
            "HDMI Out",
            "SDI Out 1",
            "SDI Out 2",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "decimator.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
