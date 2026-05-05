# Coverage Status

Tracking completed against the Insert Productions rental kit list (April 2026 export, 824 products → 269 signal-flow-relevant).

## Status: complete for the rental list

All signal-flow-relevant kit from `product_rental_income_report_04-24-2026` is now in the repo. **27 libraries / ~218 device shapes**.

## Libraries

| File | Devices | Notes |
|---|---|---|
| `_cables.xml` | 18 styles | Cable convention edge templates (colour = signal, line = transport, width = criticality) |
| `blackmagic.xml` | 25 | Community-sourced (patchify-style format) |
| `brompton.xml` | 5 | Tessera SX40, S8, M2, T1, XD |
| `novastar.xml` | 14 | MCTRL4K, MCTRL R5, MCTRL660, MX20, MX30, MX40 Pro, MX2000 Pro, H9, NovaPro UHD Jr, VX1000, VX4, VX4U, VX6S, CVT 10 |
| `yamaha.xml` | 4 | QL1, DM3, DXR12, MSP3 |
| `allen-heath.xml` | 4 | SQ5, CQ-12T, DX168, Zedi 10 |
| `sennheiser.xml` | 12 | EW-DX EM 4 (Dante 4ch + 8-way rack), EW-D AS, ADP-UHF, EM 300-500 G4, EW-DX SK/SKM, SK 500 G4, ew300 G3 handheld, IEM RX/TX, MAT 153-S |
| `shure.xml` | 2 | MX412, SM58 |
| `midas.xml` | 1 | DL32 stagebox |
| `aja.xml` | 2 | 1×6 SDI DA, C10DA |
| `decimator.xml` | 2 | MD-HX, MD-Cross v3 |
| `kramer.xml` | 2 | VM-4H2 1:2, 1:4 |
| `barco.xml` | 3 | E2 4K, S3 4K Gen 2, PDS 4K |
| `dnb.xml` | 10 | D12/D20/D40/D80 amps + E8/M4/T10/V-Sub/Y10P/Y7P speakers |
| `audio-other.xml` | 16 | QSC CP8/GXD 4, BSS AR133, Behringer UMC202/404HD, Tascam DR-701D, Sonifex RB-DA6G, Sonos AMP/Era 100/Move, Bose Soundbar, LD MAUI 28 G2 (+W/Sub), Lynx QB-5, RED 505, Pioneer DM-40D |
| `mics.xml` | 5 | DPA 6066 (beige + black), Rode NTG2, generic lapel, DJI BT lapel |
| `dj-kit.xml` | 3 | CDJ-3000, DJM-A9, DJ Kit bundle |
| `network.xml` | 21 | DrayTek (3910P, G2280x, P2280x, P2100, AP 962C); Netgear (GS116PP, GS724T, GS748T, MS510TXPP, JGS516PE); TP-Link (4 routers + 2 switches); EE 4G; Ubiquiti (UDM Pro, USW Pro 24, U7 Pro AP, Unifi rack) |
| `displays.xml` | 22 | Samsung TVs (all common sizes 24-98"); 2 outdoor (LH55OHF2, QE55LST7); HP 5527SF; IIYAMA 24/28; Lenovo 27 |
| `touchscreens.xml` | 9 | IIYAMA Prolite touch (15/27/32/43/49/55/65/75") + remote |
| `led-panels.xml` | 11 | Absen PL2.5 V2 (b11 + L/R corners), V10 (b7), 2.5 Polaris; Aluvision HiLED55+; BeMatrix LedSkin; LedSkin 1.9/2.5; Unilumin UPad IV XS; 3.9mm 500×500 |
| `cameras.xml` | 5 | Canon EOS R50, Lumix GH6, Sony PXW-Z150, Logitech BRIO, BirdDog Studio NDI |
| `playback.xml` | 8 | BrightSign HD1024/LS445/XT1144, Apple TV, Pro Signal MP, Sprite, Mac Studio, generic vMix/Pixera workstation |
| `comms.xml` | 13 | GreenGo (Switch 5, 2× beltpacks, antenna, headset); Motorola GP340 + handheld; EarTech 4-way; Interspace (Cueing Toolbox, MicroCue3 kit + clicker, balance boxes) |
| `extenders.xml` | 6 | LINDY USB CAT5 TX/RX, Neoteck HDMI RX, generic HDMI 3:1, Pro Signal 4×4 4K matrix, Datapath FX4/H |
| `elgato.xml` | 3 | Streamdeck Mini, Streamdeck XL, HD60 Pro |
| `computers.xml` | 13 | 5× MacBook variants (Pro M4/M3 Max/M2 Pro Max/Air M3/Pro 2019), 5× Lenovo Legion (V15/GTX1660/RTX2060/RTX3070/RTX4060), MSI 15.6 RTX 4050, Intel NUC i5 + i7 SFF |

## Skipped (out of signal-flow scope)

Cables, adapters, power supplies, mains distribution, brackets, mounts, stands, packaging cases, ladders, tools, batteries, chargers, antennas without active electronics, tripods, USB sticks, hard drives, software licences, EpicTech / DHL / generic Subrent placeholders, generic "PA System" bundle entries, mic clamps, mic clips, speaker stand poles, phono/XLR cables, "[Equinox]" duplicates, generic round bases, headset cases, consumer headphones (HD 450BT, SRH240A, Megaboom), passive in-ceiling speakers, remotes, lighting (separate domain).

## Notes

- Where the exact port layout is well known (Yamaha QL1, Sennheiser EW-DX, Midas DL32, Barco E2, etc.) the libraries are accurate.
- For obscure switches/routers/converters I built a sensible generic chassis. Correct on use as needed.
- Lighting (64 products) is a separate domain — different convention (DMX universes, hot patches, rigging plots) — left for a future skill.
- Computers get minimal chassis — generally TB/HDMI outs + ethernet + USB. Model variants don't change port layout meaningfully, but each is a separate library tile so techs can find it by GPU/CPU label.
- `audio-other.xml` and similar grouped files exist to keep the picker tidy — single-device-per-vendor entries collapsed into thematic libraries.
