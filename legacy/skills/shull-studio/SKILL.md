---
name: shull-studio
description: >
  The shared build engine and router for every SHULL Science classroom material Matthew
  Shull creates across Chemistry, Physics, and Geology at James A. Garfield Local Schools.
  Load this skill FIRST for any request to build, revise, plan, name, file, or audit a
  classroom document — slide decks, guided/Cornell notes, practice sets, tests and quizzes,
  labs, reference sheets, study guides, rubrics, unit plans, or pacing calendars. Trigger
  on phrases like "build me a deck for U8", "make guided notes for section 3.2", "practice
  set on molarity", "what do I still need for Unit 5", "rename these files", "does this
  match my brand", or any mention of SHULL, U#/S#.#, the Anti-AI-Slop Standard, or the
  Teacher Brand. Holds the locked palette, typography, doc-code grammar, file/folder
  routing, connector policy (Higgsfield, Mobbin), and the QA gate every deliverable must
  pass. Other SHULL skills depend on this one.
---

# SHULL Studio — Core Build Engine

This is the shared layer. It does not build a document by itself; it tells every other
SHULL skill *how* to build one, and routes the request to the right specialist.

**Owner:** Matthew Shull · James A. Garfield Local Schools (Ohio)
**Courses:** Chemistry (primary), Physics, Geology

---

## Step 0 — Load the right context, in this order

1. **This file** — brand, routing, QA gate.
2. **The course profile** for whichever course the request names:
   - Chemistry → `shull-chemistry-guidelines`
   - Geology → `shull-geology-guidelines`
   - Physics → `shull-physics-guidelines`
   If the course is ambiguous and the topic doesn't make it obvious, ask. One question.
3. **The Anti-AI-Slop Standard** — treat as a standing constraint on every word written.
   If `ANTI_AI_SLOP_EDUCATOR_STANDARD.md` is in Project Knowledge, search it. If not,
   `references/anti-slop-condensed.md` in this skill carries the operative rules.
4. **The specialist skill** for the deliverable (see routing table below).
5. **The public format skill** for the output type — `/mnt/skills/public/pptx/SKILL.md`,
   `/mnt/skills/public/docx/SKILL.md`, or `/mnt/skills/public/pdf/SKILL.md`.

Do not skip 3. Voice failures are the most common way a SHULL document goes wrong, and
they are invisible until Matt reads it in front of a class.

---

## Routing table

| Request | Route to |
|---|---|
| Slide deck, PowerPoint, presentation | `shull-slide-deck-builder` |
| Guided notes, Cornell notes, notes packet, note-taking scaffold | `shull-guided-notes-builder` |
| Test, quiz, exam, exit ticket, bell ringer, A–D versions | `test-quiz-generator` |
| Practice set, homework worksheet, problem set | `shull-practice-set-generator` (if installed); otherwise build from `assets/shull_brand.css` + the v2 rules in §4 below |
| Unit planning, gap audit, file naming, folder routing, inventory, "what's left" | `shull-course-librarian` |
| Lab handout, pre-lab, post-lab, missed-lab | Course profile §Lab template + this file's brand rules (no dedicated skill yet) |
| Reference sheet, one-page binder insert | This file's brand rules + course profile content |
| Interactive HTML tool, self-check widget, dashboard | `anti-ai` skill + Mobbin (see `references/connectors.md`) |

Several skills can be active at once. A "build me Unit 5" request legitimately runs the
librarian for the plan, then the deck builder, then the notes builder, then the quiz
generator — in that order, because the deck sets the vocabulary the notes and quiz reuse.

---

## 1. Locked brand tokens

| Token | Hex | Use |
|---|---|---|
| Deep Forest | `#1A2318` | Dark backgrounds, banners, number squares |
| Slate Stone | `#2C3B2D` | Secondary dark neutral, chips |
| Moss Green | `#4A7C59` | Primary accent, rules, borders |
| Warm Earth | `#8B6914` | Secondary accent; `#6E5310` at small sizes for grayscale legibility |
| Bio Lime | `#A8C97F` | Highlight / must-write cue — **one per slide, no exceptions** |
| Parchment | `#EDF0E5` | Light background, light text on dark |

