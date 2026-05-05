---
name: insert-drawio-signal-flow
description: Compose draw.io signal-flow diagrams for Insert Productions jobs from free-form briefs, using a curated library of AV equipment shapes and a consistent cable-style convention. Use this skill whenever Ryan describes a signal flow, system design, patch plan, rack patch, kit chain, or asks to "draw me a diagram of …" — including pasted briefs from PMs that name kit ("ATEM 2 M/E feeds Tessera SX40 via Videohub"), describe a flow ("camera 1 to switcher to LED wall"), or ask for a system schematic. Trigger eagerly — any request that mixes equipment names with words like diagram, schematic, signal flow, patch, plan, route, feed, or "to/from" almost certainly wants this skill. Output is a `.drawio` file the team opens in draw.io. Do NOT trigger for LED panel data/power cable maps (that's `insert-led-mapper`) or for whiteboard-style sketches (use Excalidraw).
---

# Insert Productions — Draw.io Signal Flow Diagrams

Compose `.drawio` signal-flow diagrams from free-form briefs by translating the brief into a structured spec, then running the composer against this skill's curated equipment libraries.

## Skill layout

```
/mnt/skills/user/insert-drawio-signal-flow/
├── SKILL.md                                  ← this file
├── README.md                                 ← repo-level overview
├── libraries/                                ← .xml shape libraries
│   ├── _cables.xml                           ← edge-style templates
│   ├── blackmagic.xml                        ← community-sourced
│   ├── brompton.xml                          ← Tessera processors
│   └── novastar.xml                          ← Novastar processors
├── sources/                                  ← Python specs that build each library
│   ├── _cables.py
│   ├── brompton.py
│   └── novastar.py
├── scripts/
│   ├── library_io.py                         ← parser + builder engine
│   ├── cable_styles.py                       ← cable convention single source of truth
│   ├── compose_diagram.py                    ← spec → .drawio
│   └── build_all.py                          ← rebuild every library
├── reference/
│   └── cable_conventions.md                  ← human-readable convention table
└── examples/
    ├── sample_spec.json
    └── sample_diagram.drawio
```

## When invoked, do this

### 1. Inspect available kit

If unsure what's in a library, summarise it first:

```bash
python3 /mnt/skills/user/insert-drawio-signal-flow/scripts/library_io.py summarise \
    /mnt/skills/user/insert-drawio-signal-flow/libraries/<lib>.xml
```

Returns titles + every port (inputs / outputs / control / loose / info) per device. Use this to (a) pick the right device for the brief, and (b) match port names exactly when writing the spec — the composer is forgiving but exact matches are best.

### 2. Build the spec

Translate the brief into JSON. Spec format:

```json
{
  "title": "Studio A — camera routing",
  "page_width": 1700,
  "page_height": 1100,
  "title_block": true,
  "legend": true,
  "devices": [
    {
      "id":      "atem",
      "library": "blackmagic",
      "title":   "atem 2/me",
      "x":       100,
      "y":       120
    }
  ],
  "connections": [
    {
      "from":  "atem.PGM ME1",
      "to":    "sx40.SDI 1 (12G)",
      "cable": "sdi",
      "label": "PGM"
    }
  ]
}
```

Field rules:

- **`id`** — short identifier you make up; used in `connections`.
- **`library`** — filename without `.xml` (e.g. `brompton`, `novastar`, `blackmagic`).
- **`title`** — must match a device title in that library (case-insensitive, substring tolerant).
- **`x` / `y`** — optional. If omitted, the composer auto-places left-to-right in declaration order.
- **`from` / `to`** — `device_id.Port Name` format. Port name is matched case-insensitively, with substring fallback.
- **`cable`** — one of the keys in `cable_styles.CABLE_STYLES`, OR a free hint (`"12G-SDI"`, `"Cat6"`, `"Dante"`) that the classifier will resolve. Unknown hints fall back to a plain solid black line — that's a deliberate flag, not a bug.

### 3. Run the composer

Save the spec to `/tmp/spec.json`, then:

```bash
python3 /mnt/skills/user/insert-drawio-signal-flow/scripts/compose_diagram.py \
    --spec /tmp/spec.json \
    --output /mnt/user-data/outputs/<JOBNAME>_signal_flow.drawio
```

### 4. Deliver

Use `present_files` with the `.drawio` path. Ryan opens it in draw.io desktop, tweaks layout, exports.

## Signal-flow diagram conventions

- **Layout left → right.** Sources (cameras, playback, mics) on the left, processing (switchers, processors) in the middle, destinations (LED walls, projectors, recorders) on the right.
- **Chassis colours:** light grey body, green input section (`#d5e8d4`), orange output section (`#ffe6cc`), blue control section (`#dae8fc`). These match draw.io defaults and the existing Blackmagic library.
- **Cable colours:** see `reference/cable_conventions.md`. Colour = signal type, dash = transport (solid copper / dashed fibre / dotted wireless), width = criticality.
- **Title block** is black with white text + red rule beneath. Insert brand cue without overwhelming the technical content.
- **Legend** appears below the bottom-most device, scoped to only the cable styles actually used in the diagram.
- **No arrowheads** by default — direction is inferred from layout + green/orange port colours.

## Cable types — quick reference

| Cable | Style key | Colour |
|---|---|---|
| SDI (copper) | `sdi` | yellow |
| SDI over fibre | `sdi_fibre` | yellow dashed |
| HDMI / DisplayPort | `hdmi` | purple |
| IP video (NDI / 2110) | `ip_video` | blue |
| LED data (Cat6 / 10G) | `led_data` | dark green |
| Analog audio | `audio_analog` | pink |
| AES3 / MADI | `aes` | mid green |
| Dante / AoIP | `dante` | mid green dashed |
| DMX / sACN | `dmx` | magenta |
| Timecode (LTC) | `timecode` | orange |
| Genlock / Reference | `genlock` | orange dashed |
| Network / Control | `network` | thin grey |
| Wireless RF / IR | `wireless` | grey dotted |
| USB | `usb` | light grey |
| Mains 13/16A | `power_single` | thick black |
| Mains 32A 3ph | `power_3ph` | thick red |

Free hints work too — `"12G-SDI"` resolves to `sdi`, `"Cat6"` to `network`, `"audio over IP"` to `dante`, etc.

## Common pitfalls — read before composing

- **Port names with parentheses are normal.** `"SDI 1 (12G)"` is the actual Brompton port name. Use the exact library name in the spec, not a shortened version.
- **"PGM" is a label, not a port.** ATEM ports are `"PGM ME1"`, `"PGM ME2"`, etc. Always summarise the device first if unsure.
- **Auto-layout is dumb.** It places devices left-to-right in declaration order, 4 per row. For complex diagrams with branching paths, write explicit `x`/`y` for each device.
- **Don't escape inside the spec JSON.** Write `"label": "PGM & AUX"`, not `"label": "PGM &amp; AUX"`. The composer escapes for you.
- **Camera sources may not have an SDI Out port in the library.** Some devices (e.g. Blackmagic's `microstudiocam 4k`) only expose their tally-return SDI as an input. If the brief routes a camera as a source, either pick a different device or note the gap to Ryan.

## Adding kit on the fly

If Ryan says "add the Roland V-1200HD" and it's not in any library:

1. Open `/mnt/skills/user/insert-drawio-signal-flow/sources/roland.py` (create if missing — copy from `brompton.py`).
2. Append a device dict:
   ```python
   {
       "title":      "v-1200hd",
       "name":       "Roland V-1200HD",
       "subtitle":   "Multi-format Switcher",
       "tags":       ["Switcher", "Video"],
       "width":      160,
       "loose_ports": ["IP:", "Tally"],
       "inputs":      ["SDI 1", "SDI 2", …],
       "outputs":     ["PGM", "PVW", "AUX 1", "AUX 2"],
       "control":     ["LAN", "MIDI"]
   }
   ```
3. Run `python3 /mnt/skills/user/insert-drawio-signal-flow/sources/roland.py` to regenerate `libraries/roland.xml`.
4. Then continue composing.

Note this is a one-shot — the new device only persists if Ryan also commits the change to the source repo (`product_library` on GitHub).

## When to choose this skill vs others

- **Signal flow / patch / system schematic** → this skill.
- **LED panel-by-panel data + power map** → `insert-led-mapper`.
- **Stage / venue / floor plan** → not yet covered.
- **Quick doodle to talk through an idea** → Excalidraw.
- **Production documentation print pack** → `insert-prod-doc-print-pack`.
