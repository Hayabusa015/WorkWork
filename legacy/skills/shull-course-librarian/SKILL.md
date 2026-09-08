---
name: shull-course-librarian
description: >
  Plans, tracks, files, and maintains Matt Shull's SHULL Science materials library across
  Chemistry, Physics, and Geology at James A. Garfield Local Schools. Use for anything about
  the library rather than a single document: unit build plans, "what's left for Unit 5",
  coverage/gap audits, file naming and folder routing, inventory, pacing against the
  2026-2027 calendar and grading deadlines, brand consistency sweeps, batch conversion of
  legacy files, or auditing Project Knowledge for stale/superseded/conflicting files. Trigger
  on "what's left to build", "plan out Unit 3", "audit my folder", "rename these", "am I on
  pace for MP2", "where does this file go", "check for brand consistency", "audit my project
  knowledge", or "clean up my files". Orchestrates other SHULL skills once a plan becomes
  production. Every invocation runs the standing Project Knowledge audit below.
---

# SHULL Course Librarian

The planning and maintenance layer. Everything else builds one document; this one decides
*which* documents to build, in what order, and whether the ones that exist still match —
and whether the reference material Claude is reading from is even still true.

Requires `shull-studio` and the relevant course profile.

---

## Standing directive — Project Knowledge audit (runs on every invocation)

This is not a fifth job Matt has to ask for. Every time this skill fires — for any of the
four jobs below — silently run this check first and fold the result into the response. If
it turns up nothing, say so in one line. If it turns up something, report it before doing
the job Matt actually asked for; a stale file can invalidate the work about to be done.

**What to check, for every file currently in this project's Knowledge:**

1. **Absorbed content.** Has a document's content been fully locked into a skill since it
   was uploaded? Check the running list in "Known absorptions" below first, then look for
   the general pattern: a project-knowledge file whose rules now read like a subset or
   earlier draft of something `shull-studio`, a course profile, or a builder skill states
   as locked/confirmed.
2. **Contradicted status.** Does the file assert something as missing, blocking, pending,
   or unresolved that newer project knowledge (a later upload, a confirmed decision) now
   contradicts? The classic tell is language like "does not exist yet," "is blocking,"
   "not yet supplied," or "INCOMPLETE" sitting next to a file that clearly resolves it.
3. **Superseded versions.** Is there a `_v2`, "refinements," or "addendum" file whose
   changes have since been folded into a locked skill spec, making the standalone version
   redundant rather than authoritative?
4. **Orphaned scope creep.** A doc from another course's project (e.g., a Chemistry export
   sitting in the Physics project) that duplicates a skill file rather than serving a
   deliberate cross-reference purpose. Ask rather than assume which it is.
5. **Internal conflicts.** Two Knowledge files that state different values for the same
   thing (a palette hex, a grading weight, a policy number) with neither marked superseded.

**Known absorptions (update this list whenever a new one is confirmed):**

| Project Knowledge file | Absorbed into | Status |
|---|---|---|
| `SHULL_Design_Refinements_v2.md` | `shull-studio` §4 (Practice set v2 rules, verbatim) and `shull-slide-deck-builder` (clipping/reserved-height rule) | Fully superseded — flag for removal |
| `PHYSICS_Unit_Map_Request.md` | Resolved by `SHULL_Physics_Unit_Map_1.pdf` + `SHULL_Physics_Pacing_Guide_20262027.pdf` | Contradicted/resolved — flag for removal |
| `SHULL_Studio_Install_and_Architecture.md` — "One blocking item" section | Same as above | Contradicted — flag that one section, file otherwise fine as an install log |
| `SHULL_Chemistry_Claude_Project_Export.md` (when found in the Physics project) | Overlaps `shull-chemistry-guidelines` skill | Ask whether it's an intentional cross-reference chassis or leftover — don't assume |

**Reporting format** — a short table, not prose:

| File | Issue | Recommended action |
|---|---|---|
| `example.md` | Fully absorbed into `shull-studio` §4 | Remove |

**Hard limits:**

- Never delete, edit, or silently ignore a Project Knowledge file. This skill can only
  *read* Project Knowledge and *report* — it cannot write back to it. Removal happens in
  Matt's Project Knowledge settings, not here.
- Never treat "flagged for removal" as done until Matt confirms and removes it. If the same
  stale file turns up again next time, flag it again — don't assume silence meant yes.