**Typography.** Trade Gothic Next is the brand primary. In render environments it is
almost never available, so use the confirmed fallback ladder and don't improvise:
Oswald (display) / Inter or Source Sans 3 (body) → **Poppins (display) / Lato (body)** →
Liberation Sans (body) when Lato is missing. Poppins is present in the render container;
Lato often is not. Never substitute a font not on this ladder.

**Non-negotiable visual rules**

- Grayscale differentiation must never rely on color alone. Vary fill value, outline
  weight, and label together.
- One accent-color word per headline. No gradients on text, ever.
- Atom Seal watermark 12–15% opacity; drop to 8–10% on dense table pages.
- Minimum print weights: box borders ≥ 1px at ~55% gray; writing lines ≥ 0.75pt at ~35% gray.
- No text below 8pt on a student page except the running footer. No student-facing slide
  text below 16pt.
- Dense tabular content uses real tables, not flexbox card grids.

**Ink-saving is the default — this is a hard rule for anything that gets physically
printed** (worksheets, practice sets, guided/Cornell notes, labs, study guides, reference
sheets). Digital-only deliverables (slide decks viewed on a projector/screen) are exempt.

For anything printed:

- Outlined and bordered treatments replace solid fills. No full-page color banners, no
  shaded section backgrounds, no solid-fill headers.
- Color is a thin accent only — a chip outline, a rule line, a small tag, a border — never
  a fill covering more than a small label or icon.
- Table rows: hairline borders, not alternating solid-color shading. If shading is truly
  needed for scanability, use a very light gray tint, never a brand color at full or
  medium saturation.
- Atom Seal watermark: 12–15% opacity normally, drop to 8–10% on dense/tabular pages, and
  consider omitting entirely on a heavily-inked page (a full lab handout, a dense practice
  set) rather than layering it under existing content.
- Number squares, chips, and border-tab labels stay outlined/light-fill on print — the
  solid Deep Forest fill is reserved for slides and digital-only use.
- Full-color variants are preserved as `.bak` or generated on request — never shipped as
  the default print file.

---

## 2. Document code grammar

Every SHULL document carries `U#/S#.#` and it must match the binder tab, the slide footer,
the organizer, and the folder name. They are one system.

**File name:** `SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor].[ext]`

- COURSE: `CHEM`, `PHYS`, `GEO`
- Type: `Slides`, `Guided_Notes`, `Practice_Set`, `Quiz`, `Test`, `Lab`, `Study_Guide`,
  `Reference`, `Key`, `Rubric`
- Unit is zero-padded two digits; section is not (`U08_S8.4`)
- Version letters for parallel forms append at the end: `..._S8.4_A.docx`
- Answer keys are **always separate files** ending `_Key`

**In-document chip:** rounded rectangle, Poppins semibold, letter-spaced, reading
`U10 / S10.4`. Dark fill on light pages, outlined on dark pages. One chip style across
slides, practice sets, labs, quizzes, and notes.

**Number squares:** Deep Forest square, Parchment numeral, ~15pt. Used for problem numbers
and organizer unit numbers. Section markers on dark slide dividers stay circles.

Full folder routing lives in `references/file-routing.md`.

---

## 3. Voice — the short version

Write as a knowledgeable teacher talking to his own 10th–12th graders. Direct, plain,
specific about what to show and turn in. Say "you" and "your group." Reading level ~10th–11th.

Say things like: "Show enough work that I can follow your reasoning." "Include units
throughout." "Be specific — 'it changed' is not an observation."

Never: "Dive into," "embark on a journey," "in today's fast-paced world," "this engaging
activity will," "there are no wrong answers" when answers can be wrong, or a paragraph
explaining the educational value of a worksheet before the directions. Do not label student
copies "easy / medium / hard." Do not invent a story, opinion, or classroom anecdote and
attribute it to Mr. Shull.

