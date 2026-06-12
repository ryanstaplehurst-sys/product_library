# Coverage Status

Tracking against the live Current RMS product catalogue. Last full stock sync: **12 June 2026** (full catalogue pull, ~1,760 products incl. sub-rent placeholders → active, signal-flow-relevant kit diffed against every library). Previous baseline: April 2026 rental income export (824 products → 269 signal-flow-relevant).

## Status: synced to Current RMS, June 2026

**29 libraries / ~314 device shapes** (+ 18 cable styles).

June 2026 sync added ~75 shapes: two new libraries (`projectors.xml`, `roland.xml`), legacy serialised kit that never appeared in the income report (Yamaha CL5/QL5/LS9/M7CL + RIOs, Midas M32, d&b Q/B/C-series, Shure ULX-D/Axient/UHF-R, Barco E2 Jr/EC-30/EC-50/PDS902, Extron, Lightware, Teradek Bolt), and new stock since April (Shure SM7B, Netgear M4250, Mio Mix 104, Fischer IEM BP, Cyclone 4K, BrightSign HD224, ScreenBeam 1100+, HDBaseT 4KEX70-L, KVMs, Kramer VIA Connect², DJI Osmo Pocket 3, Asus NUC13, ASUS TUF A15, Beetronics 22" touch, Philips 27", BMD Cleanswitch 12x12 / Sync Generator / ATEM Mini Extreme ISO, DrayTek AP 960C, Unilumin uPad IV, and more).

## Retired kit (kept for sub-rent diagrams)

No longer in Current RMS but shapes retained deliberately — these still appear on jobs as sub-rentals:

- **Brompton** — entire range gone from RMS (SX40, S8, M2, T1, XD). `brompton.xml` kept.
- **Novastar** — MCTRL R5, MX40 Pro, MX2000 Pro, H9, NovaPro UHD Jr, CVT 10 no longer held. Still held: MCTRL4K, MCTRL660, MX20, MX30, VX1000, VX4, VX4U, VX6S. All 14 shapes kept in `novastar.xml`.

## Libraries

