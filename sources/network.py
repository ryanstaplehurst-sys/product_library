"""
network.py — Network infrastructure library.

Routers, switches, APs across DrayTek, Netgear, TP-Link, Ubiquiti, EE.
Switches modelled with one uplink port + N PoE/non-PoE downlinks. Specific
port counts approximated from common variants — verify on site.
"""

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))

from library_io import write_library  # noqa: E402


def switch(title, name, subtitle, ports, sfp=0):
    return {
        "title": title,
        "name": name,
        "subtitle": subtitle,
        "tags": ["Network", "Switch"],
        "width": 170,
        "loose_ports": ["IP:", "Mains In"],
        "inputs": [f"Port {i+1}" for i in range(ports)] +
                  [f"SFP {i+1}" for i in range(sfp)],
        "control": ["Console", "USB"] if sfp else [],
    }


def router(title, name, subtitle, lan_ports=4, has_sfp=False):
    ctrl = ["Console", "USB"]
    return {
        "title": title,
        "name": name,
        "subtitle": subtitle,
        "tags": ["Network", "Router"],
        "width": 170,
        "loose_ports": ["IP:", "Mains In"],
        "inputs": (["WAN 1", "WAN 2 / SFP"] if has_sfp else ["WAN"]) + [f"LAN {i+1}" for i in range(lan_ports)],
        "control": ctrl,
    }


def ap(title, name, subtitle, has_uplink=True):
    return {
        "title": title,
        "name": name,
        "subtitle": subtitle,
        "tags": ["Network", "Access Point"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["IP:"],
        "inputs": ["PoE/Uplink (RJ45)"] if has_uplink else [],
    }


DEVICES = [
    # DrayTek
    router("Vigor 3910 P", "DrayTek Vigor 3910 P", "Multi-WAN Router", lan_ports=4, has_sfp=True),
    switch("Vigor G2280x", "DrayTek Vigor G2280x", "28-port Managed PoE Switch", ports=24, sfp=4),
    switch("Vigor P2280x", "DrayTek Vigor P2280x", "28-port Managed PoE Switch", ports=24, sfp=4),
    switch("Vigor P2100", "DrayTek Vigor P2100", "10-port PoE Switch", ports=8, sfp=2),
    ap("Vigor AP 962C", "DrayTek VigorAP 962C", "Wi-Fi 6 Access Point"),

    # Netgear
    switch("GS116PP", "Netgear GS116PP", "16-port Unmanaged PoE+", ports=16),
    switch("GS724T", "Netgear ProSAFE GS724T", "24-port Managed Switch", ports=24, sfp=2),
    switch("GS748T", "Netgear ProSAFE GS748T", "48-port Managed Switch", ports=48, sfp=4),
    switch("MS510TXPP", "Netgear ProSAFE MS510TXPP", "10-port Multi-Gig PoE+", ports=8, sfp=2),
    switch("JGS516PE", "Netgear ProSAFE Plus JGS516PE", "16-port Managed Switch", ports=16),

    # TP-Link
    router("TL-WR940N", "TP-Link TL-WR940N", "Wireless N Router", lan_ports=4),
    router("AC1200", "TP-Link AC1200", "Dual-band Router", lan_ports=4),
    router("4G LTE TL-MR6400", "TP-Link TL-MR6400", "4G LTE Router", lan_ports=4),
    router("5G CPE", "TP-Link 5G CPE", "5G CPE Router", lan_ports=4),
    switch("TL 5-port", "TP-Link 5-port Switch", "Unmanaged 5-port", ports=5),
    switch("TL 8-port", "TP-Link 8-port Switch", "Unmanaged 8-port", ports=8),

    # EE
    router("EE 4G", "EE 4G Router", "4G Router (consumer)", lan_ports=2),

    # Ubiquiti
    {
        "title": "UDM Pro",
        "name": "Ubiquiti UDM Pro",
        "subtitle": "Dream Machine Pro",
        "tags": ["Network", "Router"],
        "width": 180,
        "loose_ports": ["IP:", "Mains In"],
        "inputs": [
            "WAN 1 (RJ45)",
            "WAN 2 / SFP+",
            "LAN 1",
            "LAN 2",
            "LAN 3",
            "LAN 4",
            "LAN 5",
            "LAN 6",
            "LAN 7",
            "LAN 8",
            "SFP+ 9",
            "SFP+ 10",
        ],
        "control": [
            "Console",
            "USB",
        ],
    },
    {
        "title": "USW Pro 24 PoE",
        "name": "Ubiquiti USW Pro 24 PoE",
        "subtitle": "24-port PoE+ Pro Switch",
        "tags": ["Network", "Switch"],
        "width": 180,
        "loose_ports": ["IP:", "Mains In 1", "Mains In 2"],
        "inputs": [f"Port {i+1}" for i in range(24)] + ["SFP+ 25", "SFP+ 26"],
        "control": ["Console"],
    },
    ap("U7 Pro AP", "Ubiquiti U7 Pro", "Wi-Fi 7 Access Point"),
    {
        "title": "Unifi Network Rack",
        "name": "Ubiquiti Unifi Network Rack",
        "subtitle": "Pre-rigged Unifi Stack",
        "tags": ["Network", "Bundle"],
        "width": 170,
        "info_row": True,
        "loose_ports": ["IP:", "Mains In"],
        "inputs": ["WAN"],
        "outputs": [
            "LAN Patch 1",
            "LAN Patch 2",
            "LAN Patch 3",
            "LAN Patch 4",
            "AP Drop 1",
            "AP Drop 2",
        ],
    },
]


if __name__ == "__main__":
    out = REPO / "libraries" / "network.xml"
    write_library(out, DEVICES)
    print(f"Wrote {out} ({len(DEVICES)} devices)")
