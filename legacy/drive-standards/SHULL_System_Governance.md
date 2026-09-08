# SHULL System Governance

**Owner:** Matthew Shull · James A. Garfield Local Schools
**Applies to:** Chemistry, Physics, Geology — all three Claude Projects
**Status:** CONFIRMED. This file is the tiebreaker when two sources disagree.
**Upload to:** Project Knowledge in all three course projects. Identical copy in each.

---

## 1. The one rule

**A fact lives in exactly one place.**

Every conflict in this system so far came from the same fact being written twice — the
Geology palette sat in both the export and the skill file, the curriculum map sat in both,
and when one changed the other went quietly stale. Duplication is the defect. Not
forgetting to update, not disorganization — duplication.

So: two layers, hard line between them, nothing written in both.

---

## 2. The two layers

### Layer 1 — SKILLS own the build

Anything about *how* a document is made. Course-independent. Changes once or twice a year.

- Brand: palette hexes, typography ladder, watermark, chip and number-square styles
- Layout: margins, grid, reserved-height rule, page budgets, line caps
- Structure: Cornell packet anatomy, practice-set v2 shape, slide-type library
- Design philosophy: ink-saving, grayscale-safety, one accent word per headline
- UI and interactive: HTML tool patterns, connector policy (Higgsfield, Mobbin)
- Doc-code grammar: `U#/S#.#`, filename pattern, folder routing
- The QA gate
- Voice and the Anti-AI-Slop rules

Files: `shull-studio`, `shull-slide-deck-builder`, `shull-guided-notes-builder`,
`test-quiz-generator`, `shull-practice-set-generator`, `shull-course-librarian`, `anti-ai`.

### Layer 2 — PROJECT KNOWLEDGE owns the course

Anything about *what* is taught in one specific class. Course-specific. Changes constantly.

- Curriculum map: unit titles, unit numbers, section codes, section order
- Pacing, calendar dates, grading deadlines
- Policies: grading weights, late work, retakes, quiz cadence
- Population and rigor level
- Assessment shape for that course (single-day vs. split, MC weighting)
- Lab and activity philosophy for that course
- Reference packet contents
- Real-world connection themes
- Every generated science material — decks, notes, practice, tests, labs

Files: one `*_DECISIONS.md` per course, plus the generated materials.

### The line, stated as a test

> If changing it would affect **all three courses**, it's a skill.
> If changing it would affect **one course**, it's Project Knowledge.

A thinner summary-box border is a skill change. Moving Plate Tectonics from U4 to U5 is a
Project Knowledge change. The color of the summary-box border is a skill change *unless a
course has its own palette* — which Geology does, so the Geology palette is the one
declared exception below.

---

## 3. Precedence — what wins

1. Matt's direct instruction in the current conversation
2. **For course facts:** the course `*_DECISIONS.md` in Project Knowledge
3. **For build mechanics:** the skill file
4. Anything labeled CONFIRMED over anything labeled CARRIED OVER or PROVISIONAL
5. Newer dated entry over older

When a skill file states a course fact and the decisions file disagrees, the decisions file
wins and **the skill is reported as stale** — it does not get silently obeyed and it does
not get silently ignored. It gets flagged in the fix list.

When the two layers genuinely overlap and it isn't clear which is which: stop and ask. One
question. Do not guess and do not build on the guess.

---

## 4. Course skills must point, never restate

A course guidelines skill (`shull-chemistry-guidelines`,
`shull-physics-guidelines`, `shull-geology-guidelines`) exists to say *how this course
differs in build terms* — rigor level, which document types it uses, which brand exceptions
apply. It must not carry the curriculum map, the calendar, the grading policy, or the
section list.

Where it currently does, replace the content with a pointer:

> **Curriculum map.** Lives in `GEO_DECISIONS.md` in this project's Knowledge. Read it
> there. Never build against a unit or section code that isn't in that file.

That single change is what stops you from having to touch a skill every time you adjust
the course.

---

## 5. Making a change — the two paths

### Path A: course change (most of them)

You say it in chat. I write the dated entry and hand you the updated `*_DECISIONS.md`.
You drop it into that project's Knowledge, replacing the old copy. Under a minute. No
skill is touched.

