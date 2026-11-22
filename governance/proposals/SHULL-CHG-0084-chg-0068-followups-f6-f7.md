# SHULL-CHG-0084 — SHULL-CHG-0068 follow-ups F6 and F7 not done

> The follow-ups were recorded on `SHULL-CHG-0068-physics-u3-six-sections.md` (section on follow-ups,
> F6 and F7) but never raised as a finding. No conflict with a LOCKED rule (none known).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0084 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 22) |
| **Current Rule** | `courses/README.md` line 18: "\| Physics \| Mapped — 11 units, 48 sections. Source PDF is missing from Drive (Q-14). \|". `templates/notes/specs/make_phys_u03_s03.1-s03.6_notes.py` line 12: "2026-11-10 (SHULL-CHG-0068 pending for DECISIONS.md)." |
| **Proposed Rule** | `courses/README.md` points at `courses/physics/DECISIONS.md` for unit and section counts instead of stating them. The docstring drops "pending" on the next edit of that file. |
| **Supersedes** | `courses/README.md` line 18, in part. |
| **Reason** | Physics now has 47 sections (`courses/physics/DECISIONS.md` decision log). The README restates a fact owned by the decisions file (CLAUDE.md §1), and the copy has gone stale, as F7 predicted. The docstring is stale because SHULL-CHG-0068 is approved and applied. |
| **Affected Agents** | Secretary (`courses/README.md` is under `courses/`). Builder (docstring, on next edit). |
| **Affected Skills** | None. |
| **Affected Courses** | Physics. |
| **Risk** | Low. |
| **Recommendation** | Adopt as F7 itself recommended: point, do not restate 47. Should the Chemistry row ("16 units, 90 sections") follow the same pattern? That is open question 1. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. Apply the same pointer treatment to the Chemistry row on line 17, which also restates counts
   owned by its decisions file? Not checked for staleness this run.
