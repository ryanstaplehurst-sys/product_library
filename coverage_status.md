# Coverage Status

Tracking progress through the Insert Productions rental kit list (April 2026 export, 824 products → 269 signal-flow-relevant).

## Done

- ✅ `_cables.xml` — 18 cable convention edge templates
- ✅ `blackmagic.xml` — community-sourced (25 devices)
- ✅ `brompton.xml` — Tessera SX40, S8, M2, T1, XD
- ✅ `novastar.xml` — partial (MCTRL4K, MCTRL R5, MX40 Pro, MX2000 Pro, H9, NovaPro UHD Jr, CVT 10)

## In progress / next

- ⏳ Extend `novastar.xml` — add MCTRL660, MX20, MX30, VX1000, VX4, VX4U, VX6S

## Queued (priority order)

| Priority | Manufacturer / file | Devices |
|---|---|---|
| 1 | `yamaha.xml` | DM3, QL1, DXR12 |
| 2 | `allen-heath.xml` | SQ5, CQ-12T, DX168, Zedi 10 |
| 3 | `sennheiser.xml` | EW-DX EM 4 Dante (8-way + standard), EW-D antenna splitter, ADP-UHF, EM 300-500 G4, SK 500 G4, ew300 G3 IEM (RX + TX), G3 ew300 handheld TX, MAT 153-S, L600 charger |
| 4 | `shure.xml` | MX412, SM58, SRH240A |
| 5 | `midas.xml` | DL32 |
| 6 | `aja.xml` | 1×6 distribution amp, C10DA |
| 7 | `decimator.xml` | MD-HX, MD-Cross v3 |
| 8 | `kramer.xml` | VM-4H2 (1:2, 1:4) |
| 9 | `barco.xml` | E2 4K SMS, S3 4K SMS Gen 2, PDS 4K |
| 10 | `dnb.xml` | D12, D20, D40, D80 amps; E8, M4, T10, V-Sub, Y10P, Y7P |
| 11 | `qsc.xml` | CP8, GXD 4 |
| 12 | `displays.xml` | Samsung (multiple sizes), IIYAMA Prolite (multiple), HP 27", Lenovo 27" |
| 13 | `iiyama-touch.xml` | Prolite touchscreens (15/27/32/43/49/55/65/75") |
| 14 | `network.xml` | DrayTek Vigor 3910 P, G2280x, P2100, AP 962C; Netgear GS116PP/GS724T/GS748T/MS510TXPP/JGS516PE; TP-Link AC1200/4G LTE/5G CPE/8-port/5-port; Ubiquiti UDM Pro, USW Pro 24, U7 Pro AP |
| 15 | `pioneer.xml` | CDJ3000, DJM-A9, DM-40D |
| 16 | `playback.xml` | BrightSign HD1024/LS445/XT1144, Apple TV, Pro Signal 4K Media Player, Sprite, Mac Studio media rack, BirdDog Studio NDI |
| 17 | `cameras.xml` | Canon EOS R50, Lumix GH6, Sony PXW-Z150, Logitech BRIO 4K |
| 18 | `led-panels.xml` | Absen PL2.5 (V2/V10), Absen 2.5mm Polaris, Aluvision HiLED55+, BeMatrix LedSkin, LedSkin 1.9mm/2.5mm, Unilumin UPad IV XS, generic 3.9mm 500×500 |
| 19 | `comms.xml` | GreenGo (Switch 5, beltpacks, headset, antenna), Motorola GP340, EarTech 4-way, Interspace Cueing Toolbox / MicroCue3 |
| 20 | `audio-other.xml` | BSS AR133 DI, Behringer UMC202HD/UMC404HD, Tascam DR-701D, Sonifex RB-DA6G, Sonos AMP/Era 100/Move, Bose Smart Soundbar, Yamaha MSP3, Lynx QB-5, RED 505, LD MAUI 28 G2 |
| 21 | `mics.xml` | DPA 6066 Core Omni Headset (beige + black), Rode NTG2, generic lapel/headset placeholders |
| 22 | `extenders.xml` | LINDY USB CAT5, Neoteck HDMI Extender RX, generic HDMI 3:1 |
| 23 | `pro-signal.xml` | 4×4 4K HDMI Switch, 4K Media Player |
| 24 | `elgato.xml` | HD60 Pro Game Capture, Streamdeck Mini, Streamdeck XL |

## Skipped (out of signal-flow scope)

Cables, adapters, power supplies / mains distribution, brackets, mounts, stands, packaging cases, ladders, tools, batteries, charging stations, antennas (without active electronics), tripods, USB sticks, hard drives, software licences, EpicTech / DHL / generic Subrent placeholders, generic "PA System" packaged kits, mic clamps, mic clips, speaker stand poles, phono cables, generic XLR cables, "[Equinox]" duplicate placeholders, generic round bases, headset cases (mic case ≠ device).

## Notes

- Where I have reliable knowledge of the exact port layout (Yamaha QL1, Sennheiser EW-DX, Midas DL32, Barco E2, etc.) the libraries are accurate.
- For obscure switches/routers/converters I build a sensible generic chassis. Marked with `# generic — verify ports` in the source.
- Lighting (64 products) is a separate domain — different convention (DMX universes, hot patches, rigging plots) — left for a separate skill.
- Computers (Apple, Lenovo, MSI, NUC) get minimal chassis — generally one HDMI/Thunderbolt out + ethernet + USB. Model variants don't change port layout meaningfully.
