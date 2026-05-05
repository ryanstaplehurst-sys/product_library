"""
displays.py — Display sinks: Samsung TVs, monitors, outdoor screens.

For each screen, modelled as a sink with the typical port set. Sizes are
separate library entries so the picker can find them by inches.
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


def samsung_tv(size_inches, model_suffix=""):
    title = f"Samsung {size_inches}\""
    if model_suffix:
        title += f" {model_suffix}"
    return {
        "title": title,
        "name": f"Samsung {size_inches}\" {model_suffix}".strip(),
        "subtitle": "4K Smart TV",
        "tags": ["Video", "Display", "Sink"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "HDMI 1",
            "HDMI 2",
            "HDMI 3",
            "HDMI 4 (ARC)",
            "USB",
            "Optical Audio In",
        ],
        "outputs": ["Audio Return (eARC)"],
        "control": ["Network", "WiFi"],
    }


def samsung_outdoor(size_inches, model):
    return {
        "title": f"Samsung Outdoor {size_inches}\" {model}",
        "name": f"Samsung {model}",
        "subtitle": f"{size_inches}\" Outdoor 4K",
        "tags": ["Video", "Display", "Outdoor"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["Mains In (IP66)"],
        "inputs": [
            "HDMI 1",
            "HDMI 2",
            "USB",
        ],
        "control": ["Network"],
    }


def basic_monitor(brand, size, name=None, has_dp=True):
    title = f"{brand} {size}\""
    return {
        "title": title,
        "name": name or f"{brand} {size}\" Monitor",
        "subtitle": "Computer Monitor",
        "tags": ["Video", "Display", "Sink"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": (
            ["HDMI", "DisplayPort", "USB-C"] if has_dp
            else ["HDMI", "USB-C"]
        ),
    }


DEVICES = [
    # Samsung TVs (one entry per common size — same chassis, different tile label)
    samsung_tv("24"),
    samsung_tv("32", "HD"),
    samsung_tv("40"),
    samsung_tv("43"),
    samsung_tv("43", "Silver Bezel"),
    samsung_tv("43", "UE43TU70"),
    samsung_tv("43", "U7000F"),
    samsung_tv("50"),
    samsung_tv("50", "UE50DU7100K"),
    samsung_tv("55"),
    samsung_tv("55", "UE55DU7100K"),
    samsung_tv("55", "UE55U7000FK"),
    samsung_tv("65"),
    samsung_tv("75"),
    samsung_tv("85"),
    samsung_tv("98"),

    # Samsung Outdoor
    samsung_outdoor("55", "LH55OHF2VBC"),
    samsung_outdoor("55", "QE55LST7TCU"),

    # Other monitors
    basic_monitor("HP", "27", name="HP 5527SF"),
    basic_monitor("IIYAMA", "24"),
    basic_monitor("IIYAMA", "28", name="IIYAMA Prolite 28\""),
    basic_monitor("Lenovo", "27"),
]


if __name__ == "__main__":
    out = REPO / "libraries" / "displays.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
