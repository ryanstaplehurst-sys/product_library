---
name: insert-drawio-signal-flow
description: Compose draw.io signal-flow diagrams for Insert Productions jobs from free-form briefs, using a curated library of AV equipment shapes and a consistent cable-style convention. Use this skill whenever Ryan describes a signal flow, system design, patch plan, rack patch, or "draw me a diagram of …" in conversation — including pasted briefs from PMs that name kit ("ATEM 2 M/E feeds Tessera SX40 via Videohub"), describe a flow ("camera 1 to switcher to LED wall"), or ask for a system schematic. Trigger eagerly — any request that mixes equipment names with the words diagram, schematic, signal flow, patch, plan, route, feed, or "to" + "from" almost certainly wants this skill. Output is a `.drawio` file the team opens in draw.io to review and tweak. Do NOT trigger for LED panel cable maps (use insert-led-mapper) or Excalidraw whiteboard sketches.
---

# Insert Productions — Draw.io Signal Flow Diagrams

Compose `.drawio` diagrams of AV signal flows by translating Ryan's free-form briefs into a structured spec, then running the composer against a curated library of manufacturer device shapes.

## Repo layout

```
insert-drawio-signal-flow/
├── libraries/              ← .xml files loaded into draw.io as Custom Libraries
│   ├── _cables.xml         (cable style reference — drag a cable, get the right colour/dash)
│   ├── blackmagic.xml
│   ├── brompton.xml
│   ├── novastar.xml
│   └── …
├── sources/                ← Python device specs that build each library
│   ├── _cables.py
│   ├── brompton.py
│   ├── novastar.py
│   └── …
├── scripts/
│   ├── library_io.py       ← parser + builder (used by every source)
│   ├── cable_styles.py     ← single source of truth for cable conventions
│   └── compose_diagram.py  ← spec → .drawio
└── reference/
    └── cable_conventions.md
```

## How to compose a diagram from a brief

When Ryan describes a signal flow, do this:

1. **Identify devices.** Map every named piece of kit to a `library` + `title`. If you can't find an exact match, run `python3 scripts/library_io.py summarise libraries/<lib>.xml` to inspect available titles, or fall back to a sensible substitute and mention what you swapped.
2. **Identify connections.** For each "X to Y" / "X feeds Y" / "X out → Y in" in the brief, write a connection entry. Use the actual port names from the library — when in doubt, summarise the device's library entry and pick the closest match.
3. **Choose cable types.** Use `cable_styles.classify_cable()` mentally — SDI defaults to `sdi`, fibre adds `_fibre` suffix, control is `network`, etc. See `reference/cable_conventions.md`.
4. **Build the spec** as JSON (schema below), write to `/tmp/spec.json`.
5. **Run the composer**:
   ```bash
   python3 scripts/compose_diagram.py \
       --spec /tmp/spec.json \
       --output /mnt/user-data/outputs/<JOBNAME>_signal_flow.drawio
   ```
6. **Deliver** with `present_files`. Ryan opens the `.drawio` in his desktop draw.io, tweaks, exports if needed.

## Spec schema

```json
{
  "title": "Studio A — camera routing",
  "page_width": 1700,
  "page_height": 1100,
  "title_block": true,
  "legend": true,
  "devices": [
    {
      "id":      "atem",                "// required, used in connections",
      "library": "blackmagic",          "// required, .xml filename without extension",
      "title":   "atem 2/me",           "// required, matches the library tile",
      "x":       100,                    "// optional — auto-placed if omitted",
      "y":       120,                    "// optional",
      "label_override": "ATEM 2 M/E (FOH)" "// optional"
    }
  ],
  "connections": [
    {
      "from":  "device_id.Port Name",
      "to":    "device_id.Port Name",
      "cable": "sdi",                    "// see cable_styles.CABLE_STYLES keys + aliases",
      "label": "PGM"                     "// optional edge label"
    }
  ]
}
```

### Port name matching

The composer matches ports case-insensitively and falls back to substring match. Don't worry about getting capitalisation perfect — `"sdi 1"` will find `"SDI 1 (12G)"`. If the match is ambiguous it picks the first hit; if it can't find one at all it raises a clear error listing all available ports on that device.

### Cable hints

Cable values can be canonical keys (`sdi`, `network`, `dante`) or free hints (`12G-SDI`, `Cat6`, `audio over IP`). The classifier resolves them to the canonical style. Anything unrecognised falls back to a plain solid black line — that's intentional, not a bug. An unstyled cable is a flag for Ryan to clarify, not Claude's guess.

See `reference/cable_conventions.md` for the full table.

## Building or updating a library

To add a device to an existing manufacturer library:

1. Open `sources/<manufacturer>.py`
2. Append a dict to `DEVICES` — see Brompton/Novastar for examples
3. Run `python3 sources/<manufacturer>.py` — overwrites `libraries/<manufacturer>.xml`

To add a new manufacturer:

1. Copy `sources/brompton.py` → `sources/<new>.py`
2. Replace device list, change the output path
3. Run it

The schema for one device:

```python
{
    "title":      "tessera SX40",          # short id shown on the library tile
    "name":       "Brompton Tessera SX40", # bold name on the chassis
    "subtitle":   "4K LED Processor",      # smaller text below the name
    "tags":       ["LED", "Processor"],    # space-separated draw.io filter tags
    "width":      160,                      # default 140
    "info_row":   True,                     # default True
    "loose_ports": ["IP:", "Genlock In"],   # text cells outside swimlanes
    "inputs":      ["SDI 1", "SDI 2", …],   # green swimlane
    "outputs":     ["DATA A", "DATA B"],     # orange swimlane
    "control":     ["Network", "USB"]        # blue swimlane (optional)
}
```

## Loading libraries in draw.io

Once Ryan has the repo cloned, in draw.io desktop or web:
**File → Open Library → choose `libraries/<file>.xml`**

The library appears as a panel on the left. Drag any device onto a canvas; ports stay live as connection anchors.

## Diagram conventions

- **Signal flow runs left → right.** Sources (cameras, playback) on the left, processing in the middle, destinations (LED walls, projectors, recorders) on the right.
- **Chassis colours:** light grey body, green input swimlane, orange output swimlane, blue control swimlane. These are draw.io defaults and match the existing Blackmagic library.
- **Title block** is black with white text, red rule beneath — Insert brand cue without overwhelming the technical content.
- **Legend** appears below the bottom-most device, scoped to only the cable styles actually used in the diagram.

## Common pitfalls

- **Port names with parentheses** — `"SDI 1 (12G)"` works fine in JSON, but if the brief says "SDI 1" Claude should use the full library port name in the spec, not invent a shortened version.
- **"PGM" is not a port** — it's a label. The actual ATEM PGM ports are `"PGM ME1"`, `"PGM ME2"`, etc. Always summarise the device first if unsure.
- **Auto-layout is dumb.** It places devices left-to-right in declaration order, 4 per row. For complex diagrams with branching paths, write explicit `x`/`y` for each device — or accept that Ryan will adjust in draw.io.
- **Don't HTML-escape inside the spec JSON.** Let the composer handle escaping. Just write `"label": "PGM & AUX"`, not `"label": "PGM &amp; AUX"`.

## When to choose this skill vs others

- **Signal flow / patch / system schematic** → this skill.
- **LED panel-by-panel data + power cable map** → `insert-led-mapper`.
- **Stage / venue / floor plan** → not yet covered. Use draw.io directly or sketch in Excalidraw.
- **Quick doodle to talk through an idea** → Excalidraw.
