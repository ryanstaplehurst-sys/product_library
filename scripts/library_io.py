"""
library_io.py
=============
Read and write draw.io shape libraries (.xml files) of AV equipment for
Insert Productions signal-flow diagrams.

A library file is a single <mxlibrary>...</mxlibrary> root containing a JSON
array of device entries. Each entry has:

    {
        "xml":   "<mxGraphModel>...</mxGraphModel>"   (HTML-escaped),
        "w":     int chassis width,
        "h":     int chassis height,
        "aspect": "fixed",
        "title": "library tile label"
    }

Every device is a swimlane chassis with stacked child cells:

    chassis (swimlane)
    ├── info row              (grey text cell)
    ├── loose ports           (loose text cells, no swimlane)
    ├── inputs swimlane       (green #d5e8d4)
    │   ├── port: "SDI 1"
    │   └── port: "SDI 2"
    ├── outputs swimlane      (orange #ffe6cc)
    │   └── port: "DATA A"
    └── control swimlane      (blue #dae8fc, optional)
        ├── port: "Genlock"
        └── port: "Network"

Public API
----------

    build_library_file(devices) -> str
        Build a complete .xml library file from a list of DeviceSpec dicts.

    parse_library_file(path) -> list[ParsedDevice]
        Read an existing library, return parsed device specs (for composing
        diagrams or rebuilding libraries from existing files).

    instantiate_device(parsed_device, x, y, id_prefix) -> tuple
        Take a parsed device and return mxCell XML positioned at (x, y) with
        all internal IDs prefixed for uniqueness. Returns (xml_str, port_index)
        where port_index maps port name -> global ID for cable routing.
"""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


# ---------------------------------------------------------------------------
# Style constants — matches the Blackmagic library house style
# ---------------------------------------------------------------------------

CHASSIS_FILL = "#f5f5f5"
INPUTS_FILL = "#d5e8d4"   # green
INPUTS_STROKE = "#82b366"
OUTPUTS_FILL = "#ffe6cc"  # orange
OUTPUTS_STROKE = "#d79b00"
CONTROL_FILL = "#dae8fc"  # blue
CONTROL_STROKE = "#6c8ebf"
INFO_STROKE = "#666666"

DEFAULT_FONT = "Verdana"
DEFAULT_FONT_SIZE = 13
DEFAULT_PORT_HEIGHT = 26
DEFAULT_WIDTH = 140
HEADER_HEIGHT = 40        # chassis title swimlane header
SECTION_HEADER_HEIGHT = 26  # input/output/control swimlane header

# Style fragments (built once, reused for every device)

_CHASSIS_STYLE = (
    "swimlane;fontStyle=1;childLayout=stackLayout;horizontal=1;"
    f"startSize={HEADER_HEIGHT};fillColor={CHASSIS_FILL};horizontalStack=0;"
    "resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;"
    "marginBottom=0;html=1;fontSize=13;points=[];strokeColor=default;"
    f"rounded=1;fontColor=#333333;strokeWidth=2;swimlaneBody=0;"
    f"fontFamily={DEFAULT_FONT};absoluteArcSize=1;arcSize=20;"
)

_INFO_STYLE = (
    f"text;strokeColor={INFO_STROKE};fillColor={CHASSIS_FILL};align=left;"
    "verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
    "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"
    "whiteSpace=wrap;html=1;fontColor=#333333;"
)

_LOOSE_PORT_STYLE = (
    "text;strokeColor=default;fillColor=default;align=center;"
    "verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
    "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"
    "whiteSpace=wrap;html=1;labelBorderColor=none;rounded=0;glass=0;part=0;"
)


def _section_style(fill: str) -> str:
    return (
        "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;"
        f"startSize=26;fillColor={fill};horizontalStack=0;resizeParent=1;"
        "resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;"
        "html=1;strokeColor=default;rounded=0;swimlaneFillColor=default;"
        "connectable=0;"
    )


def _port_style(align: str = "left") -> str:
    return (
        f"text;strokeColor=default;fillColor=none;align={align};"
        "verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;"
        "rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;"
        "whiteSpace=wrap;html=1;"
    )


# ---------------------------------------------------------------------------
# Device spec → XML (for building libraries)
# ---------------------------------------------------------------------------

def _esc_attr(value: str) -> str:
    """Escape a string for use as an XML attribute value."""
    return html.escape(value, quote=True)