- When a new absorption is confirmed during a conversation, say so and note that the
  "Known absorptions" table above should be updated the next time this skill file is
  revised and re-uploaded.

---

## Four jobs

### 1. Unit build plans

Given a unit, produce the full material list and a build order. Read the unit's section list
from the course profile — never invent sections.

**Build order within a section**, and the reason for it:

1. **Slide deck** — sets vocabulary, worked examples, and the must-write items
2. **Guided notes** — keyed to the deck, one-to-one
3. **Practice set** — reuses the deck's worked-example patterns at higher difficulty
4. **Lab or activity** — placed where the section's content supports it
5. **Quiz** — draws only from what the deck and practice set covered
6. **Study guide** — after the last section of the unit
7. **Unit test A–D + keys + item analysis** — last

Nothing later in the list should introduce a term that doesn't appear earlier in it. That's
the whole point of the order, and it's the first thing to check on a gap audit.

Deliver the plan as a table: section, document type, filename, status, dependency. Not prose.

### 2. Gap and coverage audits

Given a course or unit folder, report what exists, what's missing, and what's inconsistent.

Check for:

- Missing document types against the build list above
- Filename convention violations (`SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor].[ext]`)
- Folder routing violations — near-duplicate folders like `Tests` beside `Tests-Quizizz`
- Code mismatches: the `U#/S#.#` on the document vs. the filename vs. the folder path
- Missing answer keys (every assessment and practice set needs one, as a separate file)
- Missing A–D versions where the course profile requires them
- Orphans: a practice set with no corresponding deck, a quiz covering an unbuilt section
- Redundant duplicates. `SHULL_Chemistry_Claude_Project_Export.md` in Chemistry Project
  Knowledge duplicates the `shull-chemistry-guidelines` skill file and is flagged for manual
  removal.

Output a table with a Fix column. Then ask which fixes to run — don't batch-rename anything
without confirmation, because renames break links Matt may have elsewhere.

### 3. Filing and naming

Resolve Course → Unit → Section → content-type before saving anything. Full rules in
`shull-studio/references/file-routing.md`. Reuse existing folders case-insensitively. If the
unit or section is unclear, ask — never default to a misc folder.

For batch conversion of legacy files: work in **unit batches**, uploaded directly to chat.
Project Knowledge is for standing reference documents — specs, standards, guidelines — not
one-time conversion inputs.

### 4. Pacing and deadlines

Check build progress against the course pacing guide and the grade-reporting calendar in
`references/calendar-2026-2027.md`. Flag when a unit's assessments won't exist before the
grades-due date that would need them.

---

## Consistency sweep

When asked to check finished materials against the brand, run this and report as a table —
document, defect, severity, fix:

| Check | Looking for |
|---|---|
| Palette | Off-brand colors; more than one accent word per headline; gradients on text |
| Type | Anything under 8pt on print / 16pt on slides; fonts outside the confirmed ladder |
| Grayscale | Categories distinguished by hue alone |
| Ink | Solid fills on student print pages that should be outlined |
| Chips | Chip style drifting between document types |
| Codes | `U#/S#.#` present on every page and matching everywhere |
| ID fields | Name / Date / Period present on every student document |
| Footers | Auto-generated running footer with page count |
| Keys | Every answer-bearing document has a separate key file |
| Voice | Banned phrasing from the Anti-AI-Slop Standard; padding; motivational filler |

Severity: **blocking** (student-facing error, wrong science, unreadable print) ·
**should-fix** (brand drift, inconsistency) · **nice-to-have** (polish).

---

## Standing open items

Carry these forward and surface them when relevant. Don't resolve them silently.

- Possible missing Chemistry section 9.6 — unconfirmed
- Universal document-code grammar not finalized beyond `U#/S#.#`
- Lab placements beyond Unit 0 are provisional
- Physics unit/section map not yet supplied (see `shull-physics-guidelines`)
- Reference sheet queue, prioritized: Sig Figs / Sci Notation / Metric Conversion Toolkit →
  Types of Chemical Reactions → Electron Configuration → then Periodic Trends, Lewis Dot,
  IMFs, Le Châtelier's, Nuclear Decay, Acid-Base Quick Reference
- Lab equipment packet: volumetric flask photo needs a reshoot; 11 items still on line art

---

## Orchestration

When a plan becomes production, hand off in order and don't try to build everything in one
pass. One section at a time, each document QA'd before the next starts. State which skill
you're routing to and why.

A "build me all of Unit 5" request is a plan first. Show the plan, get a yes, then build.
