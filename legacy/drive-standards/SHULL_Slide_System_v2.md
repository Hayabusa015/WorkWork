# SHULL Science — Slide System v2

**Status:** Replaces the previous Slide Standard for **projected slides only.**
Print documents are unchanged. Read the scope rule below before anything else.

---

## 1. Scope — the two palettes

SHULL now runs two palettes, split by medium, not by course.

| | Slides (projected) | Print (worksheets, notes, tests, labs) |
|---|---|---|
| Ground | Ink black `#111111` / Paper `#F6F6F6` | Parchment `#EDF0E5` |
| Accent | Amber `#FFCB74` | Bio Lime `#A8C97F` |
| Structure | Ink `#111111` | Deep Forest `#1A2318` |
| Font | Poppins | Poppins + Liberation Sans |

**Why the split is legitimate.** Projection and paper are different media.
Bio Lime on parchment is engineered for a photocopier and to save toner; it goes
muddy under a classroom projector. Amber on near-black is engineered for a lit
room and would burn a cartridge dry in a week.

**The rule:** if it will be projected, amber. If it will be printed, Bio Lime.
Nothing prints from the slide deck except handout exports, which convert.

*This split needs Matt's sign-off. Until then, treat it as WORKING.*

### Physics is an exception — CONFIRMED 2026-09-06

Physics does not use the two palettes above, and does not use the medium split at
all. It runs one palette, "Quiet Voltage," across both projection and print:

| | Physics — both media |
|---|---|
| Ground | Porcelain `#E7DDD7` (light) / Ink Black `#0B0A0E` (dark) |
| Accent | Violet `#3A2168` (text-safe) · Violet Static `#A97BFF` (fill only) |
| Structure | Ink Black `#0B0A0E`, rules in Chrome `#B9ADA6` |
| Font | Poppins + Liberation Sans |

The split exists because Bio Lime washes out under a projector. Violet on
Porcelain measures 9.8:1, so that reasoning does not apply. Violet Static measures
2.3:1 on Porcelain and is never used as body text on a light ground.

Full token table, contrast and grayscale measurements, and the replacement image
prompt style block: `SHULL_PHYS_Palette_QuietVoltage.md`.

Chemistry and Geology are unaffected — `tokens.js` is unchanged for them.

---

## 2. The template

`_Brand/Templates/SHULL_Science_Slide_Template.pptx` — twelve layouts in the
slide master. New slide → Layout → pick one. Never build a slide from scratch.

| # | Layout | Ground | Use |
|---|---|---|---|
| 01 | Unit Title | dark | Opens a unit |
| 02 | Section Title | amber | Opens a section |
| 03 | Grouped Concept | light | Two contrasting ideas + image |
| 04 | Divider | dark | Visual reset, one concept image |
| 05 | Process / Timeline | light | Four numbered steps |
| 06 | Concept + Image | dark | Framing left, image panel right, key question |
| 07 | Comparison Cards | light | Three parallel items |
| 08 | Diagram + Annotation | light | Figure left, labeled rules right |
| 09 | Example Problem | light | Problem, given, need, empty work area |
| 10 | Worked Solution | light | Data, formula, completed work |
| 11 | Givens / Equation / Answer | light | Any course |
| 12 | Deck Index | dark | Reference. Delete before class. |

**09 and 10 are a pair.** Every example problem gets its solution slide.

---

## 3. Type

| Role | Size |
|---|---|
| Unit title | 40 |
| Section number | 44 |
| Headline | 28 |
| Subhead | 17 |
| Body, card body | 16 |
| Work area, answer | 18–20 |
| Card label | 12 |
| Eyebrow | 11 |
| Footer | 10 |

**Floor: 16pt for anything read as content.** 10–12pt is permitted only for
eyebrows, card labels, and footers — navigation, not content. The prototype
deck had 104 runs at 9pt; that is unreadable past the second row.

---

## 4. Rules carried forward

1. **One must-write bar per slide.** The only write-this cue. Two cues means
   students copy neither.
2. **Dark grounds are structural** — unit title, section title, divider, index.
   Content slides are light. Layout 06 is the single deliberate exception.
3. **Reserve, don't layer.** A highlight block reserves its height and text
   flows around it. This is why the U8 preview clipped on slides 8 and 17.
4. **Example problems ship with an empty work area.** Filled live on the board.
5. **Rasterize and scan every deck before delivery.** Clipped baselines are the
   most common defect and the only reliable catch is looking at the pixels.

---

## 5. Images

### The division of labor

| Generated | Hand-built by Claude |
|---|---|
| Real objects — glassware, apparatus, instruments, benches | Anything with a number, label, or formula |
| Atmosphere, mood, historical settings | Bohr diagrams, Lewis structures, orbitals |
| Landscape and texture | Free-body diagrams, graphs, vectors |

**The test:** if students *read* it as science, it's built. If they only *look*
at it, it's generated. A generated Bohr diagram will have the wrong electron
count in a way nobody catches at a glance.

**Geology exception.** Atmosphere may be generated. Specimen photographs for
rock and mineral identification may not — a generated "quartz" is not quartz,
and identification is the thing being assessed. Shoot those.

### Sourcing

**Physics uses a different style block** — cool chrome and violet, not warm amber.
See `SHULL_PHYS_Palette_QuietVoltage.md` §7. Older amber-lit Physics images can be
brought onto the palette with `_Brand/Templates/regrade.py` instead of being
regenerated.

Higgsfield is out of credits and Claude cannot download images — Wikimedia,
NASA, and every other host are blocked from the build environment. The working
loop is:

1. Claude supplies a prompt per slide (`SHULL_Image_Prompt_Pack.md`)
2. Matt generates in Gemini, ChatGPT, or Canva Magic Media
3. Matt saves under the given filename and attaches
4. Claude places, corrects exposure, and re-renders

### Spec

- **16:9, minimum 1920 × 1080.** Every slot is 16:9 except the Process/Timeline
  band, which is 3:1 — generate 16:9 and center-crop.
- Near-black ground, warm amber key from upper left, shallow depth of field
- **No text in the image, ever.** All labels are live text on the slide.
- Too bright is fixable on the way in. Don't discard for exposure.

### The style block

Append verbatim to every prompt. This is what makes images from different
sessions look like one deck.

> Photorealistic, dramatic studio photography. Matte near-black background
> (#111111). Warm amber key light (#FFCB74) from the upper left, deep shadow on
> the right. Shallow depth of field, soft falloff into black at the edges. Rich
> gold and warm brass tones against cool grey. No text, no labels, no numbers,
> no watermarks, no people. Wide 16:9 landscape, subject centered with generous
> negative space. Clean, editorial, museum-catalog quality.

---

## 6. Regenerating the template

Source lives in `_Brand/Templates/`. `tokens.js` holds every color and size;
change a token, run `node build.js`, and all twelve layouts follow.

`build.js` now selects its token module from `process.env.SHULL_TOKENS`, defaulting
to `./tokens`. A course with a declared palette exception supplies its own file
rather than forking the build:

```bash
node build.js                                  # Chemistry / Geology — Ink & Amber
SHULL_TOKENS=./tokens.phys.js node build.js    # Physics — Quiet Voltage
```

The layout geometry, type scale and the twelve masters are identical either way.
A palette exception is a colour change only.
