# Design — SHULL OS app

The locked design system for `app/`. Every page redesign reads this file before
emitting code. Do not regenerate per page — extend or amend this file when the
system needs to grow.

**This file does not own the colours.** `brand/tokens.json` at the repository root is
the authority for every hex, and `scripts/build_app_tokens.py` generates
`app/public/tokens.css` from it. A colour changed here and not there is the defect
`validate_tokens.py` exists to catch. What this file owns is how the app *uses* those
tokens.

## Genre
modern-minimal — a working tool, not a marketing page. Function carries it; no
enrichment, no hero imagery, no illustration.

## Macrostructure family
- App pages: **Workbench** — fixed tool rail, working surface beside it, content in
  panels. Varies only by what fills the surface.
- There are no marketing or content pages in this app.

## Theme
Derived, not picked. Dark ground because `brand/tokens.json` measures every course
display colour against asphalt and all three clear AAA there (Lab Lime 12.0,
Quantum Gold 10.15, Terra Teal 7.27). The `*Deep` text-on-light variants are
deliberately unused here — they are for paper.

| Slot | Source |
|---|---|
| `--paper` / `--paper-2` / `--paper-3` | `ground.asphalt` / `ground.graphite` / mix |
| `--ink` / `--ink-2` / `--ink-3` | `ground.white` / `ground.mutedOnDark` / 85 % mix |
| `--accent` | **the selected course's `primary`** — see below |
| `--course-*` | all three course `primary` values, for lists showing every course |
| `--danger` / `--caution` / `--success` | `semantic.*` — never substituted by a course colour |

### The accent is a slot, not a value
`[data-course]` on `<body>` selects it. Chemistry turns the app Lab Lime, Physics
Quantum Gold, Geology Terra Teal; `class` routing takes the neutral parchment accent
because no single course owns a general-class material.

Before this, the app hard-coded Geology's locked Terra Teal as the accent on every
screen, Chemistry and Physics included. A course's identity colour is not a UI accent.
(The value itself stays in `brand/tokens.json`, which is why it is not repeated here.)

### Contrast is measured, not eyeballed
Muted text (`--ink-3`) measured **2.74:1** on a panel before this pass — below WCAG AA
and far below the house 5.5 — while carrying every hint, date and caption. It is now
85 % mix: 6.57 on the ground, 5.38 in a field, 4.63 on a panel. Functional borders
(`--rule-strong`) went 1.51 → 3.29 on a panel, clearing the 3:1 that WCAG 1.4.11 wants
for a UI boundary. `--rule` stays faint; it only draws decorative separators.

Re-measure with the probe in `docs/` or any canvas-based reader — `color-mix()`
resolves to `oklab()`, which naive contrast maths reads as garbage.

## Typography
- Body: `typography.stack` — Trade Gothic Next → Archivo → Liberation Sans
- Display: `typography.stackCondensed` — used only for the wordmark and the credit figure
- All headings roman. No italic headers.

## Spacing
4-point named scale in `tokens.css`. Use `var(--space-md)`, never a raw value.

## Motion
- `--ease-out` / `--ease-in-out`, `--dur-short` 160 ms, `--dur-mid` 240 ms
- Animate `transform` and `opacity` only
- Three primitives total: nav/button hover tint, card lift on the template gallery,
  1px press on `:active`
- `prefers-reduced-motion: reduce` collapses all of it
- The focus ring is **never** animated — it appears the instant focus lands

## Microinteractions stance
- Silent success. No celebratory toasts.
- Errors surface in `#notice`, bordered in `--danger`, never a modal.
- A destructive or costly action states its cost in text before the button, not after.

## CTA voice
- Primary: filled `--accent`, `--accent-ink` label, `--radius-input`
- Secondary: `--paper-3` fill, `--rule-strong` border
- Quiet: no fill, border only
- Every interactive element ships all 8 states.

## Per-page allowances
- App pages MUST NOT use enrichment — function carries the page.
- Panels may be rearranged by the user (the layout editor in `interface.js`);
  the system does not assume a fixed panel order.

## What pages MUST share
The wordmark, the course-accent mechanism, the type stack, the CTA voice, the panel
rhythm (`--radius-card`, `--rule-hair` border, `--space-md` padding).

## What pages MAY differ on
Which panels appear and in what order; the grid split; whether the surface is one
column or two.