Entry format — append to the top of the log, never edit history:

```
### 2026-09-05 — Unit numbering
Plate Tectonics is U5, not U4. Glaciers U9. Resources U10.
Supersedes: shull-geology-guidelines §5.
Status: CONFIRMED
```

The `Supersedes:` line is what makes drift visible instead of silent.

### Path B: build or brand change (rare)

You say it in chat. I tell you which skill owns it and hand you the revised skill file to
re-upload in Customize → Skills. Because a skill reinstall has already wiped user edits
once, the packaged file you re-upload is the real copy — the live one is a cache.

If a change touches both layers, it gets split into two edits and you're told which is
which.

---

## 6. Checks and balances

### Check 1 — every librarian invocation

The librarian already runs a Project Knowledge audit on every call. It now also checks
layer violations: a course fact sitting in a skill, a build rule sitting in Project
Knowledge, and any fact appearing in two places. Reported as a table with a Fix column.

### Check 2 — before any build

Before producing a document, confirm the unit and section code exist in that course's
decisions file. If they don't, stop and ask. Never build against a code from a skill file
alone. This is the check that would have caught the U4/U5 Plate Tectonics problem before a
packet was printed with the wrong footer.

### Check 3 — the scheduled drift sweep

One recurring task per course project, staggered so at most one report lands per morning:

> Run the SHULL drift check for this project. Compare the course skill against this
> project's decisions file. Report only: facts stated in both places, facts that disagree,
> and any decisions-file entry with no matching material built yet. Report as a fix list.
> Do not apply anything.

Output is always the same shape — a numbered list of things to fix, shortest first. If
nothing drifted, one line saying so.

### Check 4 — the fix list format

Every audit output uses this and nothing else. No prose, no preamble.

| # | File | Problem | Your action | Time |
|---|---|---|---|---|
| 1 | `shull-geology-guidelines` §7 | Palette contradicts decisions file | Re-upload trimmed skill | 2 min |

Sorted by blocking first, then by how long the fix takes. Anything over ten minutes gets
broken into smaller rows.

---

## 7. What I cannot do — stated plainly so you don't build on it

- I cannot write to Project Knowledge. Every update is a file you upload.
- I cannot write to installed skills. Same.
- Nothing propagates on its own. There is no background sync.
- Past-chat search cannot cross project boundaries, so each course must be swept separately.

What I *can* do is never let a drift go unreported, and always hand back a finished file
rather than a description of what you should change. The manual step is the upload, not the
authoring.

---

## 8. Migration — what has to move, per course

This is the current fix list. Work top to bottom; each row is independent.

### Geology — three blocking conflicts

| # | File | Problem | Action |
|---|---|---|---|
| 1 | `shull-geology-guidelines` §5 | Unit map says Plate Tectonics U4, Glacial U8, Oceans U9. Working record says U5, U9, U10 — a one-unit offset from U4 on. Blocks every TBD code. | Confirm the real numbering, then move the map to `GEO_DECISIONS.md` and cut §5 to a pointer |
| 2 | `shull-geology-guidelines` §7 | Says palette is identical to Chemistry. Geology export §8A confirms the earth palette (Canyon Umber, Basalt Brown, Rust Red, Amber Ochre, Sage Moss, Sandstone). Built U1 packet already uses it. | Cut §7's palette table; add the Geology palette to `shull-studio` §1 as the one declared course exception |
| 3 | `shull-geology-guidelines` §3 vs. built U1 materials | Skill says never use Gizmos. U1 S1.2 notes and a built worksheet both use the Red Shift Gizmo. | Decide: keep as a named exception, or replace the activity |
| 4 | `SHULL_Geology_Claude_Project_Export.md` §5 | Says the curriculum map is INCOMPLETE. It isn't. | Superseded by `GEO_DECISIONS.md` — remove once that file exists |
| 5 | All `GEO_*` filenames | `GEO_U1_S1.2-S1.4_Guided_Cornell_Notes.docx` should be `SHULL_GEO_Guided_Notes_U01_S1.2.docx` | Batch rename after unit numbering is settled — not before, or it gets done twice |

### Chemistry — content sitting in the skill

