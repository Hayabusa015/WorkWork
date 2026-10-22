# SHULL OS — Change Log

**Purpose:** the human-readable index into the audit log. Git history *is* the audit log; this file
is how you find your way into it without running `git log` twelve times.

**This file is an index, not a source.** Every row points at the record that holds the reasoning. If
this file and a record disagree, **the record wins** and this file is the defect. Never restate a
rule here — a hex code, a unit number, or a filename grammar written in this file would be a second
place that fact lives, which is the one thing the whole system exists to prevent.

**Append at the top. Never edit a shipped row.** A change that was wrong gets a *new* row that
supersedes it, exactly as the decision logs work.

---

## How a row is written

| Column | Means |
|---|---|
| **ID** | `SHULL-CHG-NNNN`, allocated in `governance/CHANGE_CONTROL.md` order, never reused |
| **Date** | The date the user approved it, not the date it was implemented |
| **Change** | Four to eight words. The record has the sentence. |
| **Status** | `CONFIRMED` (approved and fully implemented) · `PARTIAL` (approved, implementation incomplete — the record says what is missing) · `PROPOSED` (awaiting the user) · `SUPERSEDED` (replaced; the superseding ID is named) |
| **Record** | The file holding the full record |

---

## 2026-10-22

Two sessions independently drafted SHULL-CHG-0046 through 0052 in parallel (see each record's
"Reconciliation note" and SHULL-CHG-0052's addendum). One session's drafts were implemented first and
are what the rows below describe; the other's PROPOSED drafts of the same seven findings were not
separately rows here, to avoid listing the same fact twice under two statuses.

| ID | Date | Change | Status | Record |
|---|---|---|---|---|
| SHULL-CHG-0053 | 2026-10-22 | A Secretary's Desk click is the user's recorded decision | CONFIRMED | `governance/proposals/SHULL-CHG-0053-desk-click-is-recorded-decision.md` |
| SHULL-CHG-0052 | 2026-10-22 | Dashboard IDs 0024-0038 collided with real git records of the same ID; re-filed at 0046-0051 | CONFIRMED | `governance/proposals/SHULL-CHG-0052-dashboard-id-desync.md` |
| SHULL-CHG-0051 | 2026-10-22 | SHULL-CHG-0010's own header Status contradicted its own resolution | CONFIRMED | `governance/proposals/SHULL-CHG-0051-chg-0010-header-status.md` |
| SHULL-CHG-0050 | 2026-10-22 | Agents README claimed a `model` frontmatter field no agent has (judgment call — see record) | CONFIRMED | `governance/proposals/SHULL-CHG-0050-agents-readme-model-field.md` |
| SHULL-CHG-0049 | 2026-10-22 | standards/README.md referenced a `superseded/` directory that was never built (judgment call — see record) | CONFIRMED | `governance/proposals/SHULL-CHG-0049-standards-superseded-dir.md` |
| SHULL-CHG-0048 | 2026-10-22 | scripts/README.md documented 12 of 32 scripts; now documents all of them | CONFIRMED | `governance/proposals/SHULL-CHG-0048-scripts-readme-undocumented.md` |
| SHULL-CHG-0047 | 2026-10-22 | Three READMEs still said "Status: not yet written" for files long since written | CONFIRMED | `governance/proposals/SHULL-CHG-0047-not-yet-written-readmes.md` |
| SHULL-CHG-0046 | 2026-10-22 | Phase 13 status stale in CLAUDE.md and the implementation plan (4th occurrence) | CONFIRMED | `governance/proposals/SHULL-CHG-0046-phase-13-status-stale.md` |

## 2026-10-16

| ID | Date | Change | Status | Record |
|---|---|---|---|---|
| SHULL-CHG-0045 | 2026-10-16 | Strike-through: well-known calculation slips count as common; QA_GATE notes the key-handwriting face | CONFIRMED | `governance/proposals/SHULL-CHG-0045-strike-through-common-slips-and-qa-gate-key-face.md` |
| SHULL-CHG-0044 | 2026-10-16 | ShullHand (Matt's own handwriting) becomes the key-handwriting face | CONFIRMED | `governance/proposals/SHULL-CHG-0044-shullhand-key-font.md` |
| SHULL-CHG-0043 | 2026-10-16 | Handwritten teacher answer keys: pencil and pen, stacked fractions, algebra steps, physics scenario sketch | CONFIRMED | `governance/proposals/SHULL-CHG-0043-handwritten-answer-keys.md` |
| SHULL-CHG-0042 | 2026-10-16 | Molecular structures on student pages are built with the molecule script | CONFIRMED | `governance/proposals/SHULL-CHG-0042-molecule-builder-rule.md` |

## 2026-10-15

| ID | Date | Change | Status | Record |
|---|---|---|---|---|
| SHULL-CHG-0035 | 2026-10-15 | Drive: system creates no folders; file loose if no match | PARTIAL | `governance/proposals/SHULL-CHG-0035-drive-unit-folders.md` |
| SHULL-CHG-0036 | 2026-10-15 | Chemistry 1.4 Isotopes folded into 1.3; code retired | CONFIRMED | `governance/proposals/SHULL-CHG-0036-chem-s1.4-fold.md` |
| SHULL-CHG-0024 | 2026-10-15 | Short section-led filenames; no course prefix | PARTIAL | `governance/proposals/SHULL-CHG-0024-short-filenames.md` |
| SHULL-CHG-0041 | 2026-10-15 | Short topics: 20-character short titles from the course decisions file | PARTIAL | `governance/proposals/SHULL-CHG-0041-short-topics.md` |
| SHULL-CHG-0028 | 2026-10-15 | reconcile-session-files skill: list session documents not on Drive, file after approval | CONFIRMED | `governance/proposals/SHULL-CHG-0028-reconcile-session-files.md` |
| SHULL-CHG-0027 | 2026-10-15 | Filing gate: file to Drive only after user approval | CONFIRMED | `governance/proposals/SHULL-CHG-0027-filing-gate.md` |
| SHULL-CHG-0026 | 2026-10-15 | gws uploads built files to an Upload Inbox; connector files them | CONFIRMED | `governance/proposals/SHULL-CHG-0026-gws-upload-inbox.md` |
| SHULL-CHG-0025 | 2026-10-15 | Humanize skill and structural prose tells | CONFIRMED | `governance/proposals/SHULL-CHG-0025-humanize-skill.md` |

## 2026-09-20

| ID | Date | Change | Status | Record |
|---|---|---|---|---|
| SHULL-CHG-0023 | 2026-09-20 | Guided notes are strictly recall; no questions | CONFIRMED | `governance/proposals/SHULL-CHG-0023-notes-are-recall.md` |

## 2026-09-23

`PENDING` in a record is `PROPOSED` here. The Date column stays empty until the user approves.

| ID | Date | Change | Status | Record |
|---|---|---|---|---|
| SHULL-CHG-0039 | 2026-09-28 | Self-check answer prints inside the work box | PARTIAL | `governance/proposals/SHULL-CHG-0039-selfcheck-in-work-box.md` |
| SHULL-CHG-0038 | 2026-09-23 | Old notes headers restored on the paged layout | PARTIAL | `governance/proposals/SHULL-CHG-0038-notes-old-headers.md` |
| SHULL-CHG-0034 | 2026-09-23 | Main session records the user's verbatim decision | PARTIAL | `governance/proposals/SHULL-CHG-0034-approval-recording.md` |
| SHULL-CHG-0033 | 2026-09-23 | Guided notes paged redesign from the Codex reference | CONFIRMED | `governance/proposals/SHULL-CHG-0033-notes-paged-redesign.md` |
| SHULL-CHG-0032 | 2026-09-23 | Retroactive: seven unrecorded notes-template commits | CONFIRMED | `governance/proposals/SHULL-CHG-0032-notes-template-retroactive.md` |

## 2026-09-16

| ID | Date | Change | Status | Record |
|---|---|---|---|---|
| SHULL-CHG-0030 | 2026-09-16 | Tests-Quizizz renamed Quiz, moves to Unit level; Homework folder removed, filed loose in Section | IMPLEMENTED | `governance/proposals/SHULL-CHG-0030-quiz-unit-level-no-homework-folder.md` |
| SHULL-CHG-0029 | 2026-09-16 | Guided Notes and Presentations move from Section to Unit level | IMPLEMENTED | `governance/proposals/SHULL-CHG-0029-unit-level-guided-notes-presentations.md` |

## 2026-09-09 · 2026-09-08

| ID | Date | Change | Status | Record |
|---|---|---|---|---|
| SHULL-CHG-0017 | 2026-09-09 | Course profiles: stacked fractions, equation bar, Geology has no math | CONFIRMED | `governance/proposals/SHULL-CHG-0017-course-profiles.md` |
| SHULL-CHG-0018 | 2026-09-09 | Cue column narrows to 1.28in and condenses; no box around the equation bar | CONFIRMED | `governance/proposals/SHULL-CHG-0018-cue-column.md` |
| SHULL-CHG-0019 | 2026-09-09 | Worksheet template with three enforced course profiles; font audit | CONFIRMED | `governance/proposals/SHULL-CHG-0019-worksheet-template.md` |
| SHULL-CHG-0020 | 2026-09-09 | Master_Physics card layout; toner replaces marked as the ink budget | CONFIRMED | `governance/proposals/SHULL-CHG-0020-master-physics-layout.md` |
| SHULL-CHG-0021 | 2026-09-09 | Calculations carry their answer, except the last question | CONFIRMED | `governance/proposals/SHULL-CHG-0021-self-check-answers.md` |
| SHULL-CHG-0022 | 2026-09-09 | A Geology assignment is not a cut-and-glue by default; sort and match blocks | CONFIRMED | `governance/proposals/SHULL-CHG-0022-geology-formats.md` |
| SHULL-CHG-0016 | 2026-09-09 | A problem to solve gets a bordered work box, enforced at build | CONFIRMED | `governance/proposals/SHULL-CHG-0016-work-boxes.md` |
| SHULL-CHG-0015 | 2026-09-09 | A numbered list is just the number — no box, any format | CONFIRMED | `governance/proposals/SHULL-CHG-0015-no-number-boxes.md` |
| SHULL-CHG-0014 | 2026-09-09 | Guided notes template, .docx, from Matthew's own packet | CONFIRMED | `governance/proposals/SHULL-CHG-0014-guided-notes-template.md` |
| SHULL-CHG-0013 | 2026-09-08 | Twelve-layout slide template migrated onto the token system | CONFIRMED | `governance/proposals/SHULL-CHG-0013-slide-template.md` |
| SHULL-CHG-0012 | 2026-09-08 | Physics decisions file created from two legacy sources | CONFIRMED | `courses/physics/DECISIONS.md` |
| SHULL-CHG-0011 | 2026-09-08 | Chemistry decisions adopted from Drive as authoritative | CONFIRMED | `courses/chemistry/DECISIONS.md` |
| SHULL-CHG-0010 | 2026-09-08 | Adopt the existing lab template rather than redesign | PARTIAL | `governance/proposals/SHULL-CHG-0010-lab-template.md` |
| SHULL-CHG-0009 | 2026-09-08 | Geology has section numbers — 10 units, 54 sections | CONFIRMED | `governance/proposals/SHULL-CHG-0009-geology-section-numbering.md` |
| SHULL-CHG-0008 | 2026-09-08 | Text-safe deep variants for colour on a light ground | CONFIRMED | `docs/DECISIONS_2026-09-07.md` |
| SHULL-CHG-0007 | 2026-09-08 | Zero-padded section codes | CONFIRMED | `docs/DECISIONS_2026-09-07.md` |

## 2026-09-07

| ID | Date | Change | Status | Record |
|---|---|---|---|---|
| SHULL-CHG-0006 | 2026-09-07 | Typography resolved and substitution made deterministic | CONFIRMED | `docs/DECISIONS_2026-09-07.md` |
| SHULL-CHG-0005 | 2026-09-07 | Drive architecture — the built structure stands | CONFIRMED | `docs/DECISIONS_2026-09-07.md` |
| SHULL-CHG-0004 | 2026-09-07 | Geology unit numbering — Plate Tectonics is U4 | CONFIRMED | `docs/DECISIONS_2026-09-07.md` |
| SHULL-CHG-0003 | 2026-09-07 | Geology palette locked | CONFIRMED | `docs/DECISIONS_2026-09-07.md` |
| SHULL-CHG-0002 | 2026-09-07 | Physics palette locked | CONFIRMED | `docs/DECISIONS_2026-09-07.md` |
| SHULL-CHG-0001 | 2026-09-07 | Repository identity resolved | CONFIRMED | `docs/DECISIONS_2026-09-07.md` |

---

## Open, not yet a change record

Tracked here so they are not lost between sessions. These are **not** decisions; they are questions
with the user.

| Raised | Question | Waiting on |
|---|---|---|
| 2026-09-23 | Approve the paged guided-notes redesign? Two conflicts with LOCKED rules come first: block-number chips vs SHULL-CHG-0015, and cue width vs SHULL-CHG-0018. The rebuild stays uncommitted until approval. | User — SHULL-CHG-0033. Answered 2026-09-23 — approved |
| 2026-09-23 | Acknowledge the retroactive record for seven notes-template commits made without a Change ID (2026-09-16 to 2026-09-23). History is not rewritten. | User — SHULL-CHG-0032. Answered 2026-09-23 — approved |
| 2026-09-20 | SHULL-CHG-0023 made the notes packet strictly recall but scoped three blocks out of it: the closed-notes section summary box, the per-section self-check, and the "still fuzzy on" prompt. They read as the student checking their own notes rather than being quizzed on a slide. Should any of them also lose their question form? | User — SHULL-CHG-0023 §"Deliberately out of scope" |
| 2026-09-08 | File the U01 S1.4 deck into the live teaching Drive? 3 operations logged, not executed | User — `reports/drive-operations/2026-09-08_chem-u01-s01.4-slides.md` |
| 2026-09-09 | Nebular theory is filed `GEO_U1_S1.3` in his own sheet; the roadmap says 1.3 is *The Scale of the Universe* and 1.4 is *Formation of a Solar System*. Same drift puts *The Sun* at 1.4 in the notes spec where the roadmap says 1.5. Which numbering is right? **Partial action 2026-09-16:** the physical `GEO_U1_S1.2`/`S1.3` files were relocated to match their own filename/content code (`reports/drive-operations/2026-09-16f_geo-u1-file-relocation.md`) — this only makes the *file location* consistent with the *filename*; it does not answer whether the roadmap's section titles or the filenames are the ones that are wrong. | User — SHULL-CHG-0019 |
| 2026-09-09 | The practice-set ramp: his shipped Physics packet runs 2/2/1/1 (six questions); the INHERITED studio spec said 2/3/2/1 (eight). Physics now follows the artifact. Should Chemistry adopt 2/2/1/1 too, or keep its own counts? | User — SHULL-CHG-0019 |
| 2026-09-09 | `validate_codes.py` checks that a section code exists, not that its title matches the roadmap. That is how the 1.3/1.4 drift survived. Worth building a title check? | User |
| 2026-09-09 | Tier tags reuse `semantic.danger` (red) for CHALLENGE. Red also means hazard in a lab. Keep it, or run the ramp grey → course accent → ink? | User — SHULL-CHG-0020 |
| 2026-09-08 | Empty image wells render as dashed boxes; a deck cannot suppress a well it is not using | Design — T-7 open finding |
| 2026-09-09 | Notes specs cannot express a table inside a Cornell cell — his Physics equation table flattened to text | Design — SHULL-CHG-0016, matters most for Physics |
| 2026-09-08 | Two Geology section titles in U5 are near-duplicates | User — deferred to "when I get to work" |
| 2026-09-08 | The Drive Lab folder now holds a duplicate of two template files | User — deferred to "when I get to work" |
| 2026-09-07 | Chemistry grading framing differs between two legacy sources | User — see `courses/chemistry/DECISIONS.md` open questions |
| 2026-09-16 | ~~The Librarian's live Geology/Physics folder scaffold logged intent to build the old five-per-section structure the same day SHULL-CHG-0029 replaced it. Does live Drive need remediation?~~ **RESOLVED 2026-09-16.** Yes, it needed remediation, and it's done: Geology, Physics, and Chemistry were all retrofitted through SHULL-CHG-0029 and then SHULL-CHG-0030, and the 220 resulting leftover folders were trashed after Matt's approval. Full trail: `reports/drive-operations/2026-09-16b` through `2026-09-16f`. | Resolved — no longer waiting on anyone |
| 2026-09-16 | Physics Section 01.1 has 4 homework files named for `S01.2` despite being physically filed in `01.1` — the same class of drift as the Nebular Theory row above, found during the SHULL-CHG-0030 retrofit. Unlike the Geology pair, these were **not** relocated (not explicitly asked). Does `01.1` or the filenames have it right, and should they move? | User — `reports/drive-operations/2026-09-16c_physics-u01-chemistry-shull-chg-0024.md` |
| 2026-09-16 | Naming/zero-padding drift found during the same retrofit, not corrected (out of scope for a folder-structure task): Chemistry Unit 00's two lab PDFs use `S0.4` instead of the standard zero-padded `S00.4`; Chemistry Unit 01's stray `Unit PPT` deck (`Unit 1 - Matter and Atomic Theory Notes.pptx`) carries no `SHULL_` filename code at all. Worth a Naming-skill/Auditor pass whenever convenient. | User/Auditor — `reports/drive-operations/2026-09-16c_physics-u01-chemistry-shull-chg-0024.md` |
| 2026-09-16 | Chemistry Unit 00 still has a bare `Labs` folder instead of a proper Section folder (known defect, `config/drive.json` → `knownDefects`) — which section it belongs to has never been established, so nothing has renamed or refiled it. | User |

---

## A known gap in this log's own coverage

`governance/CHANGE_CONTROL.md` §6 requires the Change ID in the commit message. **The thirteen
founding commits do not carry one** — the rule was written partway through them, and rewriting that
history to comply would be forging an audit log to make it look like it was always followed.

The rule binds from the commit that introduces this file forward. To trace a pre-rule change, use
the Record column: every one of the twelve is fully recorded, and the record names what it
supersedes. Nothing is lost; it is one hop slower.

The same gap opened again after the rule: seven notes-template commits (2026-09-16 to 2026-09-23)
carry no Change ID. They are recorded retroactively in SHULL-CHG-0024, and their history is not
rewritten either.