def _make_label(name: str, subtitle: str | None = None) -> str:
    """Build the chassis title label (used as `label` on UserObject).

    Matches the Blackmagic style: bold name on top, smaller subtitle below
    inside a div with explicit font-size.
    """
    label = _esc_attr(name)
    if subtitle:
        sub_attr = _esc_attr(subtitle)
        # Inner HTML: name<div style="font-size: 13px;">subtitle</div>
        # In an mxCell label, this gets escaped into &amp;lt; etc.
        label = f"{label}&lt;div style=&quot;font-size: 13px;&quot;&gt;{sub_attr}&lt;/div&gt;"
    return label


def _port_cell(
    port_id: int,
    parent_id: int,
    name: str,
    y: int,
    width: int,
    align: str = "left",
    style_override: str | None = None,
) -> str:
    """Generate XML for one port cell."""
    style = style_override or _port_style(align)
    return (
        f'<UserObject label="{_esc_attr(name)}" tags="" id="{port_id}">'
        f'<mxCell style="{style}" vertex="1" parent="{parent_id}">'
        f'<mxGeometry y="{y}" width="{width}" height="{DEFAULT_PORT_HEIGHT}" as="geometry"/>'
        f'</mxCell></UserObject>'
    )


def build_device_xml(spec: dict) -> tuple[str, int, int]:
    """Build the inner <mxGraphModel>...</mxGraphModel> XML for one device.

    Returns (xml_string, width, height).

    spec keys:
        title           — short title shown on library tile (required)
        name            — main chassis label (defaults to title)
        subtitle        — small label below name (optional)
        tags            — list of draw.io tag strings (optional)
        width           — chassis width in px (default 140)
        info_row        — bool, include "Info: " row (default True)
        loose_ports     — list[str], unstyled ports above input swimlane
        inputs          — list[str] | list[dict], green swimlane
        outputs         — list[str] | list[dict], orange swimlane
        control         — list[str] | list[dict], blue swimlane (optional)

    Each port can be a string (just the name) or a dict with at least
    {"name": "..."} and optional keys passed through to extend the cell.
    """
    title = spec["title"]
    name = spec.get("name", title)
    subtitle = spec.get("subtitle")
    tags = spec.get("tags", [])
    width = spec.get("width", DEFAULT_WIDTH)
    info_row = spec.get("info_row", True)
    loose_ports = spec.get("loose_ports", []) or []
    inputs = spec.get("inputs", []) or []
    outputs = spec.get("outputs", []) or []
    control = spec.get("control", []) or []

    tags_attr = _esc_attr(" ".join(tags)) if tags else ""

    # Layout: stack everything top-to-bottom.
    # Chassis header is HEADER_HEIGHT (40) — drawn by the swimlane itself.
    # Children are positioned with y starting at HEADER_HEIGHT (40).

    parts: list[str] = []
    next_id = 2
    chassis_id = 2
    parent_id = 1

    # Reserve chassis cell — emit later once we know total height
    # We'll fill in geometry at the end.
    chassis_geom_placeholder = "__CHASSIS_GEOM__"

    label_html = _make_label(name, subtitle)
    parts.append(
        f'<UserObject label="{label_html}" tags="{tags_attr}" id="{chassis_id}">'
        f'<mxCell style="{_CHASSIS_STYLE}" vertex="1" parent="{parent_id}">'
        f'{chassis_geom_placeholder}'
        f'</mxCell></UserObject>'
    )
    next_id = 3

    y_cursor = HEADER_HEIGHT  # children start at 40 (after chassis header)

    # 1. Info row
    if info_row:
        info_id = next_id
        next_id += 1
        parts.append(
            f'<UserObject label="Info: " tags="" id="{info_id}">'
            f'<mxCell style="{_INFO_STYLE}" vertex="1" parent="{chassis_id}">'
            f'<mxGeometry y="{y_cursor}" width="{width}" height="{DEFAULT_PORT_HEIGHT}" as="geometry"/>'
            f'</mxCell></UserObject>'
        )
        y_cursor += DEFAULT_PORT_HEIGHT

    # 2. Loose ports (utility cells outside any swimlane)
    for port in loose_ports:
        port_name = port if isinstance(port, str) else port["name"]
        loose_id = next_id
        next_id += 1
        parts.append(
            _port_cell(
                loose_id, chassis_id, port_name, y_cursor, width,
                style_override=_LOOSE_PORT_STYLE,
            )
        )
        y_cursor += DEFAULT_PORT_HEIGHT

    # 3. Inputs swimlane
    if inputs:
        section_id = next_id
        next_id += 1
        section_h = SECTION_HEADER_HEIGHT + (len(inputs) * DEFAULT_PORT_HEIGHT)
        parts.append(
            f'<UserObject label="Input" tags="" id="{section_id}">'
            f'<mxCell style="{_section_style(INPUTS_FILL)}" vertex="1" parent="{chassis_id}">'
            f'<mxGeometry y="{y_cursor}" width="{width}" height="{section_h}" as="geometry"/>'
            f'</mxCell></UserObject>'
        )
        port_y = SECTION_HEADER_HEIGHT
        for port in inputs:
            port_name = port if isinstance(port, str) else port["name"]
            port_id = next_id
            next_id += 1
            parts.append(
                _port_cell(port_id, section_id, port_name, port_y, width, align="left")
            )
            port_y += DEFAULT_PORT_HEIGHT
        y_cursor += section_h

    # 4. Outputs swimlane
    if outputs:
        section_id = next_id
        next_id += 1
        section_h = SECTION_HEADER_HEIGHT + (len(outputs) * DEFAULT_PORT_HEIGHT)
        parts.append(
            f'<UserObject label="Output" tags="" id="{section_id}">'
            f'<mxCell style="{_section_style(OUTPUTS_FILL)}" vertex="1" parent="{chassis_id}">'
            f'<mxGeometry y="{y_cursor}" width="{width}" height="{section_h}" as="geometry"/>'
            f'</mxCell></UserObject>'
        )
        port_y = SECTION_HEADER_HEIGHT
        for port in outputs:
            port_name = port if isinstance(port, str) else port["name"]
            port_id = next_id
            next_id += 1
            parts.append(
                _port_cell(port_id, section_id, port_name, port_y, width, align="right")
            )
            port_y += DEFAULT_PORT_HEIGHT
        y_cursor += section_h

    # 5. Control swimlane
    if control:
        section_id = next_id
        next_id += 1
        section_h = SECTION_HEADER_HEIGHT + (len(control) * DEFAULT_PORT_HEIGHT)
        parts.append(
            f'<UserObject label="Control" tags="" id="{section_id}">'
            f'<mxCell style="{_section_style(CONTROL_FILL)}" vertex="1" parent="{chassis_id}">'
            f'<mxGeometry y="{y_cursor}" width="{width}" height="{section_h}" as="geometry"/>'
            f'</mxCell></UserObject>'
        )
        port_y = SECTION_HEADER_HEIGHT
        for port in control:
            port_name = port if isinstance(port, str) else port["name"]
            port_id = next_id
            next_id += 1
            parts.append(
                _port_cell(port_id, section_id, port_name, port_y, width, align="left")
            )
            port_y += DEFAULT_PORT_HEIGHT
        y_cursor += section_h

    total_h = y_cursor

    # Backfill chassis geometry now we know total height
    chassis_geom = (
        f'<mxGeometry width="{width}" height="{total_h}" as="geometry">'
        f'<mxRectangle x="380" y="243" width="120" height="40" as="alternateBounds"/>'
        f'</mxGeometry>'
    )
    inner = "".join(parts).replace(chassis_geom_placeholder, chassis_geom, 1)

    xml = (
        '<mxGraphModel><root>'
        '<mxCell id="0"/>'
        '<mxCell id="1" parent="0"/>'
        f'{inner}'
        '</root></mxGraphModel>'
    )
    return xml, width, total_h


