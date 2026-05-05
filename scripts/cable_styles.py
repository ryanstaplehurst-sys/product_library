"""
cable_styles.py — Insert Productions cable convention styles.

Single source of truth for cable line styles. Used by:
    - sources/_cables.py to build the libraries/_cables.xml reference library
    - scripts/compose_diagram.py to style edges between device ports

Convention principles:
    - Colour     = signal type (yellow=SDI, green=audio, blue=IP video, …)
    - Line style = transport (solid=copper, dashed=fibre, dotted=wireless)
    - Width      = criticality (thin=control, normal=signal, thick=power)

If the composer can't classify a cable from the brief, it falls back to
GENERIC ("solid black, 1px") — this is intentional: an unstyled cable in
a diagram is a flag to the user, not a guess.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Style fragments
# ---------------------------------------------------------------------------

_BASE = (
    "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;"
    "html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;"
)


def _style(stroke: str, width: float = 1.5, dash_pattern: str | None = None, dotted: bool = False) -> str:
    parts = [_BASE, f"strokeColor={stroke}", f"strokeWidth={width}"]
    if dash_pattern:
        parts.append("dashed=1")
        parts.append(f"dashPattern={dash_pattern}")
    elif dotted:
        parts.append("dashed=1")
        parts.append("dashPattern=1 4")
    return ";".join(parts) + ";"


# ---------------------------------------------------------------------------
# Cable style table
#
# key     : canonical cable id (used in compose specs)
# label   : human-readable name shown on the legend tile
# style   : draw.io edge style string
# colour  : the stroke colour (kept separately for reference/legends)
# aliases : strings the brief parser will match (case-insensitive)
# ---------------------------------------------------------------------------

CABLE_STYLES: dict[str, dict] = {
    "sdi": {
        "label": "SDI (copper)",
        "colour": "#E5C100",
        "style": _style("#E5C100", 1.8),
        "aliases": ["sdi", "3g-sdi", "12g-sdi", "6g-sdi", "hd-sdi", "bnc"],
    },
    "sdi_fibre": {
        "label": "SDI over fibre / SMPTE",
        "colour": "#E5C100",
        "style": _style("#E5C100", 1.8, dash_pattern="6 4"),
        "aliases": ["smpte", "sdi fibre", "sdi over fibre", "sdi fiber", "fibre sdi"],
    },
    "hdmi": {
        "label": "HDMI / DisplayPort",
        "colour": "#7F3FBF",
        "style": _style("#7F3FBF", 1.8),
        "aliases": ["hdmi", "dp", "displayport", "dvi"],
    },
    "ip_video": {
        "label": "IP video (NDI / ST 2110)",
        "colour": "#1F6FEB",
        "style": _style("#1F6FEB", 1.8),
        "aliases": ["ndi", "st2110", "st 2110", "2110", "ip video", "srt"],
    },
    "ip_video_fibre": {
        "label": "IP video over fibre",
        "colour": "#1F6FEB",
        "style": _style("#1F6FEB", 1.8, dash_pattern="6 4"),
        "aliases": ["10g fibre", "ip fibre", "ip fiber", "ip over fibre"],
    },
    "led_data": {
        "label": "LED data (Cat6/10G)",
        "colour": "#0A6E5A",
        "style": _style("#0A6E5A", 2.0),
        "aliases": ["data", "led data", "tessera data", "cat6 led"],
    },
    "led_data_fibre": {
        "label": "LED data over fibre",
        "colour": "#0A6E5A",
        "style": _style("#0A6E5A", 2.0, dash_pattern="6 4"),
        "aliases": ["led fibre", "data fibre", "data fiber"],
    },
    "audio_analog": {
        "label": "Analog audio",
        "colour": "#E91E63",
        "style": _style("#E91E63", 1.5),
        "aliases": ["analog audio", "xlr", "trs", "line", "mic"],
    },
    "aes": {
        "label": "AES3 / MADI",
        "colour": "#2E7D32",
        "style": _style("#2E7D32", 1.5),
        "aliases": ["aes", "aes3", "aes/ebu", "madi"],
    },
    "dante": {
        "label": "Dante / AoIP",
        "colour": "#2E7D32",
        "style": _style("#2E7D32", 1.5, dash_pattern="6 4"),
        "aliases": ["dante", "aoip", "audio over ip", "ravenna"],
    },
    "dmx": {
        "label": "DMX / sACN",
        "colour": "#C2185B",
        "style": _style("#C2185B", 1.5),
        "aliases": ["dmx", "sacn", "artnet", "art-net", "art net"],
    },
    "timecode": {
        "label": "Timecode (LTC)",
        "colour": "#F57C00",
        "style": _style("#F57C00", 1.5),
        "aliases": ["ltc", "timecode", "tc", "smpte tc"],
    },
    "genlock": {
        "label": "Genlock / Reference",
        "colour": "#F57C00",
        "style": _style("#F57C00", 1.5, dash_pattern="3 3"),
        "aliases": ["genlock", "ref", "reference", "blackburst", "tri-level", "tri level"],
    },
    "network": {
        "label": "Network / Control (Cat5/6)",
        "colour": "#666666",
        "style": _style("#666666", 1.0),
        "aliases": ["network", "ethernet", "cat5", "cat6", "control", "rj45", "lan"],
    },
    "wireless": {
        "label": "Wireless RF / IR",
        "colour": "#666666",
        "style": _style("#666666", 1.0, dotted=True),
        "aliases": ["wireless", "rf", "ir", "antenna", "radio"],
    },
    "usb": {
        "label": "USB",
        "colour": "#9E9E9E",
        "style": _style("#9E9E9E", 1.0),
        "aliases": ["usb", "usb-c", "usb c", "thunderbolt"],
    },
    "power_single": {
        "label": "Mains power (13/16A)",
        "colour": "#000000",
        "style": _style("#000000", 3.0),
        "aliases": ["13a", "16a", "mains", "power", "iec", "powercon"],
    },
    "power_3ph": {
        "label": "Mains power (32A 3-phase)",
        "colour": "#D32F2F",
        "style": _style("#D32F2F", 3.0),
        "aliases": ["32a", "63a", "3 phase", "3-phase", "three phase", "ceeform"],
    },
    "generic": {
        "label": "Unspecified",
        "colour": "#000000",
        "style": _style("#000000", 1.5),
        "aliases": [],
    },
}


def classify_cable(hint: str | None) -> str:
    """Map a free-form cable hint to a canonical CABLE_STYLES key.

    Used by the composer when a brief says "wire SDI from camera to switcher".
    Returns "generic" if nothing matches.
    """
    if not hint:
        return "generic"
    h = hint.lower().strip()
    # Direct key match first
    if h in CABLE_STYLES:
        return h
    # Alias match — longest first to avoid "audio" matching before "audio_analog"
    candidates: list[tuple[str, str]] = []
    for key, meta in CABLE_STYLES.items():
        for alias in meta["aliases"]:
            if alias in h:
                candidates.append((alias, key))
    if candidates:
        candidates.sort(key=lambda c: -len(c[0]))
        return candidates[0][1]
    return "generic"


def style_for(hint: str | None) -> str:
    """Return the draw.io edge style string for a cable hint."""
    return CABLE_STYLES[classify_cable(hint)]["style"]


def label_for(hint: str | None) -> str:
    """Return the human-readable cable label for a hint."""
    return CABLE_STYLES[classify_cable(hint)]["label"]
