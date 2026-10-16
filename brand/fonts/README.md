# Fonts

**Archivo** and **Archivo Narrow** — SIL Open Font License, redistributable, committed here.

Chosen in SHULL-CHG-0006 because they are neo-grotesques with true condensed cuts, close in
character to Trade Gothic Next. The previously documented ladder named Poppins, which is geometric
and a poor stylistic match, and which is **not installed in the build container** despite a skill
file asserting that it is.

A SessionStart hook installs these to `~/.fonts` and runs `fc-cache`, so the QA render and the
shipped PDF are the same artifact. Before this, every QA pass inspected Liberation Sans metrics
while the document declared Trade Gothic Next.

**ShullHand** — made from Matt's own handwriting, so there is no third-party licence. Adopted by
SHULL-CHG-0044 (PROVISIONAL until Matt confirms it on a real key). **Teacher answer keys only, never a
student page** — it is the face named by `typography.keyHandwriting` in `brand/tokens.json`, and it is
deliberately outside the Archivo stack. Version **0.2** (internal family `ShullHand`, version string
`Version 0.2`; 140 glyphs plus 36 alternate copies of letters and digits, which the key helper
alternates so repeated characters do not look stamped).

| File | sha256 |
|---|---|
| `ShullHand.ttf` | `28095a1f30a325ac65871be158fb27b706c0c192ac0bad079335290281e6fa74` |
| `ShullHand_alts.json` (base character to Private Use alternate) | `120aee2bbd01367c7889785fce4cd044ff2384a8c9ef55bab844e60dff0a9cd2` |
| `source/ShullHand-handwriting-sample-2026-10-16.pdf` (the source scan) | `7bd966d324d800d02e91da4c25dde3bb874e8571f20f4f3b3873e285efc337ff` |

Rebuild from the committed scan:

```
python3 scripts/build_handwriting_font.py --scan brand/fonts/source/ShullHand-handwriting-sample-2026-10-16.pdf --page-order 4,1,2,3 --out brand/fonts/ShullHand
```

**Regenerating it.** A new version built from the same committed scan and script, with the same
character set and no new rule, is routine regeneration: no new change record. The commit message
names SHULL-CHG-0044 and the version, the version line and sha256 values above are updated, and one
real key is checked visually. A new change record is needed for a new source scan, a change of scope
beyond keys, a change in the fallback policy, or removing Patrick Hand (SHULL-CHG-0044 Item G).

Known limits of v0.2:
- Letters are separate, not joined.
- His "2" resembles an "a". Context usually resolves it; it is a legibility risk on keys.
- In his running writing "1" is a plain stroke, but the font uses his boxed "1".
- No sigma and no vector-arrow glyphs (the key builder draws arrows).
- Colons and periods are heavy.
- No superscript or subscript glyphs; the key builder draws them.
- The baseline does not drift the way real handwriting does.

**Patrick Hand** — SIL Open Font License, committed here (`PatrickHand-Regular.ttf`,
`OFL-PatrickHand.txt`). Source: `google/fonts` repository, `ofl/patrickhand`. Added by SHULL-CHG-0043.
**Now the per-glyph fallback** for any character ShullHand lacks (SHULL-CHG-0044); keys only, never a
student page. sha256 of the ttf: `0f173b3e6cb6d1af25babf7f0057c5ac4ee11f9992b0469bb817e967ef4ad0fc`.

**Trade Gothic Next is Monotype-licensed. Never commit it.** It is named first in the font stack so
files resolve correctly on Matt's own machine.
