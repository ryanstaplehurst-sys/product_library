"""
compose_diagram.py — Compose a draw.io diagram from a structured spec.

Workflow
--------

Claude reads the user's free-form brief, translates it to a JSON spec, then
runs this script to write a .drawio file. The user opens the .drawio file in
draw.io, tweaks layout, and exports.

Spec format
-----------

    {
        "title": "Studio A camera routing",
        "page_width": 1600,
        "page_height": 1000,
        "auto_layout": true,
        "devices": [
            {
                "id": "cam1",                    # required, used in connections
                "library": "blackmagic",         # required, library file name (no .xml)
                "title": "microstudiocam 4k",    # required, matches library title
                "x": 40, "y": 80,                # optional — auto if omitted
                "label_override": "Cam 1 (FOH)"  # optional — overrides chassis label
            },
            …
        ],
        "connections": [
            {
                "from": "cam1.SDI Out",          # device-id "." port-name
                "to":   "atem.SDI In 1",
                "cable": "sdi",                  # cable_styles key or free hint
                "label": "Prog feed"             # optional edge label
            },
            …
        ],
        "title_block": true,                     # adds Insert-branded title
        "legend": true                           # adds cable-style legend
    }

Run
---
    python3 scripts/compose_diagram.py --spec /tmp/spec.json --output /path/to/diagram.drawio
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET

SCRIPTS = Path(__file__).resolve().parent
REPO = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

from library_io import parse_library_file, instantiate_device, ParsedDevice  # noqa: E402
from cable_styles import classify_cable, CABLE_STYLES, style_for  # noqa: E402


# ---------------------------------------------------------------------------
# Library loading
# ---------------------------------------------------------------------------

class LibraryCache:
    """Loads + caches libraries from libraries/*.xml on demand."""

    def __init__(self, libs_dir: Path):
        self.libs_dir = libs_dir
        self._cache: dict[str, list[ParsedDevice]] = {}

    def get(self, library_name: str) -> list[ParsedDevice]:
        if library_name not in self._cache:
            path = self.libs_dir / f"{library_name}.xml"
            if not path.exists():
                raise FileNotFoundError(
                    f"Library not found: {path}. Available: "
                    + ", ".join(p.stem for p in self.libs_dir.glob("*.xml"))
                )
            self._cache[library_name] = parse_library_file(path)
        return self._cache[library_name]

    def find_device(self, library_name: str, title: str) -> ParsedDevice:
        devs = self.get(library_name)
        # Exact match first
        for d in devs:
            if d.title.lower() == title.lower():
                return d
        # Substring match
        target = title.lower()
        for d in devs:
            if target in d.title.lower() or d.title.lower() in target:
                return d
        # Fuzzy: strip punctuation/whitespace
        norm = re.sub(r"\W", "", target)
        for d in devs:
            if re.sub(r"\W", "", d.title.lower()) == norm:
                return d
        available = ", ".join(d.title for d in devs)
        raise ValueError(
            f'Device "{title}" not found in {library_name}.xml. Available: {available}'
        )


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

@dataclass
class PlacedDevice:
    """A device placed on the canvas with all its global IDs resolved."""
    spec_id: str
    title: str
    x: int
    y: int
    width: int
    height: int
    xml_fragment: str
    port_index: dict[str, str]  # port name -> globally unique cell id


def _auto_layout(
    spec_devices: list[dict],
    cache: LibraryCache,
    margin_x: int = 60,
    margin_y: int = 100,
    gap_x: int = 100,
    gap_y: int = 60,
    cols: int = 4,
) -> list[tuple[int, int]]:
    """Return a list of (x, y) for each device in the spec.

    Rows wrap every `cols` devices. Each row's y is the max-height-so-far so
    devices in the row align at the top.
    """
    positions: list[tuple[int, int]] = []
    cur_x = margin_x
    cur_y = margin_y
    row_max_h = 0
    col_count = 0
    for sd in spec_devices:
        if "x" in sd and "y" in sd:
            positions.append((sd["x"], sd["y"]))
            continue
        device = cache.find_device(sd["library"], sd["title"])
        if col_count >= cols:
            cur_x = margin_x
            cur_y += row_max_h + gap_y
            row_max_h = 0
            col_count = 0
        positions.append((cur_x, cur_y))
        cur_x += device.width + gap_x
        row_max_h = max(row_max_h, device.height)
        col_count += 1
    return positions


# ---------------------------------------------------------------------------
# Edge construction
# ---------------------------------------------------------------------------

def _parse_endpoint(endpoint: str) -> tuple[str, str]:
    """'cam1.SDI Out' → ('cam1', 'SDI Out')."""
    if "." not in endpoint:
        raise ValueError(f'Endpoint must be "device_id.Port Name": got "{endpoint}"')
    dev, port = endpoint.split(".", 1)
    return dev.strip(), port.strip()


def _edge_xml(
    edge_id: str,
    source_id: str,
    target_id: str,
    style: str,
    label: str | None = None,
) -> str:
    label_attr = f' value="{html.escape(label, quote=True)}"' if label else ""
    return (
        f'<mxCell id="{edge_id}"{label_attr} style="{style}" edge="1" '
        f'parent="1" source="{source_id}" target="{target_id}">'
        '<mxGeometry relative="1" as="geometry"/>'
        '</mxCell>'
    )


# ---------------------------------------------------------------------------
# Title block + legend
# ---------------------------------------------------------------------------

def _title_block(title: str, x: int, y: int, cell_id: str) -> str:
    style = (
        "rounded=0;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=none;"
        "fontColor=#FFFFFF;fontSize=18;fontStyle=1;fontFamily=Verdana;align=left;"
        "verticalAlign=middle;spacingLeft=20;"
    )
    return (
        f'<mxCell id="{cell_id}" value="{html.escape(title, quote=True)}" '
        f'style="{style}" vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y}" width="600" height="44" as="geometry"/>'
        '</mxCell>'
        # Red rule beneath
        f'<mxCell id="{cell_id}_rule" style="rounded=0;fillColor=#FF0000;'
        f'strokeColor=none;" vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y + 44}" width="600" height="4" as="geometry"/>'
        '</mxCell>'
    )


def _legend(used_keys: list[str], x: int, y: int, base_id: int) -> tuple[str, int]:
    """Render a legend showing the cable styles actually used in this diagram.

    Returns (xml, next_id_to_use).
    """
    if not used_keys:
        return "", base_id

    parts = []
    box_w = 320
    row_h = 22
    box_h = 36 + len(used_keys) * row_h

    # Frame
    frame_id = base_id
    parts.append(
        f'<mxCell id="{frame_id}" value="" style="rounded=0;whiteSpace=wrap;html=1;'
        f'fillColor=#FFFFFF;strokeColor=#212121;strokeWidth=1.5;" '
        f'vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y}" width="{box_w}" height="{box_h}" as="geometry"/>'
        '</mxCell>'
    )
    # Title
    title_id = base_id + 1
    parts.append(
        f'<mxCell id="{title_id}" value="CABLE LEGEND" style="text;html=1;'
        f'fontFamily=Verdana;fontSize=11;fontStyle=1;fontColor=#000000;'
        f'align=left;verticalAlign=middle;'
        f'spacingLeft=12;strokeColor=none;fillColor=none;" vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y + 4}" width="{box_w}" height="24" as="geometry"/>'
        '</mxCell>'
    )
    next_id = base_id + 2

    for i, key in enumerate(used_keys):
        meta = CABLE_STYLES[key]
        row_y = y + 30 + i * row_h
        # Sample dots
        parts.append(
            f'<mxCell id="{next_id}" style="ellipse;fillColor=#000000;'
            f'strokeColor=none;aspect=fixed;" vertex="1" parent="1">'
            f'<mxGeometry x="{x + 14}" y="{row_y + 8}" width="5" height="5" as="geometry"/>'
            '</mxCell>'
        )
        parts.append(
            f'<mxCell id="{next_id + 1}" style="ellipse;fillColor=#000000;'
            f'strokeColor=none;aspect=fixed;" vertex="1" parent="1">'
            f'<mxGeometry x="{x + 90}" y="{row_y + 8}" width="5" height="5" as="geometry"/>'
            '</mxCell>'
        )
        # Sample edge
        parts.append(
            f'<mxCell id="{next_id + 2}" style="{meta["style"]}" edge="1" '
            f'parent="1" source="{next_id}" target="{next_id + 1}">'
            '<mxGeometry relative="1" as="geometry"/>'
            '</mxCell>'
        )
        # Label
        parts.append(
            f'<mxCell id="{next_id + 3}" value="{html.escape(meta["label"], quote=True)}" '
            f'style="text;html=1;fontFamily=Verdana;fontSize=10;fontColor=#000000;'
            f'align=left;verticalAlign=middle;strokeColor=none;fillColor=none;" '
            f'vertex="1" parent="1">'
            f'<mxGeometry x="{x + 105}" y="{row_y}" width="{box_w - 110}" height="20" as="geometry"/>'
            '</mxCell>'
        )
        next_id += 4

    return "".join(parts), next_id


# ---------------------------------------------------------------------------
# Compose
# ---------------------------------------------------------------------------

def compose(spec: dict, libs_dir: Path) -> str:
    """Build a complete .drawio file content from the spec."""
    cache = LibraryCache(libs_dir)
    title = spec.get("title", "Untitled signal flow")
    page_w = spec.get("page_width", 1600)
    page_h = spec.get("page_height", 1000)

    spec_devices = spec.get("devices", [])
    spec_conns = spec.get("connections", [])

    # 1. Resolve & lay out devices
    positions = _auto_layout(spec_devices, cache)
    placed: dict[str, PlacedDevice] = {}
    device_xml_parts: list[str] = []

    title_offset = 80 if spec.get("title_block", True) else 0

    for i, sd in enumerate(spec_devices):
        spec_id = sd["id"]
        device = cache.find_device(sd["library"], sd["title"])
        x, y = positions[i]
        y += title_offset
        prefix = f"d{i}_{spec_id}"
        xml_frag, port_idx = instantiate_device(device, x, y, prefix)
        device_xml_parts.append(xml_frag)
        placed[spec_id] = PlacedDevice(
            spec_id=spec_id,
            title=device.title,
            x=x,
            y=y,
            width=device.width,
            height=device.height,
            xml_fragment=xml_frag,
            port_index=port_idx,
        )

    # 2. Build edges, tracking which cable styles got used (for the legend)
    edge_parts: list[str] = []
    used_cable_keys: list[str] = []
    edge_counter = 0
    for conn in spec_conns:
        src_dev, src_port = _parse_endpoint(conn["from"])
        dst_dev, dst_port = _parse_endpoint(conn["to"])
        if src_dev not in placed:
            raise ValueError(f"Unknown device id in connection: {src_dev}")
        if dst_dev not in placed:
            raise ValueError(f"Unknown device id in connection: {dst_dev}")
        src = placed[src_dev]
        dst = placed[dst_dev]
        # Look up port — first try exact, then ParsedDevice.find_port via the
        # original device object (more forgiving).
        src_port_id = src.port_index.get(src_port)
        if src_port_id is None:
            full_port = next(
                (k for k in src.port_index if k.lower() == src_port.lower()),
                None,
            )
            if full_port is None:
                # Fuzzy: substring
                full_port = next(
                    (k for k in src.port_index if src_port.lower() in k.lower()),
                    None,
                )
            if full_port is not None:
                src_port_id = src.port_index[full_port]
        dst_port_id = dst.port_index.get(dst_port)
        if dst_port_id is None:
            full_port = next(
                (k for k in dst.port_index if k.lower() == dst_port.lower()),
                None,
            )
            if full_port is None:
                full_port = next(
                    (k for k in dst.port_index if dst_port.lower() in k.lower()),
                    None,
                )
            if full_port is not None:
                dst_port_id = dst.port_index[full_port]

        if src_port_id is None:
            raise ValueError(
                f'Port "{src_port}" not found on {src_dev} ({src.title}). '
                f"Available: {', '.join(sorted(src.port_index))}"
            )
        if dst_port_id is None:
            raise ValueError(
                f'Port "{dst_port}" not found on {dst_dev} ({dst.title}). '
                f"Available: {', '.join(sorted(dst.port_index))}"
            )

        cable_hint = conn.get("cable")
        cable_key = classify_cable(cable_hint)
        if cable_key not in used_cable_keys and cable_key != "generic":
            used_cable_keys.append(cable_key)

        edge_id = f"e{edge_counter}"
        edge_counter += 1
        edge_parts.append(
            _edge_xml(
                edge_id,
                src_port_id,
                dst_port_id,
                style_for(cable_hint),
                conn.get("label"),
            )
        )

    # 3. Title block
    decoration_parts: list[str] = []
    if spec.get("title_block", True):
        decoration_parts.append(_title_block(title, 40, 30, "title_block"))

    # 4. Legend
    if spec.get("legend", True) and used_cable_keys:
        # Position legend at bottom-left of canvas, below all devices
        max_y = (
            max((p.y + p.height) for p in placed.values())
            if placed
            else (title_offset + 100)
        )
        leg_xml, _ = _legend(used_cable_keys, 40, max_y + 40, 99000)
        decoration_parts.append(leg_xml)

    # 5. Assemble final .drawio file
    body = (
        '<mxGraphModel dx="2000" dy="1200" grid="1" gridSize="10" guides="1" '
        'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
        f'pageWidth="{page_w}" pageHeight="{page_h}" math="0" shadow="0">'
        '<root>'
        '<mxCell id="0"/>'
        '<mxCell id="1" parent="0"/>'
        + "".join(decoration_parts)
        + "".join(device_xml_parts)
        + "".join(edge_parts)
        + "</root></mxGraphModel>"
    )

    drawio = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<mxfile host="claude.ai" type="device">\n'
        '  <diagram name="Signal flow">\n'
        f'    {body}\n'
        '  </diagram>\n'
        '</mxfile>\n'
    )
    return drawio


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--spec", required=True, help="Path to JSON spec")
    p.add_argument("--output", required=True, help="Path to write .drawio")
    p.add_argument(
        "--libs",
        default=str(REPO / "libraries"),
        help="Path to libraries dir (default: %(default)s)",
    )
    args = p.parse_args()

    spec = json.loads(Path(args.spec).read_text())
    libs = Path(args.libs)
    drawio = compose(spec, libs)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(drawio, encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
