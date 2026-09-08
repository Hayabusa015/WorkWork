---
name: shull-guided-notes-builder
description: >
  Builds SHULL Science guided notes and Cornell notes packets for Matt Shull's Chemistry,
  Physics, and Geology classes at James A. Garfield Local Schools. Use whenever the user
  asks for guided notes, Cornell notes, a notes packet, fill-in notes, a note-taking
  scaffold, an interactive notebook page, or says things like "notes to go with the Unit 7
  deck", "make a Cornell packet for section 4.2", "students need something to write on
  during this lecture", or "turn this deck into notes". Also use to revise scaffolding
  level, add a completed teacher copy, or convert existing notes to the SHULL format.
  Produces a .docx student packet plus a filled teacher copy, keyed one-to-one to the
  section slide deck.
---

# SHULL Guided & Cornell Notes Builder

Requires `shull-studio` (brand, voice, codes, QA gate) and the course profile. Read
`/mnt/skills/public/docx/SKILL.md` before writing build code — output is `.docx` so Matt
can edit it.

---

## The governing idea

The notes and the deck are one object. A student should be able to look at a slide and know
exactly which blank it fills. If the notes introduce a term the deck doesn't show, or the
deck highlights something the notes have no room for, the packet is broken.

**Always ask for or locate the section deck first.** If it doesn't exist yet, either build
it first (route to `shull-slide-deck-builder`) or tell Matt the notes will be provisional
until the deck is set.

---

## Step 1 — Set the scaffolding level

Scaffolding is not fixed. It comes down over the year — that's confirmed course philosophy,
and it's the single decision that most changes what the packet looks like.

| When | Level | What students get |
|---|---|---|
| Units 0–3 | **Heavy** | Cue column pre-filled with the questions; most sentences partially written with 1–3 blanks; worked examples with the setup given and the arithmetic blank |
| Units 4–8 | **Medium** | Cue column half pre-filled; definitions blank but term given; worked examples with the first step given |
| Units 9+ | **Light** | Cue column blank with prompts only; students write full definitions; worked examples blank with the problem stated |

Geology runs one level heavier than Chemistry at the same point in the year. Physics
matches Chemistry unless Matt says otherwise.

If Matt doesn't specify, pick from the unit number and **state the choice in one line** so
he can override it.

## Step 2 — Cornell layout

```
┌──────────────────────────────────────────────────┐
│  BANNER — dark, chip with U#/S#.#                │
│  NAME ______  DATE ____  PERIOD ___              │
├──────────────┬───────────────────────────────────┤
│  CUE         │  NOTES                            │
│  2.0"        │  4.9"                             │
│              │                                   │
│  questions,  │  content, blanks, diagrams,       │
│  terms,      │  worked examples                  │
│  prompts     │                                   │
├──────────────┴───────────────────────────────────┤
│  SUMMARY — 4 ruled lines, bottom of last page    │
└──────────────────────────────────────────────────┘
```

- Left cue column 2.0", notes column 4.9", on letter portrait with 0.6" side margins.
- Vertical rule between columns: Moss Green, 1pt.
- Summary block only on the **last page** of the packet, not every page.
- Body 11pt. Blanks are underscored runs sized to the expected answer — a one-word blank
  and a full-sentence blank should not look identical.
- Name / Date / Period on page 1 only.
- Running footer: `SHULL SCIENCE · [COURSE] · U# / S#.#` left, `GUIDED NOTES · PAGE X OF Y`
  right, 6.4pt Poppins, `#6B7265`.

## Step 3 — Write the content

Mirror the deck's sequence and its vocabulary exactly. Same terms, same order, same worked
examples with the same numbers.

- **Must-write cue.** Anything the deck marked with the Bio Lime block gets a visible marker
  in the notes — a thin Bio Lime left-rule on that line. One marker per corresponding slide.
  This is the connection that makes the two documents feel like one system.
- **Concise bullets, not paragraphs.** If a note line runs past two lines, it's a paragraph
  and needs cutting.
- **Worked examples get a bordered work area**, sized to the actual work. Reuse the `.math`
  sizing logic from the practice-set template: 0.72" / 0.92" / 1.18". A box too small to
  work in is worse than no box.
- **Diagrams are hand-built** and appear as labeled blanks where students annotate — a
  particle diagram with empty label lines, a free-body diagram with blank vectors, a
  cross-section with unlabeled strata. Students should be drawing and labeling, not just
  filling word blanks.
- Leave a `NOTICE THIS` margin note where a common misconception lives. Name the
  misconception plainly: "Students usually multiply here. You divide."

## Step 4 — Teacher copy

Always produce two files:

- `SHULL_[COURSE]_Guided_Notes_U##_S##.#.docx` — student, blanks empty
- `SHULL_[COURSE]_Guided_Notes_U##_S##.#_Key.docx` — every blank filled, worked examples
  completed, summary written as a model

The key is generated from the same source structure so they can't drift out of sync. Do not
hand-write the key separately.

## Step 5 — Differentiation

When asked for it, use the confirmed Modified (M) / Challenge framework:

- **(M)** — more blanks pre-filled, fewer blanks per line, worked examples with the setup
  given. Same content, same terms. Never a shorter or easier set of ideas.
- **Challenge** — an extra cue-column prompt per page asking students to connect the section
  to an earlier unit, plus one extension problem at the end.

Mark the version discreetly in the footer, not in the banner. Students notice banners.

## Step 6 — QA

Render to PDF, rasterize, look at it. Then:

- [ ] Blanks sized to expected answers, not uniformly
- [ ] Every deck term appears; no term appears that isn't on a slide
- [ ] Work areas big enough to actually work in
- [ ] Summary block on last page only
- [ ] Bio Lime must-write markers match the deck's highlight blocks, one per slide
- [ ] `U#/S#.#` in banner chip, footer, and filename all match
- [ ] Key filled completely and consistent with the student copy
- [ ] Nothing below 8pt except the footer
- [ ] Ink-conscious: outlined boxes, no solid fills on student pages

## Step 7 — Deliver

Both files to the section's `Guided Notes/` folder. Present them. Then say in two lines what
scaffolding level you used and why, so Matt can push it up or down.
