# SHULL Science Slide Standard — Geometry and Layout

16:9, 13.333 × 7.5 in. All measurements in inches from the top-left.

## Palette assignment

| Element | Color |
|---|---|
| Content slide background | Parchment `#EDF0E5` |
| Title / divider / summary background | Deep Forest `#1A2318` |
| Body text on light | `#22271F` |
| Body text on dark | Parchment `#EDF0E5` |
| Headline accent word (one per headline) | Moss Green `#4A7C59` on light, Bio Lime `#A8C97F` on dark |
| Highlight / must-write block | Bio Lime `#A8C97F` fill, Deep Forest text |
| Rules and dividers | Moss Green `#4A7C59`, Warm Earth `#8B6914` for the second rule |

## Type scale

| Role | Size | Font |
|---|---|---|
| Unit title | 44–54pt | Poppins Bold |
| Slide headline | 30–36pt | Poppins Bold |
| Subhead | 20–22pt | Poppins SemiBold |
| Body bullet | 19–24pt | Lato / Liberation Sans |
| Highlight block text | 20–24pt | Lato SemiBold |
| Table cell | 16–18pt | Lato |
| Footer chip | 10–11pt | Poppins SemiBold, letter-spaced |

**16pt is the hard floor** for anything a student reads from a seat. The footer chip is the
only exception.

## Layout regions

```
┌────────────────────────────────────────────────────────┐
│ 0.55  headline band            (top 0.5 → 1.5)         │
│ ────  Moss Green rule at y=1.55                        │
│                                                        │
│       content column                                   │
│       x 0.7 → 8.1     (or full width 0.7 → 12.6)       │
│                                                        │
│       ── reserved highlight block ──                   │
│                                                        │
│                              footer chip  y 6.9        │
└────────────────────────────────────────────────────────┘
```

Right rail, when used: x 8.5 → 12.6. Used for solution tallies, data tables, a single
diagram. Content inside a rail card is **vertically centered**, not top-aligned.

## The reserved-height rule

The single most important layout constraint. The highlight block is placed first and the
content column's height is computed as *slide height minus block height minus footer band*.
Text is then flowed into what remains.

Do not place text first and overlay the block. That is how slides 8 and 17 of the U8 preview
shipped with cut-off text.

**Hard line caps:**

| Layout | Max |
|---|---|
| Content slide **with** highlight block | 3 bullets, ≤ 2 lines each |
| Content slide **without** highlight block | 5 bullets, ≤ 2 lines each |
| Vocabulary slide | 4 terms |
| Worked example | 4 steps |
| Table slide | 6 data rows |

If the content exceeds the cap, split the slide. Never shrink type to fit.

## Spacing

- ≥ 0.15" fixed space after any subhead before the first bullet.
- 0.18–0.22" between bullets.
- 0.35" minimum from any text baseline to the edge of its containing box.
- Highlight block internal padding: 0.14" top/bottom, 0.20" left/right.

## Chips and markers

**Footer chip:** rounded rectangle, ~1.35 × 0.30 in, bottom-right at y ≈ 6.9. Reads
`U10 / S10.4`. Slate Stone fill with Moss Green outline on dark slides; Deep Forest fill
with Parchment text on light slides. Same chip family as the practice-set banner chip.

**Section markers on dark dividers:** circles, Bio Lime outline, Parchment numeral.
(Number *squares* are for print documents — problem numbers and organizer units. Circles
are the slide-divider variant. Don't cross them.)

## Card color logic

Pick one and state it on the Slide Key slide:

- **Option A (preferred):** all cards white/parchment, and the single Bio Lime block carries
  the must-write.
- **Option B:** green card = write this definition, white card = reference only. If you use
  this, the Slide Key slide must say so in words.

Never ship a deck that mixes green and white cards with no stated rule.

## Grayscale

Decks get projected, but they also get printed as handouts. Every categorical distinction
must survive grayscale — vary fill value and outline, not just hue.

## QA raster checklist

After `soffice --headless --convert-to pdf` and `pdf2image`:

- [ ] No text clipped at any box or slide edge
- [ ] Nothing under 16pt in the student-facing area
- [ ] Exactly one Bio Lime block per slide, at most
- [ ] Dark background only on title / divider / summary
- [ ] `U#/S#.#` chip on every slide, matching the filename
- [ ] Every worked example followed by a solution slide
- [ ] Subheads clear of the first bullet
- [ ] Rail card content vertically centered
- [ ] Headlines read correctly — grammar, not just spelling
