---
id: SHULL-CHG-0023
title: Guided notes are strictly recall — the cue column names, it does not ask
status: IMPLEMENTED
opened: 2026-09-20
decided: 2026-09-20
source: User
decided_by: Matthew Shull
---

# SHULL-CHG-0023 — Guided notes are recall

## What he asked for

> "For notes: I dont want questions about the slides in the guided notes. I wanted guided notes
> just for them to write what is on the slide. Its strictly recall. Record the definition, record
> the table, record the steps, record the concept etc."
>
> — 2026-09-20, opening with "I thi k we had a discussion about this and I see it again."

## Why it came back

It had never been written down. Searching the repository for the rule returns nothing; searching
for its opposite returns four places, all of them authoritative-looking:

| Where | What it said |
|---|---|
| `templates/notes/README.md` §structure | "The cue column is questions the student should be able to answer from the notes beside them." |
| `templates/notes/specs/phys_u01_s01.1-s01.4.json` → `howItWorks` | "The left column holds the questions you should be able to answer… Cover the right side and quiz yourself with it later." |
| `templates/notes/specs/geo_u01_s01.2-s01.4.json` → `howItWorks` | "The left column asks the questions you should be able to answer…" |
| `scripts/build_template_previews.py` → gallery blurb | Same sentence again, shown in the app's Template gallery. |

Both example specs were built to that description: **45 of 50 cue prompts were literal questions**,
and the Geology packet carried **12 more on the notes side** ("How long ago did the Big Bang
occur?" where a student needs a line reading "The Big Bang: about ______ years ago.").

Those specs are what the Designer agent copies when it writes a new packet. The defect was not one
packet — it was the example teaching itself forward.

`SHULL-CHG-0018` is the only prior cue-column record and it is about **geometry** (the 1.28in
split), not content. So this is new ground, not a contradiction.

## Current Rule

`templates/notes/README.md`: "The cue column is questions the student should be able to answer from
the notes beside them."

## Proposed Rule

**A guided-notes packet is strictly recall.** It is the page a student fills in while the slide is
up. The cue column **names the thing to record** — a definition, a table, a sequence, a concept —
and never asks for it. No question mark, and no interrogative opener, in a cue or a notes line.
Questions about the material belong in a practice set or a quiz.

| Was | Is |
|---|---|
| "What is a singularity?" | "Definition — singularity" |
| "What 3 pieces of evidence support the Big Bang theory?" | "The three pieces of evidence" |
| "Put the steps of nebular theory in order." | unchanged — an instruction to record is not a question |
| "How long ago did the Big Bang occur?" *(notes side)* | "The Big Bang: about ______________ years ago." |

**Supersedes:** `templates/notes/README.md` §"The structure, and why it is this way", first bullet.

## Mechanism, not documentation

- `templates/notes/recall.py` is the one place the rule lives. **Both renderers import it and
  refuse** a spec with a question in a cue or a notes line, naming each one.
- `scripts/validate_notes.py` walks every spec in the repository, so a bad example is caught
  without anyone building it. Added to `scripts/hook-validate.sh`.
- The two example specs were rewritten: 59 strings, every cue and every notes-side question.
- The student-facing "how these notes work" box now reads "The left column names what to record.
  Write it on the right while the slide is up." The cover-and-recall study use is kept — it works
  better against labels than against questions.

## Carried with it

**The two-ruled-lines rule was keyed to a question mark** (`a note line ending in ? gets two ruled
lines`) and became unreachable the moment questions were banned. Re-keyed: a line ending in `:` is
a label the student writes *under* — `Define protostar:`, `Core:` — and gets two lines; a line with
its blanks inline gets one. `recall.ruled_lines()` is the one place it is decided.
**This changes his packets' layout**, which is why it is called out rather than folded in.

## Deliberately out of scope

Not touched, because they are the student reflecting on their own notes rather than being quizzed
on a slide — flag if any of these should also go:

- the closed-notes **section summary box**,
- the per-section **self-check** ("I can put all 6 stages of nebular theory in the correct order"),
- the **"still fuzzy on"** prompt that closes the packet.

## Risk

**Low.** Both packets rebuild, page counts unchanged (Geology 5, Physics 7), ink inside budget
(Geology 3.82% worst / Physics 4.22%, 12% budget, no solid band). No standard, agent or course
decisions file is touched. Affects all three courses equally; no course-specific carve-out.

## Verification

- `python3 scripts/validate_notes.py` — 2 specs, clean.
- `bash scripts/hook-validate.sh` — validators clean.
- `npm test` — 36 pass.
- Both packets rebuilt and page 3 of the Geology packet read at 100 dpi.
- Gallery previews regenerated; the Template gallery now shows a recall packet.

**Implemented By:** 3cc19ef3a10a657aab70bbe60e172c49c6b7cbf6
**Verified:** yes — validators clean, 36 node tests pass, both packets rebuilt and read, page counts unchanged (Geology 5, Physics 7), ink inside budget.

## Also found, not fixed here

`templates/notes/build_notes.py` carries its own copy of `known_sections()` rather than importing
the one in `templates/_shull_docx.py` — the same regex written twice. Not touched because it is
unrelated to this change, but it is the defect this repository exists to prevent.
