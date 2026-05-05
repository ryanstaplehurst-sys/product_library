"""
computers.py — Laptops, NUCs, workstations.

Mac Studio is in playback.xml (it's a media-rack workstation). Workstation
HE (vMix/Pixera) is also in playback.xml. This file covers laptops + NUCs.
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


def macbook(model_name, subtitle):
    return {
        "title": model_name.split(" - ")[0] if " - " in model_name else model_name,
        "name": f"Apple MacBook {model_name}",
        "subtitle": subtitle,
        "tags": ["Computer", "Laptop"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["MagSafe / USB-C Power"],
        "outputs": [
            "TB4 / DP 1 (USB-C)",
            "TB4 / DP 2 (USB-C)",
            "TB4 / DP 3 (USB-C)",
            "HDMI",
            "Phones (3.5mm)",
        ],
        "control": [
            "WiFi",
            "Bluetooth",
        ],
    }


def lenovo_legion(variant):
    return {
        "title": f"Legion {variant}",
        "name": f"Lenovo Legion {variant}",
        "subtitle": "Gaming Laptop",
        "tags": ["Computer", "Laptop"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "HDMI",
            "DP (USB-C)",
            "USB-A 1",
            "USB-A 2",
            "USB-C",
            "Phones",
        ],
        "control": [
            "Ethernet",
            "WiFi",
            "Bluetooth",
        ],
    }


DEVICES = [
    macbook("Pro M4", "M4 Pro Laptop"),
    macbook("Pro M3 Max - 36GB", "M3 Max 36GB Laptop"),
    macbook("Pro M2 Pro Max", "M2 Pro Max 30-core Laptop"),
    macbook("Air M3", "M3 Air Laptop"),
    macbook("Pro 2019 15.4", "Intel 15.4\" Laptop (legacy)"),
    lenovo_legion("V15"),
    lenovo_legion("GTX 1660"),
    lenovo_legion("RTX 2060"),
    lenovo_legion("RTX 3070"),
    lenovo_legion("RTX 4060"),
    {
        "title": "MSI 15.6 RTX 4050",
        "name": "MSI 15.6\" RTX 4050",
        "subtitle": "i5 + 512GB SSD Laptop",
        "tags": ["Computer", "Laptop"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "HDMI",
            "USB-C",
            "USB-A 1",
            "USB-A 2",
            "Phones",
        ],
        "control": [
            "Ethernet",
            "WiFi",
            "Bluetooth",
        ],
    },
    {
        "title": "Intel NUC i5",
        "name": "Intel NUC i5 13th Gen",
        "subtitle": "Compact PC",
        "tags": ["Computer", "PC"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "HDMI 1",
            "HDMI 2",
            "DP (USB-C)",
            "USB-A 1",
            "USB-A 2",
            "USB-A 3",
            "USB-C",
            "Phones",
        ],
        "control": [
            "Ethernet",
            "WiFi",
            "Bluetooth",
        ],
    },
    {
        "title": "Intel NUC i7 SFF",
        "name": "Intel NUC i7 SFF",
        "subtitle": "Small Form Factor PC",
        "tags": ["Computer", "PC"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "outputs": [
            "HDMI",
            "DP",
            "USB-A 1",
            "USB-A 2",
            "USB-C",
            "Phones",
        ],
        "control": [
            "Ethernet",
            "WiFi",
            "Bluetooth",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "computers.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