| File | Devices | Notes |
|---|---|---|
| `_cables.xml` | 18 styles | Cable convention edge templates (colour = signal, line = transport, width = criticality) |
| `blackmagic.xml` | 28 | Community-sourced + Cleanswitch 12x12, Mini Converter Sync Generator, ATEM Mini Extreme ISO (no source .py — appended directly to XML) |
| `brompton.xml` | 5 | RETIRED from stock — kept for sub-rent (SX40, S8, M2, T1, XD) |
| `novastar.xml` | 14 | 8 in stock + 6 retired-but-kept (see above) |
| `projectors.xml` | 6 | NEW — Epson EB-PU2010B; Panasonic PT-MZ770, PT-RZ970, PT-RZ120, PT-RZ12KEJ, PT-RZ21K |
| `roland.xml` | 3 | NEW — V-40HD, V-60HD, XS-84H matrix |
| `yamaha.xml` | 10 | QL1, DM3, DXR12, MSP3 + CL5, QL5, LS9-32, M7CL, RIO1608-D, RIO3224-D |
| `allen-heath.xml` | 7 | SQ5, CQ-12T, DX168, Zedi 10 + QU16, Zed 14, AB168 |
| `midas.xml` | 2 | DL32 + M32 |
| `dnb.xml` | 24 | D12/D20/D40/D80 amps + E8/M4/T10/V-Sub/Y10P/Y7P + E6, MAX 15, Q1, Q7, Q-Sub, Y8, Y-Sub, B2, B6, B22, C4, C7, DS10, R70 |
| `shure.xml` | 15 | MX412, SM58 + SM7B, ULX-D (quad RX/BP/HH), Axient (AD4DA/AD1/AD2), UHF-R (UR4D+/UR4S+/UR1/UR2), UA845, UA874 |
| `sennheiser.xml` | 12 | EW-DX, EW-D, EM 300-500 G4, beltpacks/handhelds, IEM, MAT 153-S |
| `audio-other.xml` | 18 | QSC, BSS, Behringer, Tascam, Sonifex, Sonos, Bose, LD, Lynx, RED, Pioneer DM-40D + Mio Mix 104, Fischer Amps IEM BP |
| `mics.xml` | 5 | DPA, Rode, generic lapel/BT lapel |
| `dj-kit.xml` | 3 | CDJ-3000, DJM-A9, DJ Kit bundle |
| `barco.xml` | 7 | E2 4K, S3 4K Gen 2, PDS 4K + E2 Jr, EC-30, EC-50, PDS902 |
| `aja.xml` | 2 | 1×6 SDI DA, C10DA |
| `decimator.xml` | 2 | MD-HX, MD-Cross v3 |
| `kramer.xml` | 4 | VM-4H2 1:2, 1:4 + HDMI Line RX, VIA Connect² |
| `extenders.xml` | 18 | LINDY, Neoteck, HDMI 3:1, Pro Signal 4×4, Datapath FX4/H + HDBaseT 4KEX70 TX/RX, MT-VIKI & TESmart KVMs, Extron HDMI DA6 / SDI DA 1:4 / DTP TX/RX, Lightware fibre TX/RX, Teradek Bolt TX/RX |
| `network.xml` | 27 | DrayTek (+ AP 960C), Netgear (+ M4250 AV Line), TP-Link, EE 4G, Ubiquiti + HP Baseline, 3com 2816, Cisco SG300-20, MikroTik RB4011 |
| `displays.xml` | 23 | Samsung TVs (24-98"), HP, IIYAMA, Lenovo + Philips 27" |
| `touchscreens.xml` | 10 | IIYAMA Prolite touch (15-75") + remote + Beetronics 22" |
| `led-panels.xml` | 13 | Absen, Aluvision, BeMatrix, LedSkin, Unilumin UPad IV XS + uPad IV, generic 2.5mm & 3.9mm 500×500 |
| `cameras.xml` | 7 | Canon, Lumix, Sony, Logitech, BirdDog + DJI Osmo Pocket 3, Spedal webcam |
| `playback.xml` | 14 | BrightSign HD1024/HD224/LS445/XT1144, Apple TV, Pro Signal MP, Sprite, Mac Studio, vMix/Pixera workstation + Cyclone 4K, ScreenBeam 1100+, Akai APC Mini, PlaybackPro kit, QLab rack |
| `comms.xml` | 13 | GreenGo, Motorola, EarTech, Interspace cueing |
| `elgato.xml` | 3 | Streamdeck Mini, XL, HD60 Pro |
| `computers.xml` | 19 | MacBook variants, Lenovo Legions, MSI, Intel NUCs + Asus NUC13 Pro i7, ASUS TUF A15, Mac Mini, iMac, Dell 9030 AIO, Surface Pro |

## Skipped (out of signal-flow scope)

Cables, adapters, power supplies, mains distribution, brackets, mounts, stands, packaging cases, ladders, tools, batteries, chargers, antennas without active electronics, tripods, USB sticks, hard drives, software licences (vMix, QLab, Resolume, Millumin, GreenGo SW, Unity Comms, Air Server), EpicTech / DHL / generic Subrent placeholders, generic "PA System" bundle entries, mic clamps, mic clips, speaker stand poles, phono/XLR cables, "[Equinox]" duplicates, generic round bases, headset cases, consumer headphones/speakers (HD 450BT, SRH240A, Megaboom 3/4, Volkano, Sony neckband), passive in-ceiling/install speakers (Clever Acoustic, Vision SP-1800), remotes, silent disco kit, lighting (separate domain — incl. Pharos LPC-2, Martin P3/Sceptron, Advatek PixLite, DMX nodes/dongles), tablets & phones (iPads, Galaxy Tab, iPhone — interaction devices, not signal-flow endpoints), services/day rates, projection screens (passive).

Wired vocal/instrument mic model variants (Beta 5x/8x/9x, SM57, PG58, SV200, e604/e906, ME6x, RE20 etc.) — one dynamic-mic shape (SM58) stands in for all; same XLR-out port layout.

Legacy LG/NEC/Panasonic displays (43-98") — port-identical to the Samsung size-equivalent tiles; use those.

## Notes

- Where the exact port layout is well known (Yamaha QL1, Sennheiser EW-DX, Midas DL32, Barco E2, etc.) the libraries are accurate.
- For obscure switches/routers/converters I built a sensible generic chassis. Correct on use as needed.
- Large-format desks added June 2026 (CL5, M7CL, M32 etc.) use grouped port ranges ("Omni In 1-32") rather than one cell per socket, to keep tile heights sane. The April-era desks (QL1, SQ5) keep individual ports.
- Lighting (64+ products) is a separate domain — different convention (DMX universes, hot patches, rigging plots) — left for a future skill.
- Computers get minimal chassis — generally TB/HDMI outs + ethernet + USB. Model variants don't change port layout meaningfully, but each is a separate library tile so techs can find it by GPU/CPU label.
- `audio-other.xml` and similar grouped files exist to keep the picker tidy — single-device-per-vendor entries collapsed into thematic libraries.
- `blackmagic.xml` has no `sources/` generator (community import). The three June 2026 additions were appended to the XML directly; if a `sources/blackmagic.py` is ever created it must include them.
