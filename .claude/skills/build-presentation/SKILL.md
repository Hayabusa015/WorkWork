---
name: build-presentation
description: Build a SHULL section slide deck as .pptx from the twelve-layout template. Use for any deck, presentation, or lecture slides, and for revising or QA-ing an existing one. Produces a .pptx plus a rasterized visual QA pass.
---

# build-presentation

Design and geometry: `brand/SHULL_DESIGN_SYSTEM.md` §12 and `slideGeometry` in `brand/tokens.json`.
The template itself, and what each layout is for: `templates/slide/README.md`.

> **Build from the twelve-layout template. Never from scratch.** New slide → Layout → pick one.

```bash
cd templates/slide && SHULL_COURSE=<course> node build.js <deck>.pptx
```

One file, three courses. There is no per-course fork and you must not create one — a course that
needs different colour is a token change in `brand/tokens.json`.

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
- **16pt floor** for anything read from a seat. Below it is navigation only — eyebrow, card label,
  footer code — never a sentence. `audit_slide_geometry.py` enforces exactly that distinction.
- **Section markers on dark dividers are circles.** That is a section marker, not a list number.
- **A numbered list is just the number** — no box, no square, no circle. SHULL-CHG-0015, every format.
- **Card colour logic:** either all cards neutral, or a coloured card means "write this definition" —
  and if so, the deck says so in words. Never mix with no stated rule.
- **Course colour is never a small label on a card.** `primaryDeep` on parchment measures 4.8:1 and
  Terra Teal on graphite 5.1:1 — both under the 5.5 target. Card labels are neutral; the accent
  carries rails, panels, the must-write cue and the numerals. See SHULL-CHG-0013.

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

```bash
python3 scripts/audit_slide_geometry.py <deck>.pptx
soffice --headless --convert-to pdf <deck>.pptx && pdffonts <deck>.pdf
```

The audit reads the built file, not the source: overlapping text, text off the slide, content under
the type floor, and any text/ground pair below the contrast target. `pdffonts` must show **Archivo,
embedded** — Liberation or DejaVu in that list means the stack silently substituted and every later
check would be inspecting a different document than the one that ships.

Then rasterize and **look at every slide.** The mechanical checks do not replace this; the two box
collisions in SHULL-CHG-0013 finding 7 were caught by eye first. Then `audit-deliverable`.
