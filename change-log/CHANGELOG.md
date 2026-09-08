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

## 2026-09-08

| ID | Date | Change | Status | Record |
|---|---|---|---|---|
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
| 2026-09-08 | Two Geology section titles in U5 are near-duplicates | User — deferred to "when I get to work" |
| 2026-09-08 | The Drive Lab folder now holds a duplicate of two template files | User — deferred to "when I get to work" |
| 2026-09-07 | Chemistry grading framing differs between two legacy sources | User — see `courses/chemistry/DECISIONS.md` open questions |

---

## A known gap in this log's own coverage

`governance/CHANGE_CONTROL.md` §6 requires the Change ID in the commit message. **The thirteen
founding commits do not carry one** — the rule was written partway through them, and rewriting that
history to comply would be forging an audit log to make it look like it was always followed.

The rule binds from the commit that introduces this file forward. To trace a pre-rule change, use
the Record column: every one of the twelve is fully recorded, and the record names what it
supersedes. Nothing is lost; it is one hop slower.
