# Insert Productions — Draw.io Signal Flow Libraries

A curated set of draw.io shape libraries for the AV equipment Insert Productions actually rents, plus a Python toolkit that lets Claude compose `.drawio` signal-flow diagrams from free-form briefs.

**27 libraries · ~218 device shapes · Insert's full April 2026 rental list covered.**

See [`coverage_status.md`](coverage_status.md) for the up-to-date inventory.

## What's in here

- **`libraries/`** — `.xml` files you load into draw.io as Custom Libraries (File → Open Library). Most are per-manufacturer (`yamaha.xml`, `sennheiser.xml`); a few are thematic groupings of single-device-per-vendor kit (`audio-other.xml`, `displays.xml`, `comms.xml`, `network.xml`, `playback.xml`, `cameras.xml`, `mics.xml`, `extenders.xml`, `dj-kit.xml`, `led-panels.xml`, `touchscreens.xml`, `computers.xml`).
- **`sources/`** — Python device specs that build each library. Edit a spec, run `python3 sources/<file>.py`, the matching `libraries/<file>.xml` regenerates.
- **`scripts/`** — the engine: `library_io.py` parses/builds libraries, `compose_diagram.py` turns a JSON spec into a `.drawio` file, `cable_styles.py` is the single source of truth for the cable convention, `build_all.py` rebuilds everything.
- **`reference/cable_conventions.md`** — the cable colour/line/width legend in human-readable form.
- **`coverage_status.md`** — running tracker of what kit is in the libraries vs the rental list.
- **`SKILL.md`** — instructions for Claude.

## Loading libraries in draw.io

For project managers and the rest of the team, see the [Signal Flow User Guide PDF](https://drive.google.com/) (in the technical team's shared drive) for the friendlier walkthrough.

The short version:

1. Click the green **Code** button at the top of this repo → **Download ZIP**. Extract somewhere sensible.
2. Open draw.io (desktop or app.diagrams.net).
3. **File → Open Library from File…** → navigate into the `libraries/` folder → select all 27 `.xml` files (Cmd+A or Ctrl+A) → Open.
4. Libraries appear in the left panel. Drag any device onto the canvas.

`_cables.xml` contains pre-styled edge templates you can drop between ports for the cable convention.

## Composing a diagram via Claude

If you have the `insert-drawio-signal-flow` skill installed in claude.ai, just describe the flow in plain English ("ATEM 2 M/E feeds two SX40s via Videohub, with confidence returns to FOH") and Claude returns a `.drawio` file. See `SKILL.md` for the full spec the skill speaks under the hood.

## Composing a diagram from the CLI

```bash
python3 scripts/compose_diagram.py \
    --spec /path/to/spec.json \
    --output /path/to/output.drawio
```

Spec format:

```json
{
  "title": "Studio A — camera routing",
  "title_block": true,
  "legend": true,
  "devices": [
    { "id": "atem", "library": "blackmagic", "title": "atem 2/me" },
    { "id": "sx40", "library": "brompton",   "title": "tessera SX40" }
  ],
  "connections": [
    { "from": "atem.PGM ME1", "to": "sx40.SDI 1 (12G)", "cable": "sdi" }
  ]
}
```

## Adding a device

1. Open the relevant `sources/<file>.py` (or create a new one — copy the structure from `brompton.py`).
2. Append a new dict to `DEVICES`:

   ```python
   {
       "title":      "v-1200hd",
       "name":       "Roland V-1200HD",
       "subtitle":   "Multi-format Switcher",
       "tags":       ["Switcher", "Video"],
       "width":      160,
       "loose_ports": ["IP:", "Tally"],
       "inputs":     ["SDI 1", "SDI 2", "HDMI 1", "HDMI 2"],
       "outputs":    ["PGM", "PVW", "AUX 1", "AUX 2"],
       "control":    ["LAN", "MIDI"],
   }
   ```

3. Run `python3 sources/<file>.py`. The matching `.xml` regenerates.
4. Commit and push so the team gets the new shape on their next pull.

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
| Wireless RF / IR | grey | dotted |
| USB | light grey | |
| Power 13/16A | thick black | |
| Power 32A 3-phase | thick red | |

## Building all libraries from scratch

```bash
for f in sources/*.py; do python3 "$f"; done
```

Or:

```bash
python3 scripts/build_all.py
```

## Library coverage

| File | Devices | Notes |
|---|---|---|
| `_cables.xml` | 18 | Cable convention edge templates |
| `blackmagic.xml` | 25 | Community-sourced |
| `brompton.xml` | 5 | Tessera SX40, S8, M2, T1, XD |
| `novastar.xml` | 14 | MCTRL/MX/VX/H series + CVT |
| `yamaha.xml` | 4 | QL1, DM3, DXR12, MSP3 |
| `allen-heath.xml` | 4 | SQ5, CQ-12T, DX168, Zedi 10 |
| `sennheiser.xml` | 12 | EW-DX, EW-D, EM 300-500 G4, beltpacks/handhelds, IEM, MAT 153-S |
| `shure.xml` | 2 | MX412, SM58 |
| `midas.xml` | 1 | DL32 stagebox |
| `aja.xml` | 2 | 1×6 SDI DA, C10DA |
| `decimator.xml` | 2 | MD-HX, MD-Cross v3 |
| `kramer.xml` | 2 | VM-4H2 1:2, 1:4 |
| `barco.xml` | 3 | E2 4K, S3 4K Gen 2, PDS 4K |
| `dnb.xml` | 10 | D12/D20/D40/D80 amps + E8/M4/T10/V-Sub/Y10P/Y7P |
| `audio-other.xml` | 16 | QSC, BSS, Behringer, Tascam, Sonifex, Sonos, Bose, LD, Lynx, RED, Pioneer DM-40D |
| `mics.xml` | 5 | DPA, Rode, generic lapel/BT lapel |
| `dj-kit.xml` | 3 | CDJ-3000, DJM-A9, DJ Kit bundle |
| `network.xml` | 21 | DrayTek, Netgear, TP-Link, Ubiquiti |
| `displays.xml` | 22 | Samsung TVs (24-98"), HP, IIYAMA, Lenovo |
| `touchscreens.xml` | 9 | IIYAMA Prolite touch (15-75") |
| `led-panels.xml` | 11 | Absen, Aluvision, BeMatrix, LedSkin, Unilumin, generic 3.9mm |
| `cameras.xml` | 5 | Canon, Lumix, Sony, Logitech, BirdDog |
| `playback.xml` | 8 | BrightSign, Apple TV, Pro Signal, Sprite, Mac Studio, vMix/Pixera workstation |
| `comms.xml` | 13 | GreenGo, Motorola, EarTech, Interspace cueing |
| `extenders.xml` | 6 | LINDY, Neoteck, generic HDMI 3:1, Pro Signal 4×4, Datapath FX4/H |
| `elgato.xml` | 3 | Streamdeck Mini, XL, HD60 Pro |
| `computers.xml` | 13 | MacBook variants, Lenovo Legion, MSI, Intel NUC |

## Out of scope

Cables, adapters, power, brackets, mounts, stands, packaging, ladders, batteries, chargers, antennas without active electronics, software licences, sub-rent placeholders, lighting fixtures (different domain — DMX universes belong in their own skill).

## Licence

Internal Insert Productions tool. Device specs are derived from manufacturer-published port lists; if you redistribute, check trademark guidance for each manufacturer.
