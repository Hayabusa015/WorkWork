# ARCHIVED — Physics "Quiet Voltage"

**Status:** DEPRECATED · **Superseded:** 2026-09-07 by SHULL-CHG-0002 (Quantum Gold + Deep Purple)
**Was authoritative in:** `_Brand/Standards/SHULL_PHYS_Palette_QuietVoltage.md`, **CONFIRMED
2026-09-06**, cross-confirmed by `SHULL_Slide_System_v2.md` §1
**Lifetime: one day.** Verbatim source: `legacy/drive-standards/SHULL_PHYS_Palette_QuietVoltage.md`

| Token | Hex | Grey | Use |
|---|---|---:|---|
| Porcelain | `#E7DDD7` | 223 | Light ground, both media |
| Chrome Light | `#F7F3F0` | 244 | Card fill, highlight |
| Chrome | `#B9ADA6` | 176 | Rules, borders — never text |
| Violet | `#3A2168` | 49 | Text-safe accent |
| Violet Static | `#A97BFF` | 152 | Fill-only highlight cue |
| Violet Mid | `#6B4FA8` | 97 | Second label colour in print |
| Ink Black | `#0B0A0E` | 11 | Body text, dark grounds |

## Why this one matters more than the others

It was not a proposal. It shipped, inside twenty-four hours: `tokens.phys.js`, a `SHULL_TOKENS`
environment hook in `build.js` so a course palette could exist without forking the template,
`regrade.py` to bring eight existing Unit 1 lab photographs onto the palette, a rebuilt Unit 1
practice set measured at 5.2% pixel coverage, a replacement image-prompt style block, and a measured
contrast table for eight colour pairs.

## What survived it — and it is the best of the legacy system

**1. Measured contrast, not asserted contrast.** Quiet Voltage measured every pair and *failed* one
of its own: Violet Static on Porcelain at 2.3:1, ruled out for text on paper. That method is now
`rules.contrastTargetText` and the `measured.*` blocks in `tokens.json`, and it is what surfaced
CONFLICT-28 — the finding that the replacement palette fails as text on white.

**2. A text-safe accent distinct from a fill-only accent.** Violet for type, Violet Static for
fills, with an explicit rule that the fill colour is never body text. That is exactly the shape of
SHULL-CHG-0008's `primaryDeep`. **The palette was replaced; its central idea was adopted.**

**3. Grayscale spacing as a measured floor** — every categorical pair at least 20 grey levels apart.
Now `rules.grayscaleSeparationMin`.

**4. Border *and* fill on tag pills**, so two categories never differ by fill alone.

**5. The token-indirection pattern.** `SHULL_TOKENS=./tokens.phys.js node build.js` — one build,
per-course overlays, no forked template. Preserved in `templates/`.

## Materials built on it — leave as-is

Eight Physics Unit 1 lab photographs, regraded to violet-black and cool chrome at 78% strength ·
the rebuilt Physics Unit 1 practice set · `_Brand/Templates/tokens.phys.js` · `regrade.py`, whose
violet ramp is now obsolete.

Under the no-retrofit policy these stay as built and are **not** brand defects. The user was offered
a rebuild and did not elect one. Ask before redoing them.

## Known gap it recorded, still true

The Unit 1 photo tiles are 418 × 470 px, well under the 1920 × 1080 spec. They work at panel size
and fail at full bleed.