| # | File | Problem | Action |
|---|---|---|---|
| 1 | `shull-chemistry-guidelines` §4 | Full Units 0–15 curriculum map | Move to `CHEM_DECISIONS.md`, replace with pointer |
| 2 | `shull-chemistry-guidelines` §7 | 2026–2027 calendar and pacing guide | Move to `CHEM_DECISIONS.md` |
| 3 | `shull-chemistry-guidelines` §§I, J, G, H | Grading rubric, late-work scale, quiz and test structure | Move to `CHEM_DECISIONS.md` |
| 4 | `shull-chemistry-guidelines` §6 | Reference packet contents | Move to `CHEM_DECISIONS.md` |
| 5 | `shull-chemistry-guidelines` §12 | Brand section duplicates `shull-studio` §1 | Cut entirely — the studio owns brand |
| 6 | `shull-chemistry-guidelines` §§10, 11 | Lab template and graphing rules | Keep in the skill. These are build structure, not course content |
| 7 | Chemistry section 9.6 | Binder header says six sections, only 9.1–9.5 listed | Confirm or close — carried open since install |

### Physics — mostly empty, so start clean

| # | File | Problem | Action |
|---|---|---|---|
| 1 | `shull-physics-guidelines` §3 | Unit and section map marked NEEDED. Architecture v2 says a map PDF and pacing guide exist. | Confirm which is true; if the map exists, it goes straight into `PHYS_DECISIONS.md` |
| 2 | `shull-physics-guidelines` §2 | Course identity is PROVISIONAL | Confirm population and rigor, move to `PHYS_DECISIONS.md` |
| 3 | `shull-physics-guidelines` §5 | Vectors, sign conventions, graph reading, misconception distractors | Keep in the skill. Discipline build rules, not course content |
| 4 | `shull-physics-guidelines` §4 | Shared standards CARRIED OVER from Chemistry | Delete. They belong to `shull-studio` and are duplicated here |

### All three projects

| # | File | Problem | Action |
|---|---|---|---|
| 1 | `SHULL_Design_Refinements_v2.md` | Absorbed verbatim into `shull-studio` §4 | Remove from Knowledge |
| 2 | `SHULL_Studio_Install_and_Architecture.md` | Superseded by Architecture v2 | Remove from Knowledge |
| 3 | `README (2).md` | Says build decks from `build_standard.js`; v2 says build from the template | Remove from Knowledge |
| 4 | `Guided_Notes_-_Plates.docx` | Legacy conversion input, already rebuilt | Remove from Knowledge |
| 5 | `shull-studio` missing files | `references/connectors.md`, `references/file-routing.md`, `references/calendar-2026-2027.md`, `assets/shull_brand.css`, `assets/build_pdf.py` are all referenced by the skill and none are installed | Rebuild and repackage the skill, or fold the content into `SKILL.md` |

---

## 9. Decisions file template

One per course. Newest entry at the top of the log. Sections above the log hold current
state; the log holds how it got there.

```markdown
# [COURSE] Course Decisions
**Owner:** Matthew Shull · Last updated: YYYY-MM-DD
**Authority:** This file wins over any course fact stated in a skill file.

## Curriculum map
[units and section codes — the only authoritative copy]

## Calendar and pacing
## Policies
[grading weights, late work, retakes, quiz cadence]
## Assessment shape
## Activity and lab philosophy
## Reference packet contents
## Course brand exceptions
[normally empty — Geology's palette is the only current one]

## Open questions
[numbered, each with what it blocks]

## Decision log
### YYYY-MM-DD — [topic]
[what changed] · Supersedes: [file §] · Status: CONFIRMED
```

---

## 10. Why this shape

You said you need the system to organize itself, and where it can't, to hand you a clear
list. It can't organize itself — I can't write to either layer. So the design compensates
the other direction: make drift *impossible to miss* rather than impossible to happen.

Three things do that work. One home per fact, so drift is rare. A code check before every
build, so drift can't reach a printed page. A scheduled sweep with a fixed fix-list format,
so when drift does happen it arrives as a short numbered list instead of a discovery
mid-project.

The upload step stays manual. Everything else is on me.
