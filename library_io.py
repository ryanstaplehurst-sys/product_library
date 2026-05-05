# Insert Productions — Cable Convention Reference

Every line on a signal-flow diagram should communicate three things at a glance: **what kind of signal**, **how it's transported**, and **how critical it is**. We use a consistent visual language across all diagrams so technicians don't have to read every label.

## The three axes

| Axis | What it encodes | How it's drawn |
|---|---|---|
| **Colour** | Signal type | hex stroke colour |
| **Line style** | Transport | solid (copper), dashed (fibre), dotted (wireless) |
| **Width** | Criticality | thin (control, ~1.0px), normal (signal, ~1.5–1.8px), thick (power, ~3.0px) |

When in doubt, use a normal-width solid black line. An unstyled cable is a clear flag to clarify, not a guess.

## The full table

| Cable | Colour | Style | Width | Aliases the parser accepts |
|---|---|---|---|---|
| **SDI (copper)** | `#E5C100` yellow | solid | 1.8 | sdi, 3g-sdi, 12g-sdi, hd-sdi, bnc |
| **SDI over fibre / SMPTE** | `#E5C100` yellow | dashed | 1.8 | smpte, sdi fibre, fibre sdi |
| **HDMI / DisplayPort / DVI** | `#7F3FBF` purple | solid | 1.8 | hdmi, dp, displayport, dvi |
| **IP video (NDI / ST 2110 / SRT)** | `#1F6FEB` blue | solid | 1.8 | ndi, st2110, 2110, ip video, srt |
| **IP video over fibre** | `#1F6FEB` blue | dashed | 1.8 | 10g fibre, ip fibre |
| **LED data (Cat6 / 10G)** | `#0A6E5A` dark green | solid | 2.0 | data, led data, tessera data, cat6 led |
| **LED data over fibre** | `#0A6E5A` dark green | dashed | 2.0 | led fibre, data fibre |
| **Analog audio** | `#E91E63` pink | solid | 1.5 | xlr, trs, line, mic, analog audio |
| **AES3 / MADI** | `#2E7D32` mid green | solid | 1.5 | aes, aes3, aes/ebu, madi |
| **Dante / AoIP** | `#2E7D32` mid green | dashed | 1.5 | dante, aoip, ravenna |
| **DMX / sACN / Art-Net** | `#C2185B` magenta | solid | 1.5 | dmx, sacn, artnet, art-net |
| **Timecode (LTC)** | `#F57C00` orange | solid | 1.5 | ltc, timecode, tc |
| **Genlock / Reference** | `#F57C00` orange | dashed | 1.5 | genlock, ref, blackburst, tri-level |
| **Network / Control (Cat5/6)** | `#666666` grey | solid | 1.0 | network, ethernet, cat5, cat6, control, rj45 |
| **Wireless RF / IR** | `#666666` grey | dotted | 1.0 | wireless, rf, ir, antenna |
| **USB / Thunderbolt** | `#9E9E9E` light grey | solid | 1.0 | usb, usb-c, thunderbolt |
| **Mains 13/16A single phase** | `#000000` black | solid | 3.0 | 13a, 16a, mains, iec, powercon |
| **Mains 32A 3-phase** | `#D32F2F` red | solid | 3.0 | 32a, 63a, 3-phase, ceeform |

## Rationales worth pinning

- **Yellow for SDI** matches industry yellow-BNC visual cue.
- **LED data is its own dark green**, not the same green as digital audio. They're distinct enough on screen to never confuse, and LED data appears so often in our work that it earns its own colour.
- **Genlock and timecode share orange** — both are reference signals on the same site. Solid for LTC, dashed for genlock so they're distinguishable when both appear in one diagram.
- **Magenta for DMX** because pink/red is taken for analog audio. Open to revisiting.
- **Network is thin grey** because it's everywhere and shouldn't visually compete with signal paths. When you need to show a Dante data network, use the Dante style (dashed mid-green) — that's a primary signal path, not control.
- **Wireless dotted grey** — because RF and IR both share the "no physical cable" property, and grey because the carried signal type is what matters more than the link.

## Why we don't use arrowheads

Diagrams are easier to read with directional flow inferred from layout (left → right) and from input vs output port colours (green = in, orange = out). Arrowheads add visual noise on dense diagrams and force the reader to follow individual lines instead of seeing the whole picture. The composer leaves arrows off by default. If a specific diagram benefits from arrows, override the edge style in draw.io directly.

## When to bend the rules

- **Briefs from a client who has their own conventions**: match theirs, note the deviation in the title block.
- **Single-cable type diagrams** (e.g. "show me just the Dante network"): you can drop colour entirely and use line weight to show backbone vs spur. Mention this choice in the legend.
- **Print-only mono output**: line styles still distinguish copper vs fibre vs wireless. Colour information is lost — the compose script doesn't currently auto-substitute, so flag it before exporting.
