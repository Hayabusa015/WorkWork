---
name: build-presentation
description: Build a SHULL section slide deck as .pptx from the twelve-layout template. Use for any deck, presentation, or lecture slides, and for revising or QA-ing an existing one. Produces a .pptx plus a rasterized visual QA pass.
---

# build-presentation

Design and geometry: `brand/SHULL_DESIGN_SYSTEM.md` §12 and `slideGeometry` in `brand/tokens.json`.

> **Build from the twelve-layout template. Never from scratch.** New slide → Layout → pick one.

## Scope

**One deck covers one section**, not a whole unit. Default 12–20 content slides for a one-period
section.

## The reserved-height rule — the constraint that matters most

> Place the highlight block **first**. Compute the content column height as slide height minus block
> minus footer band. Flow text into what remains.

**Never place text first and overlay the block.** That is how a shipped preview came out clipped,
and clipped text is the highest-priority visual defect in the gate.

## Non-negotiables

- **Exactly one highlight / must-write block per slide.** Two cues means students copy neither.
- **Every worked example is followed by its solution slide, every time.** A worked example with no
  solution slide is a bug, not a style choice.
- **Dark grounds are structural only** — unit title, section divider, unit summary, index. Content
  slides are light.
- **Line caps** in `slideGeometry.lineCaps`. **Exceed one and you split the slide.** Never shrink
  type to fit.
- **16pt floor** for anything read from a seat. The footer chip is the only exception.
- **Section markers on dark dividers are circles.** Number squares are for print. Do not cross them.
- **Card colour logic:** either all cards neutral, or a coloured card means "write this definition" —
  and if so, the deck says so in words. Never mix with no stated rule.

## Sequence

Unit title → Agenda → Learning target → Vocabulary → Section divider → Content → Worked example →
**Solution** → Lab or application → Formative check → Review → Unit summary. Drop what does not
apply; keep the order.

A long deck needs enough variation that not every slide looks identical. **Variation stays inside
the system** — that is the difference between a designed deck and a template.

## Colour on slides

Dark ground → `primary` / `secondary` for accents. Light ground → `primaryDeep` for anything read as
type. See `apply-shull-design`.

## Images

Anything students **read** as science is hand-built. Anything they only **look** at may be generated.
A generated Bohr diagram will have the wrong electron count in a way nobody catches at a glance.
Geology specimen photographs for identification are **shot, never generated**.

## Animation

Subtle, purposeful, professional. **Never animate because the software permits it.**

## Finishing

Export to PDF, rasterize, and **scan every slide for clipped text.** Then `audit-deliverable`.