Every question, box, heading, and graphic must earn its place. Padding to fill a page is
the failure mode this whole system exists to prevent.

---

## 4. Practice set v2 rules (locked)

Kept here so the format survives even if the dedicated generator skill isn't installed.

- Exactly 8 questions: 2 warm-up / 3 practice / 2 challenge / 1 multi-topic.
- Strict two pages, front and back. Enforced by render + `len(doc.pages) == 2` check.
- Chip-styled dark banner; Deep Forest problem-number squares.
- Tag pills, single thin rule: WARM-UP tinted green fill · PRACTICE white ·
  CHALLENGE tinted earth fill · MULTI-TOPIC solid dark with light text.
- Work boxes carry a border-tab label ("WORK — CARRY UNITS") sitting on the border, not
  floating gray text inside the box.
- `.write` ruled lines; `.math` boxes in `s` / `m` / `l` (0.72 / 0.92 / 1.18 in).
- Bracketed self-check answers for **numeric results only** — never for explanation,
  vocabulary, or graph-reading items. Styled `#6E5310`.
- Multi-part items keep full 10.5pt body size on every part. No part smaller than body.
- Running footer with `PAGE X OF Y`, auto-generated.

Working CSS: `assets/shull_brand.css`. Build helper with page-count enforcement:
`assets/build_pdf.py`.

---

## 5. Connectors

Full policy in `references/connectors.md`. The short form:

- **Default to hand-built graphics** — SVG, HTML, code. This is the Anti-AI-Slop position
  and it applies to nearly everything.
- **Higgsfield** only when a visual genuinely cannot be hand-built: photographic reference
  (lab equipment, rock and mineral samples), 3D-style molecular renders, minimal unit-divider
  art. Verify every output for scientific accuracy before use — wrong bond angles, mislabeled
  equipment, and invented on-image text are its normal failure modes. Confirm with Matt
  before spending credits. Do not generate variants by default.
- **Mobbin** only as a UI/UX pattern reference when building an interactive digital tool
  (Cowork web app, HTML self-check, dashboard). Never for print PDFs, decks, or Word docs.
  Pair with the `anti-ai` skill when translating a pattern into SHULL-branded output.

---

## 6. The QA gate — every deliverable, before it ships

Run this. Report the result in chat as a short checklist, not as prose.

1. **Render and look at it.** PDF → rasterize with `pdf2image` and view the pages. PPTX →
   export to PDF, rasterize, view. Never ship a document you have not seen rendered.
2. **Page budget.** Practice set = exactly 2. Quiz/test = whatever was specified. If over:
   reduce `@page` margins → reduce base font-size → tighten line-height → reduce block
   bottom margins. In that order. Never shrink a single question to fit.
3. **No clipped text.** Scan every rasterized page for text cut off at a box or column edge.
   This has bitten the deck builder before and it is the highest-priority visual defect.
4. **Grayscale check.** Would a photocopy still distinguish the categories? If the only
   difference is hue, fix it.
4b. **Ink check (print documents only — worksheets, guided notes, labs, study guides,
   reference sheets).** Look at the rasterized page and estimate what a printer would lay
   down. Any solid-color fill larger than a small tag, chip, or icon fails this check.
   Full-page banners, shaded backgrounds, and medium/full-saturation table shading fail.
   Fix by converting to outline/border treatment before shipping — this is not a
   nice-to-have, it ships back to the builder.
5. **Codes match.** `U#/S#.#` on the document, in the filename, and in the folder path all
   agree.
6. **Voice pass.** Read the directions aloud in your head. Any sentence that sounds like a
   brochure gets rewritten.
7. **Answer key exists and is a separate file**, if the document has answers.
8. **Every number re-solved independently**, including in each parallel version.

---

## 7. What to do when something is missing

