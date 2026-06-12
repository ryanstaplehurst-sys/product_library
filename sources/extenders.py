"""
extenders.py — HDMI/USB extenders + small video switchers.
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


DEVICES = [
    {
        "title": "LINDY USB CAT5 TX",
        "name": "LINDY USB 2.0 CAT5",
        "subtitle": "USB Extender (TX)",
        "tags": ["USB", "Extender"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "USB-B (PC)",
        ],
        "outputs": [
            "Cat5 Out (RJ45)",
        ],
    },
    {
        "title": "LINDY USB CAT5 RX",
        "name": "LINDY USB 2.0 CAT5",
        "subtitle": "USB Extender (RX)",
        "tags": ["USB", "Extender"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "Cat5 In (RJ45)",
        ],
        "outputs": [
            "USB-A 1",
            "USB-A 2",
            "USB-A 3",
            "USB-A 4",
        ],
    },
    {
        "title": "Neoteck HDMI Ext RX",
        "name": "Neoteck HDMI Extender",
        "subtitle": "HDMI over Cat (RX)",
        "tags": ["Video", "Extender"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "Cat5/6 In (RJ45)",
        ],
        "outputs": [
            "HDMI Out",
        ],
    },
    {
        "title": "HDMI Switch 3:1",
        "name": "Generic 3:1 HDMI Switch",
        "subtitle": "3-input HDMI Switch",
        "tags": ["Video", "Switcher"],
        "width": 160,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "HDMI In 1",
            "HDMI In 2",
            "HDMI In 3",
        ],
        "outputs": [
            "HDMI Out",
        ],
    },
    {
        "title": "Pro Signal 4x4 4K",
        "name": "Pro Signal 4×4 4K HDMI 2.0",
        "subtitle": "HDMI Matrix Switch",
        "tags": ["Video", "Switcher", "Matrix"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["DC Power In"],
        "inputs": [
            "HDMI In 1",
            "HDMI In 2",
            "HDMI In 3",
            "HDMI In 4",
        ],
        "outputs": [
            "HDMI Out 1",
            "HDMI Out 2",
            "HDMI Out 3",
            "HDMI Out 4",
        ],
        "control": [
            "RS-232",
            "IR",
        ],
    },
    {
        "title": "Datapath FX4/H",
        "name": "Datapath FX4/H",
        "subtitle": "4-output Display Wall",
        "tags": ["Video", "Processor", "Display Wall"],
        "width": 180,
        "info_row": True,
        "loose_ports": ["Mains In"],
        "inputs": [
            "HDMI In 1",
            "HDMI In 2",
            "DP In",
        ],
        "outputs": [
            "HDMI Out 1",
            "HDMI Out 2",
            "HDMI Out 3",
            "HDMI Out 4",
            "DP Loop Out",
        ],
        "control": [
            "LAN 1",
            "LAN 2 (Loop)",
            "USB",
        ],
    },
    {
        "title": "HDBaseT 4KEX70 TX",
        "name": "HDBaseT-Lite 4KEX70-L TX",
        "subtitle": "HDMI over Cat6 Sender",
        "tags": ["Video", "Extender"],
        "width": 170,
        "inputs": ["HDMI In"],
        "outputs": ["HDBT Out (Cat6)"],
        "control": ["RS-232", "IR"],
    },
    {
        "title": "HDBaseT 4KEX70 RX",
        "name": "HDBaseT-Lite 4KEX70-L RX",
        "subtitle": "HDMI over Cat6 Receiver",
        "tags": ["Video", "Extender"],
        "width": 170,
        "inputs": ["HDBT In (Cat6)"],
        "outputs": ["HDMI Out"],
        "control": ["RS-232", "IR"],
    },
    {
        "title": "MT-VIKI KVM 8",
        "name": "MT-VIKI 8-Port HDMI KVM",
        "subtitle": "KVM Switch",
        "tags": ["Video", "KVM"],
        "width": 170,
        "inputs": [
            "HDMI In 1-8",
            "USB Host 1-8",
        ],
        "outputs": ["HDMI Out", "USB Devices"],
        "control": ["IR Remote"],
    },
    {
        "title": "TESmart KVM 8",
        "name": "TESmart 8-Port HDMI KVM",
        "subtitle": "KVM Switch",
        "tags": ["Video", "KVM"],
        "width": 170,
        "inputs": [
            "HDMI In 1-8",
            "USB Host 1-8",
        ],
        "outputs": ["HDMI Out", "USB Devices"],
        "control": ["LAN", "RS-232", "IR Remote"],
    },
    {
        "title": "Extron HDMI DA6",
        "name": "Extron 6-Way HDMI DA",
        "subtitle": "Distribution Amplifier",
        "tags": ["Video", "DA"],
        "width": 170,
        "inputs": ["HDMI In"],
        "outputs": [
            "HDMI Out 1",
            "HDMI Out 2",
            "HDMI Out 3",
            "HDMI Out 4",
            "HDMI Out 5",
            "HDMI Out 6",
        ],
    },
    {
        "title": "Extron SDI DA 1:4",
        "name": "Extron SDI / HD-SDI DA",
        "subtitle": "1-in 4-out Distribution Amp",
        "tags": ["Video", "DA"],
        "width": 170,
        "inputs": ["SDI In"],
        "outputs": [
            "SDI Out 1",
            "SDI Out 2",
            "SDI Out 3",
            "SDI Out 4",
        ],
    },
    {
        "title": "Extron DTP TX",
        "name": "Extron DTP CAT6 TX",
        "subtitle": "HDMI Twisted-Pair Sender",
        "tags": ["Video", "Extender"],
        "width": 170,
        "inputs": ["HDMI In"],
        "outputs": ["DTP Out (Cat6)"],
        "control": ["RS-232 / IR"],
    },
    {
        "title": "Extron DTP RX",
        "name": "Extron DTP CAT6 RX",
        "subtitle": "HDMI Twisted-Pair Receiver",
        "tags": ["Video", "Extender"],
        "width": 170,
        "inputs": ["DTP In (Cat6)"],
        "outputs": ["HDMI Out"],
        "control": ["RS-232 / IR"],
    },
    {
        "title": "Lightware Fibre TX",
        "name": "Lightware DVI/HDMI Fibre TX",
        "subtitle": "Fibre Extender Sender (275m)",
        "tags": ["Video", "Extender"],
        "width": 170,
        "inputs": ["DVI/HDMI In"],
        "outputs": ["Fibre Out"],
    },
    {
        "title": "Lightware Fibre RX",
        "name": "Lightware DVI/HDMI Fibre RX",
        "subtitle": "Fibre Extender Receiver",
        "tags": ["Video", "Extender"],
        "width": 170,
        "inputs": ["Fibre In"],
        "outputs": ["DVI/HDMI Out"],
    },
    {
        "title": "Teradek Bolt TX",
        "name": "Teradek Bolt 500 LT TX",
        "subtitle": "Wireless SDI Sender",
        "tags": ["Video", "Wireless"],
        "width": 170,
        "inputs": ["SDI In"],
        "outputs": ["SDI Loop Out", "RF Out"],
    },
    {
        "title": "Teradek Bolt RX",
        "name": "Teradek Bolt 500 LT RX",
        "subtitle": "Wireless SDI Receiver",
        "tags": ["Video", "Wireless"],
        "width": 170,
        "inputs": ["RF In"],
        "outputs": ["SDI Out"],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "extenders.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
