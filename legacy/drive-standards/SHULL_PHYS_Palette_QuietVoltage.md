# SHULL Physics Palette — "Quiet Voltage"

**Status:** CONFIRMED 2026-09-06. Physics only.
**Applies to:** every Physics deliverable — slides, guided notes, practice sets,
labs, quizzes, tests, reference sheets.
**Does not apply to:** Chemistry or Geology. Those keep their own palettes and
`_Brand/Templates/tokens.js` is unchanged for them.

---

## 1. Why this is a course exception

`SHULL_System_Governance.md` §2 allows a course to hold its own palette — Geology
already does. Physics is now the second declared exception. The base SHULL palette
(Deep Forest / Moss / Bio Lime / Parchment) stays in `shull-studio` §1 as the
default for Chemistry and Geology.

**Physics also collapses the Slide System v2 medium split.** v2 runs Amber-on-Ink
for projection and Bio Lime-on-Parchment for print, because Bio Lime washes out
under a projector. Quiet Voltage does not have that problem — Violet on Porcelain
measures 9.8:1, which holds in a lit room, and Porcelain is light enough to stay
ink-cheap on paper. So Physics runs **one palette across both media**.

---

## 2. The six tokens

| Token | Hex | Gray | Use |
|---|---|---|---|
| Porcelain | `#E7DDD7` | 223 | Light ground — printed pages, light content slides |
| Chrome Light | `#F7F3F0` | 244 | Card fill on porcelain, highlight |
| Chrome | `#B9ADA6` | 176 | Rules, borders, hairlines — **never text** |
| Violet | `#3A2168` | 49 | Primary accent: the one headline word, labels, chips, key working |
| Violet Static | `#A97BFF` | 152 | Highlight / must-write cue — **one per slide, no exceptions** |
| Ink Black | `#0B0A0E` | 11 | Body text, dark grounds, number squares, must-write bar |

A seventh working value, **Violet Mid `#6B4FA8`** (gray 97), carries the second
label colour in print so that two categories never differ by fill alone.

Sampled from Matt's reference image (porcelain body, chrome edge, violet core),
2026-09-06. Ink Black was added on request.

---

## 3. Contrast — measured, not estimated

| Pair | Ratio | Verdict |
|---|---|---|
| Ink Black on Porcelain | 14.8:1 | body text ✓ |
| Ink Black on Chrome Light | 17.9:1 | text in a card ✓ |
| Violet on Porcelain | 9.8:1 | accent headline word ✓ |
| Porcelain on Ink Black | 14.8:1 | light text on dark ground ✓ |
| Porcelain on Violet | 9.8:1 | text on a violet chip ✓ |
| Violet Static on Ink Black | 6.6:1 | highlight text on dark ✓ |
| Ink Black on Violet Static | 6.6:1 | text on the highlight block ✓ |
| **Violet Static on Porcelain** | **2.3:1** | **fails — never use as text on paper** |

**The one rule that follows:** Violet Static is a fill, a rule, or a marker bar.
It is never body text on a light ground. Violet is the text-safe accent.

---

## 4. Grayscale — the photocopier test

Every categorical pair sits at least 20 grey levels apart, so nothing depends on
hue alone:

Porcelain 223 · Chrome Light 244 · Chrome 176 · Violet Static 152 · Violet Mid 97
· Violet 49 · Ink Black 11

Tag pills on a practice set are still separated by **border colour as well as
fill**: WARM-UP takes a Violet border, PRACTICE a Chrome border, CHALLENGE a
Violet Mid border, MULTI-TOPIC a solid Ink Black fill.

---

## 5. Ink discipline — unchanged

Print rules from `shull-studio` still hold and Quiet Voltage does not relax them.
Measured on the rebuilt Unit 1 practice set: **5.2% of pixels marked, 2.9% heavy
ink.**

- Outlined mastheads, never a full-width filled banner.
- Outlined number squares. The solid Ink Black square is reserved for slides.
- Hairline table rules, never alternating shaded rows.
- Chart areas are **hatched**, not tinted, in print.
- The only solid fills on a student page are the small code chip, the tag pills,
  and the 0.06" Violet Static must-write bar.

---

## 6. Where the tokens live

| File | What it holds |
|---|---|
| `_Brand/Templates/tokens.phys.js` | The Physics token set, keyed to the names `build.js` already consumes |
| `_Brand/Templates/build.js` | Now reads `process.env.SHULL_TOKENS`, defaulting to `./tokens` — Chemistry and Geology are unaffected |
| `_Brand/Templates/tokens.js` | Untouched. Ink / Amber, for Chemistry and Geology |
| `PHYS_DECISIONS.md` → Course brand exceptions | The course-level record |
| `shull-studio` §1 | Needs the exception declared alongside Geology's — skill re-upload |

Build a Physics deck with:

```bash
SHULL_TOKENS=./tokens.phys.js node build.js
```

---

## 7. Image style block — replaces the amber one for Physics

The v2 style block specifies a warm amber key light. Warm gold next to violet
reads as a mistake, so Physics uses this instead. Append verbatim to every
Physics image prompt:

> Photorealistic, dramatic studio photography. Matte violet-black background
> (#14101E). Cool chrome key light from the upper left, deep shadow on the right.
> Shallow depth of field, soft falloff into black at the edges. Brushed steel,
> polished chrome and porcelain tones, with a single soft violet accent (#A97BFF)
> in the shadows. No warm gold or amber. No text, no labels, no numbers, no
> watermarks, no people. Wide 16:9 landscape, subject centred with generous
> negative space. Clean, editorial, museum-catalog quality.

**Existing images.** The eight Unit 1 lab photos were generated to the old amber
block. Rather than discard them they were regraded — desaturated to luminance,
then mapped through a violet-black → cool chrome → chrome-light ramp at 78%
strength so the metal keeps its texture. The script is `regrade.py`; point it at
any older amber-lit Physics image to bring it onto the palette.

---

## 8. Known gap

The Unit 1 photo tiles are 418 × 470 px, well under the 1920 × 1080 spec. They
work at panel size and fail at full bleed. Worth regenerating from the style
block above when image credits are available.