# ---------------------------------------------------------------------------
# Library file packaging
# ---------------------------------------------------------------------------

def build_library_file(specs: list[dict]) -> str:
    """Build a complete .xml library file content from a list of device specs."""
    entries = []
    for spec in specs:
        xml, w, h = build_device_xml(spec)
        # The library format wants the inner XML HTML-escaped inside JSON
        entries.append(
            {
                "xml": html.escape(xml, quote=False),
                "w": w,
                "h": h,
                "aspect": "fixed",
                "title": spec["title"],
            }
        )
    body = json.dumps(entries, indent=2, ensure_ascii=False)
    return f"<mxlibrary>{body}</mxlibrary>\n"


def write_library(path: str | Path, specs: list[dict]) -> Path:
    """Build and write a library file to disk."""
    path = Path(path)
    path.write_text(build_library_file(specs), encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Library file parsing (for composing diagrams)
# ---------------------------------------------------------------------------

@dataclass
class ParsedPort:
    """A single port on a parsed device."""
    name: str
    section: str  # "loose" | "inputs" | "outputs" | "control" | "info"
    local_id: int  # ID within the device's own mxGraphModel
    y: int  # absolute y-offset within the chassis (for layout reference)


@dataclass
class ParsedDevice:
    """A device parsed from an existing library file."""
    title: str
    width: int
    height: int
    inner_xml: str  # the original (un-escaped) <mxGraphModel> content
    chassis_label: str
    tags: list[str]
    ports: list[ParsedPort] = field(default_factory=list)

    def find_port(self, name: str) -> ParsedPort | None:
        """Case-insensitive port lookup, fuzzy-tolerant."""
        target = re.sub(r"\s+", "", name.lower())
        for p in self.ports:
            candidate = re.sub(r"\s+", "", p.name.lower())
            if candidate == target:
                return p
        # Fall back to substring match
        for p in self.ports:
            candidate = re.sub(r"\s+", "", p.name.lower())
            if target in candidate or candidate in target:
                return p
        return None


def _strip_html(s: str) -> str:
    """Strip HTML tags from a label and unescape entities."""
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def parse_library_file(path: str | Path) -> list[ParsedDevice]:
    """Parse an existing draw.io library file into ParsedDevice objects."""
    path = Path(path)
    text = path.read_text(encoding="utf-8")

    # Strip <mxlibrary> wrapper, parse JSON
    inner = text.strip()
    if inner.startswith("<mxlibrary>"):
        inner = inner[len("<mxlibrary>"):]
    if inner.endswith("</mxlibrary>"):
        inner = inner[: -len("</mxlibrary>")]
    entries = json.loads(inner)

    devices: list[ParsedDevice] = []
    for entry in entries:
        raw_xml = html.unescape(entry["xml"])
        parsed = _parse_device_xml(raw_xml, entry.get("title", ""))
        parsed.width = entry["w"]
        parsed.height = entry["h"]
        devices.append(parsed)
    return devices


def _parse_device_xml(xml: str, title: str) -> ParsedDevice:
    """Parse one device's mxGraphModel XML into structured ports."""
    root = ET.fromstring(xml)
    cells_by_id: dict[str, ET.Element] = {}
    for elem in root.iter():
        cell_id = elem.get("id")
        if cell_id:
            cells_by_id[cell_id] = elem

    # Find chassis (the swimlane that's a direct child of cell id=1)
    chassis: ET.Element | None = None
    for elem in root.iter("UserObject"):
        mx = elem.find("mxCell")
        if mx is not None and mx.get("parent") == "1":
            chassis = elem
            break
    if chassis is None:
        # Fall back: maybe direct mxCell parent=1 that's a swimlane
        for elem in root.iter("mxCell"):
            if elem.get("parent") == "1" and "swimlane" in (elem.get("style") or ""):
                # Wrap in synthetic UserObject for consistent handling
                chassis = elem  # type: ignore
                break

    chassis_label = _strip_html(chassis.get("label", "")) if chassis is not None else ""
    tags = (chassis.get("tags", "") or "").split() if chassis is not None else []
    chassis_id = chassis.get("id") if chassis is not None else None

    ports: list[ParsedPort] = []
    # Children of chassis: info row, loose ports, section swimlanes
    section_lookup: dict[str, str] = {}  # section_id -> section name
    for elem in root.iter("UserObject"):
        mx = elem.find("mxCell")
        if mx is None:
            continue
        if mx.get("parent") != chassis_id:
            continue
        label = _strip_html(elem.get("label", ""))
        style = mx.get("style", "")
        elem_id = elem.get("id", "")
        if "swimlane" in style and label.lower() in {"input", "output", "control"}:
            section_lookup[elem_id] = label.lower() + "s" if not label.lower().endswith("s") else label.lower()
        else:
            # Either info row or loose port
            section = "info" if label.lower().startswith("info") else "loose"
            geom = mx.find("mxGeometry")
            y = int(geom.get("y", "0")) if geom is not None else 0
            ports.append(
                ParsedPort(name=label, section=section, local_id=int(elem_id), y=y)
            )

    # Now walk into each section swimlane and pull out ports
    for sec_id, sec_name in section_lookup.items():
        for elem in root.iter("UserObject"):
            mx = elem.find("mxCell")
            if mx is None or mx.get("parent") != sec_id:
                continue
            label = _strip_html(elem.get("label", ""))
            geom = mx.find("mxGeometry")
            y = int(geom.get("y", "0")) if geom is not None else 0
            ports.append(
                ParsedPort(
                    name=label,
                    section=sec_name.rstrip("s") + "s",  # normalise
                    local_id=int(elem.get("id", "0")),
                    y=y,
                )
            )

    return ParsedDevice(
        title=title,
        width=0,  # filled in by caller
        height=0,
        inner_xml=xml,
        chassis_label=chassis_label,
        tags=tags,
        ports=ports,
    )


# ---------------------------------------------------------------------------
# Instantiation (placing a device on a diagram canvas)
# ---------------------------------------------------------------------------

def instantiate_device(
    parsed: ParsedDevice,
    x: int,
    y: int,
    id_prefix: str,
) -> tuple[str, dict[str, str]]:
    """Place a parsed device on the diagram canvas at (x, y).

    Returns (xml_fragment, port_id_index) where:
        - xml_fragment is the device's mxCell tree with prefixed IDs and
          chassis positioned at (x, y).
        - port_id_index maps "Port Name" -> globally unique mxCell id (string),
          for use in mxEdge source/target attributes.
    """
    # Re-parse to get a tree we can mutate
    root = ET.fromstring(parsed.inner_xml)

    # Mapping from old id -> new prefixed id
    id_map: dict[str, str] = {}
    for elem in root.iter():
        old_id = elem.get("id")
        if old_id is None:
            continue
        # Keep the structural cells 0 and 1 unique-but-not-conflicting:
        # we want them to NOT appear in the final composition (we already
        # have id=0 and id=1 in the canvas root). Strip them and reparent.
        if old_id in {"0", "1"}:
            continue
        new_id = f"{id_prefix}_{old_id}"
        id_map[old_id] = new_id
        elem.set("id", new_id)

    # Update parent references
    for elem in root.iter():
        parent = elem.get("parent")
        if parent and parent in id_map:
            elem.set("parent", id_map[parent])
        elif parent == "1":
            # Reparent chassis (and any other parent=1 elements) to the
            # diagram's root layer, which we'll hardcode as "1" in the
            # composed canvas.
            elem.set("parent", "1")

    # Position the chassis: find the UserObject with parent=1, set its
    # geometry x/y.
    for uo in root.iter("UserObject"):
        mx = uo.find("mxCell")
        if mx is not None and mx.get("parent") == "1":
            geom = mx.find("mxGeometry")
            if geom is not None:
                geom.set("x", str(x))
                geom.set("y", str(y))
            break

    # Build port id index — chassis label is the device name, ports are
    # named per their parsed labels.
    port_index: dict[str, str] = {}
    for port in parsed.ports:
        old_id_str = str(port.local_id)
        if old_id_str in id_map:
            port_index[port.name] = id_map[old_id_str]

    # Serialise the relevant fragment: everything that was a child of root,
    # excluding cells id=0 and id=1.
    fragments = []
    for child in root.find("root"):
        if child.tag == "mxCell" and child.get("id") in {"0", "1"}:
            continue
        fragments.append(ET.tostring(child, encoding="unicode"))
    return "".join(fragments), port_index


# ---------------------------------------------------------------------------
# CLI helpers
# ---------------------------------------------------------------------------

def summarise_library(path: str | Path) -> str:
    """Return a human-readable summary of a library file."""
    devices = parse_library_file(path)
    lines = [f"Library: {Path(path).name}  ({len(devices)} devices)"]
    for d in devices:
        lines.append(f"  • {d.title}  ({d.width}×{d.height}px, tags: {' '.join(d.tags) or '—'})")
        for section in ("inputs", "outputs", "control", "loose", "info"):
            sec_ports = [p for p in d.ports if p.section == section]
            if not sec_ports:
                continue
            names = ", ".join(p.name for p in sec_ports)
            lines.append(f"      {section:<8} {names}")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: library_io.py summarise <path-to-library.xml>")
        raise SystemExit(1)
    cmd = sys.argv[1]
    if cmd == "summarise":
        print(summarise_library(sys.argv[2]))
    else:
        print(f"Unknown command: {cmd}")
        raise SystemExit(1)
