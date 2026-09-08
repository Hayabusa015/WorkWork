# brand — the authoritative design system

| File | Owns |
|---|---|
| `SHULL_DESIGN_SYSTEM.md` | The design system in prose: philosophy, hierarchy, density, decoration, imagery, slide geometry |
| `tokens.json` | **The only place a hex value or measurement is written.** Everything else is generated from it. |
| `palette-archive/` | Every superseded palette, with a dated note saying what replaced it and when |
| `fonts/` | Archivo and Archivo Narrow (OFL), installed into the build container at session start |

**Every colour in `tokens.json` carries its measured contrast against both grounds and its
grayscale value. A colour that enters the palette without measurements is a defect.** That rule
exists because six palettes drifted apart when the same hex was typed by hand into different files
— and because the locked course colours turned out to fail as text on the locked white background,
which nobody caught until the numbers were computed.

**Trade Gothic Next is Monotype-licensed and must never be committed here.**

*Status: not yet written. Phase 8, unblocked.*