Never invent a unit title, section number, lab, calendar date, policy, or assessment rule
and present it as settled. Either ask Matt, or produce it and label it **PROVISIONAL** in
the teacher notes — never on the student page.

Known open items carried forward: possible missing Chemistry section 9.6; the universal
document-code grammar is not finalized beyond `U#/S#.#`; lab placements beyond Unit 0 are
provisional.

SHULL Studio — Color Decision + Skill Updates
Date: 2026-09-06 · Scope: Slide decks (projection) only, going forward — no retrofit of existing decks.
---
1. Assumption I'm making — please confirm
Use white background on all student filled documents not the full color pallet to save on ink. 
---
2. Primary palette — selected, one per course
Course	Identity	Ground	Neutral	Accent 1	Accent 2
Chemistry	Lab Lime	Asphalt Black `#14161B`	Charcoal `#2A2F33`	Neon Lime `#A3E635`	Aqua `#22D3EE`
Physics	Kinetic	Asphalt Black `#14161B`	Graphite `#2E3338`	Energy Orange `#FF6B1A`	Ice Blue `#3DD6F4`
Geology	Terra Teal	Asphalt Black `#14161B`	Slate `#2C3338`	Mineral Teal `#16B8A6`	Rust Orange `#E85D24`
These come from your first uploaded image (`science_course_color_palettes.png`). Applies to
new slide decks only — U7 and U10 Chemistry decks already built stay as-is, and no
already-built deck gets retrofitted.
---
3. Back-burner reference — the other 6 options, filed not lost
From `5392.jpg`. Kept here so nothing gets lost if you want to swap later.
Chemistry (pick was #3):
Reaction Turquoise — Frosted Turquoise `#76E6D4` / Guava Red `#F45B69`
Element Violet — Electric Violet `#A855F7` / Neon Pink `#FF3D8E`
✅ Lab Lime (selected above)
Physics (pick was #1):
✅ Kinetic Orange (selected above)
Vector Red — Signal Red `#F43F4F` / Cool Gray `#9CA3AF`
Quantum Gold — Solar Gold `#F5B82E` / Deep Purple `#8B5CF6`
Geology (pick was #1):
✅ Terra Teal (selected above)
Volcanic Amber — Molten Amber `#FF8A00` / Garnet Red `#B91C1C`
Crystal Green — Olivine Green `#A3C644` / Stone Gray `#9CA3AF`
Filing: drop this whole file in Drive at `_Brand/Standards/SHULL_Color_Palette_Library.md`
so it's the one place both the pick and the alternates live — not duplicated into three
course folders.
---
4. Skill patch — `shull-studio` (add as new §1a, right after the Locked Brand Tokens table)
```markdown
## 1a. Per-course slide accent palette (digital/projection only — 2026-09)

Each course gets its own dark-ground accent identity for **slide decks only**. Print
documents (worksheets, notes, labs, tests, study guides, reference sheets) are unaffected
and keep the Bio Lime / Parchment system in §1 exactly as locked.

| Course | Ground | Neutral | Accent 1 | Accent 2 |
|---|---|---|---|---|
| Chemistry — Lab Lime | `#14161B` | `#2A2F33` | `#A3E635` | `#22D3EE` |
| Physics — Kinetic | `#14161B` | `#2E3338` | `#FF6B1A` | `#3DD6F4` |
| Geology — Terra Teal | `#14161B` | `#2C3338` | `#16B8A6` | `#E85D24` |

- Applies to **new slide decks going forward only**. Do not retrofit existing decks
  (Chemistry U7, U10) to match.
- The §1 ink-saving rule still governs every printed deliverable regardless of course —
  these accent colors never touch a printed page.
- One accent-color-word-per-headline and grayscale-differentiation rules from §1 still
  apply on slides using this palette.
- Alternate options per course are parked in `_Brand/Standards/SHULL_Color_Palette_Library.md`
  — do not invent a fourth option without checking there first.
