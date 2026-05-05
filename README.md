# Insert Productions — Draw.io Signal Flow Libraries

A curated set of draw.io shape libraries for AV equipment, plus a Python toolkit that lets Claude compose `.drawio` signal-flow diagrams from free-form briefs.

## What's in here

- **`libraries/`** — `.xml` files you load into draw.io as Custom Libraries (File → Open Library). Each file is one manufacturer + a special `_cables.xml` with styled cable templates.
- **`sources/`** — Python device specs that build each library. Edit a spec, run `python3 sources/<file>.py`, and the matching `libraries/<file>.xml` regenerates.
- **`scripts/`** — the engine: `library_io.py` parses/builds, `compose_diagram.py` turns a JSON spec into a `.drawio` file, `cable_styles.py` is the single source of truth for the cable convention.
- **`reference/cable_conventions.md`** — the cable colour/line/width legend in human-readable form.
- **`SKILL.md`** — instructions for Claude.

## Loading a library in draw.io

1. Open draw.io (desktop or app.diagrams.net).
2. **File → Open Library → choose `libraries/<manufacturer>.xml`**.
3. The library appears as a panel on the left. Drag any device onto the canvas.

Repeat for `_cables.xml` to get pre-styled edge templates you can drop between ports.

## Adding a device

1. Open `sources/<manufacturer>.py`.
2. Append a new dict to `DEVICES`:

```python
{
    "title":      "tessera SX40",
    "name":       "Brompton Tessera SX40",
    "subtitle":   "4K LED Processor",
    "tags":       ["LED", "Processor"],
    "width":      160,
    "loose_ports": ["IP:", "Genlock In"],
    "inputs":      ["SDI 1 (12G)", "SDI 2 (12G)", …],
    "outputs":     ["DATA A (10G)", "DATA B (10G)"],
    "control":     ["Network", "USB"],
}
```

3. Run `python3 sources/<manufacturer>.py`. The matching `.xml` file regenerates.

## Cable convention (quick reference)

Colour = signal type, line style = transport (solid copper, dashed fibre, dotted wireless), width = criticality. See `reference/cable_conventions.md` for the full table.

| Type | Colour | Notes |
|---|---|---|
| SDI | yellow | dashed if over fibre |
| HDMI / DP | purple | |
| IP video (NDI / 2110) | blue | dashed if over fibre |
| LED data (Cat6 / 10G) | dark green | dashed if over fibre |
| AES3 / MADI / Dante | mid green | dashed for Dante |
| Analog audio | pink | |
| DMX / sACN | magenta | |
| LTC / Genlock | orange | dashed for genlock |
| Network / Control | thin grey | |
| Power 13/16A | thick black | |
| Power 32A 3ph | thick red | |

## Building all libraries from scratch

```bash
for f in sources/*.py; do python3 "$f"; done
```

## Composing a diagram

```bash
python3 scripts/compose_diagram.py \
    --spec /path/to/spec.json \
    --output /path/to/output.drawio
```

See `SKILL.md` for the spec format.

## Manufacturer coverage

- ✅ Blackmagic (seeded from the existing community library)
- ✅ Brompton — Tessera SX40, S8, M2, T1, XD
- ✅ Novastar — MCTRL4K, MCTRL R5, MX40 Pro, MX2000 Pro, H9, NovaPro UHD Jr, CVT 10
- ⏳ Roland, Yamaha, Allen & Heath, Shure, Sennheiser, AJA, Decimator, Sony, Panasonic, NewTek, Disguise, Resolume

## Licence

Internal Insert Productions tool. Device specs are derived from manufacturer-published port lists; if you redistribute, check trademark guidance for each manufacturer.
