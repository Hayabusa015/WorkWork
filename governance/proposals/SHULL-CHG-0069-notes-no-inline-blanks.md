# SHULL-CHG-0069 — Guided notes: no inline fill-in blanks (prompt + open lines)

> **Change ID is provisional.** Taken as the next integer after `SHULL-CHG-0068`, the highest ID in
> the local `governance/proposals/` on 2026-11-11 (no 0069 or higher exists locally). The Secretary
> session that wrote this record has no git tool. It could not `git fetch origin main` and cannot
> push or commit. Under `governance/CHANGE_CONTROL.md` §2 this ID is **not allocated** until someone
> checks it against a freshly fetched `origin/main` and pushes the record there. If `SHULL-CHG-0069`
> already exists on `origin/main`, renumber this file before pushing it.
>
> **No conflict with a LOCKED rule found.** The rules this replaces are labelled INHERITED (blank
> sizing, `docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md` line 255) or come from an IMPLEMENTED record
> (SHULL-CHG-0023's model line). The Physics scaffolding index it touches is an open question
> (CONFLICT-20), not settled. This record does not resolve CONFLICT-20.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0069 (provisional, see banner) |
| **Date** | 2026-11-11 |
| **Source** | User. Said by Matt on 2026-11-11 while reviewing the Physics U3 guided notes; relayed to the Secretary by the main session. |
| **Current Rule** | See section 2. In short, five places assume inline blanks: `brand/SHULL_DESIGN_SYSTEM.md` §11 line 275; `.claude/skills/build-document/SKILL.md` line 128; `standards/QA_GATE.md` line 118; SHULL-CHG-0023's model notes line; and `templates/notes/recall.py` `ruled_lines()` lines 80-90. |
| **Proposed Rule** | See section 3. |
| **Supersedes** | `brand/SHULL_DESIGN_SYSTEM.md` §11, first bullet (line 275-276). `.claude/skills/build-document/SKILL.md` "Guided notes" paragraph, sentence at line 128-129. `standards/QA_GATE.md` "Guided notes" line 118 ("blanks sized to the expected answer"). `templates/notes/recall.py` `ruled_lines()` docstring and the one-line case for inline blanks (lines 86-87, 90). SHULL-CHG-0023 "Proposed Rule" table, last row (line 60), as a model only; the recall rule itself stands. |
| **Reason** | Matt, 2026-11-11: "I just really dont like fill in the blanks" and then "I thought we made this rule in my repo a while ago". No such rule exists (main session's search, checked here: section 2). The current rules do the opposite and assume inline blanks. Offered three alternatives, he chose **"Prompt + open lines"**. This is the same pattern as SHULL-CHG-0023: a preference he believes was recorded, never written down, so the opposite keeps returning. Related but not the same: SHULL-CHG-0032 (line 105) quotes him: "Don't just needlessly add more boxes to fill in... reduce length of notes". |
| **Affected Agents** | Designer (writes notes specs), Auditor (QA gate check), Librarian (none, no filename or Drive change). |
| **Affected Skills** | `build-document` (guided notes paragraph). |
| **Affected Courses** | Open question 1. As said, Physics (he was reviewing Physics U3). If it applies to all three, it is a standard (CLAUDE.md §2 test). |
| **Risk** | Medium. Rule text is a few lines, but it changes the layout of every guided-notes packet, adds page length (open lines take more room than an inline blank), and puts the three existing U1 packets out of compliance (section 5). Interacts with the "reduce length of notes" instruction in SHULL-CHG-0032. |
| **Recommendation** | Approve, after Matt answers the two questions in section 6. Answer 1 decides whether this is Path B (standard, all three courses) or a Physics-only course decision. Answer 2 decides how much of the renderer changes. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

---

## 1. What Matt said (verbatim, 2026-11-11, as relayed by the main session)

> "I just really dont like fill in the blanks"
>
> "I thought we made this rule in my repo a while ago"

Offered three alternatives, he chose **"Prompt + open lines"**:

- Each notes block shows a short cue naming what to record (recall-only, per SHULL-CHG-0023), with
  ruled lines beside it sized to the answer, and the student writes the slide's idea.
- Worked examples keep `Given:` / `Find:` plus the work box, with an `Answer:` line instead of inline
  blanks.

## 2. Current Rule (verbatim, citations checked 2026-11-11)

| # | Where | Text |
|---|---|---|
| a | `brand/SHULL_DESIGN_SYSTEM.md` §11 "Documents", lines 275-276 | "Blanks are sized to the expected answer. A one-word blank and a full-sentence blank must not look identical." |
| b | `.claude/skills/build-document/SKILL.md`, Guided notes paragraph, lines 128-129 | "Blanks are sized to the expected answer; a one-word blank and a full-sentence blank must not look identical." |
| c | `standards/QA_GATE.md`, "Guided notes", lines 116-118 | "... every section starts on a new page and ends with a RECALL block (a summary prompt plus a self-check; SHULL-CHG-0033) · blanks sized to the expected answer." |
| d | `governance/proposals/SHULL-CHG-0023-notes-are-recall.md`, Proposed Rule table, line 60 | Model notes line: "The Big Bang: about ______________ years ago." (also quoted at line 35 as "The Big Bang: about ______ years ago.") |
| e | SHULL-CHG-0023 "Carried with it", lines 77-80, and `templates/notes/recall.py` `ruled_lines()`, lines 80-90 | "A line with its blanks inline is filled in place and takes one." Code: `return 2 if body.endswith(":") else 1`. |
| f | `courses/physics/DECISIONS.md`, Open questions, item 4, lines 190-193 | "**Notes-scaffolding index.** The guided-notes ladder is indexed to unit number — heavy U0–3, medium U4–8, light U9+. ... Re-indexing to *fraction of course elapsed* is proposed but is Matt's call. (CONFLICT-20)" Open, not settled. |

The rule in rows a-c is INHERITED from the legacy system (`docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md`
line 255, X-01 §6.2; `docs/SKILL_MIGRATION_MAP.md` line 215). Those two `docs/` files are analysis
records and are not edited by this change.

Note: rows a and b restate the same fact in two authoritative-looking places. That duplication is
noted, not fixed here (CLAUDE.md §1). On implementation, the skill should point at the standard
rather than restate it.

## 3. Proposed Rule (verbatim, not adopted)

> **Guided-notes packets use no inline fill-in blanks.** Each recall item is a cue naming what to
> record (SHULL-CHG-0023) plus ruled writing lines sized to the answer. The student writes the
> slide's idea in their own hand on those lines. The filled key prints the full statement in the
> same lines. Worked examples keep `Given:` / `Find:` and the open work box (never ruled lines), and
> end with an `Answer:` line instead of inline blanks.

Header fields (`NAME ____  DATE ____  PERIOD ____`, `templates/notes/README.md` line 187) are not
recall items and are not affected.

Scope of "blank" (inline underscores only, or also example answer lines and `fillin_table` cells)
is open question 2. The wording above will be adjusted to his answer before approval.

## 4. Files a change would touch (listed, not edited)

| File | Location | Change |
|---|---|---|
| `brand/SHULL_DESIGN_SYSTEM.md` | §11, line 275-277 | Replace the "blanks sized" bullet with the cue-plus-lines rule (or a pointer to the standard). Line 277 "Answer blanks that are clearly too small" becomes "writing lines too few for the expected answer are a defect". |
| `standards/QA_GATE.md` | line 118 | Replace "blanks sized to the expected answer" with "no inline blanks; each recall item has ruled lines sized to the key's answer". |
| `.claude/skills/build-document/SKILL.md` | lines 128-129 | Replace the restated blank rule with a pointer to the standard. |
| `templates/notes/README.md` | layout/schema sections (e.g. line 211, `"answer": "… = _____"` in the worked-problem example) | Update schema examples and prose to cue plus lines; worked-problem `answer` becomes an `Answer:` line. |
| `templates/notes/recall.py` | `ruled_lines()`, lines 80-90 | Remove the one-line inline-blank case; line count sized to the key's answer. Optionally add a check that refuses a notes line containing a run of underscores, the same way questions are refused (mechanism, not documentation, as in SHULL-CHG-0023). |
| `templates/notes/build_notes_docx.py` | worked problem `answer` render (line 588-589); `fillin_table` call (line 607) | Render an `Answer:` line; `fillin_table` only if question 2 says tables count. |
| `templates/_shull_docx.py` | `fillin_table()`, line 555 | Only if question 2 says tables count. |
| `scripts/validate_notes.py` | spec walker | Picks up the new refusal from `recall.py`; no separate rule. |
| `courses/physics/DECISIONS.md` | Open question 4, lines 190-193 | Only if Matt wants the "heavy U0–3" scaffolding description restated in terms of cue-plus-lines. This record does not resolve CONFLICT-20. If he says Physics-only (question 1), the rule itself goes here as a dated decision-log entry instead of in the standard. |
| `templates/notes/specs/*` | example and built specs | Rewritten to comply (section 5). |
| `change-log/CHANGELOG.md` | index | Row added at implementation. |

## 5. Existing packets that would no longer comply

Counted as lines with a run of four or more underscores in the spec files, 2026-11-11:

| Packet | Spec | Underscore runs |
|---|---|---|
| Chemistry U1 | `templates/notes/specs/chem_u01_s01.1-s01.5_notes_student.json` (+ `make_chem_u01_s01.1-s01.5_notes.py`) | 4 (+3 in generator) |
| Physics U1 | `templates/notes/specs/phys_u01_s01.1-s01.4.json` | 38 |
| Geology U1 | `templates/notes/specs/geo_u01_s01.2-s01.4.json` | 13 |
| Physics U3 (in progress) | `templates/notes/specs/phys_u03_s03.1-s03.6_notes_student.json` (+ `make_phys_u03_s03.1-s03.6_notes.py`) | 62 |

Counts include header fields, so they overstate recall blanks slightly. Rebuilding the printed copies
in Drive is a separate task once the rule is approved; Drive objects are not touched by this record.
Whether to retrofit U1 packets or apply going forward only is Matt's call (it may be folded into
question 1 or asked after).

## 6. Questions for Matt

1. **All three courses, or Physics only?** By the CLAUDE.md §2 test, if it applies to all three it is
   a standard (Path B: brand, QA gate, skill, templates). If Physics only, it is a course decision in
   `courses/physics/DECISIONS.md` (Path A), and the standard keeps its blank rule for Chemistry and
   Geology.
2. **What counts as a blank?** Only inline underscores in sentences? Or also the worked-example
   answer line and fill-in tables (`fillin_table`)? His chosen option already keeps an `Answer:` line
   for examples, so the open part is mainly the tables.

## 7. What this does not do

- It does not edit any file in `brand/`, `standards/`, `courses/`, `.claude/skills/`, or `templates/`.
- It does not resolve CONFLICT-20 (Physics notes-scaffolding index).
- It does not rebuild any packet or touch Drive.
- It does not add a `change-log/CHANGELOG.md` row (PENDING records are not indexed there, as with
  SHULL-CHG-0068).
