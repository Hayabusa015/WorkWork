# ARCHIVED — Slide System v2 medium split (Amber on Ink / Bio Lime on Parchment)

**Status:** DEPRECATED · **Superseded:** 2026-09-07 by spec Part 6 (white/light default)
**Was authoritative in:** `_Brand/Standards/SHULL_Slide_System_v2.md` §1
**Self-labelled:** WORKING pending sign-off. **The sign-off was never recorded anywhere.**

| | Slides (projected) | Print |
|---|---|---|
| Ground | Ink black `#111111` / Paper `#F6F6F6` | Parchment `#EDF0E5` |
| Accent | Amber `#FFCB74` | Bio Lime `#A8C97F` |
| Structure | Ink `#111111` | Deep Forest `#1A2318` |

## The reasoning, which was sound

Projection and paper are different media. Bio Lime on parchment is engineered for a photocopier and
to save toner, and goes muddy under a classroom projector. Amber on near-black is engineered for a
lit room and would burn a cartridge dry in a week.

## Why it was superseded

Spec Part 6 makes white and light the presentation default, which removes the dark projection ground
the split depended on.

## What survived it

- **"Dark grounds are structural"** — unit title, section divider, unit summary, index; content
  slides light. This was v2's own rule and it agrees with Part 6.
- **The 16pt content floor**, and the observation that produced it: a prototype deck had 104 runs at
  9pt, "unreadable past the second row."
- **The twelve-layout template** and its 09/10 example-and-solution pairing.
- **The medium-awareness principle itself.** The specific split is gone; the insight that a colour
  engineered for paper can fail under a projector is now in the design system as the requirement
  that every colour carry measured contrast against both grounds.
