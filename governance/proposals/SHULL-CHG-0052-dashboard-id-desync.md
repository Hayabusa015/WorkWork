# SHULL-CHG-0052 — Dashboard IDs 0024–0038 do not match repo records of the same ID

| Field | Value |
|---|---|
| **Date** | 2026-10-18 |
| **Source** | Janitor, weekly system review (self-diagnosed its own predecessor sweeps' defect) |
| **Resolves** | Two earlier sweeps (2026-09-27 and 2026-10-04) each allocated new Change IDs starting from `0024` and `0033` respectively, based on a checkout that did not include proposals other sessions had already pushed under those numbers. Neither sweep's own proposal files made it to `origin/main` (one had no git/shell access; the other's push failed with "repo not authorized for session"), but both wrote their findings into the Secretary's Desk dashboard's `proposals` collection regardless — so the dashboard showed 12 PENDING cards (IDs 0024-0029, 0033-0038) describing stale-documentation findings, while `governance/proposals/` on `main` used those exact same IDs for twelve unrelated, already-implemented changes (short filenames, the humanize skill, the GWS upload inbox, the filing gate, and others — see `change-log/CHANGELOG.md`). The user approved all twelve dashboard cards on 2026-10-03 and 2026-10-06, before this collision was discovered, so those decisions could never be correctly applied: there was no PENDING proposal at those IDs to move to APPROVED. |
| **Current Rule** | No rule governed how a session allocates a new Change ID beyond "never reused" (`governance/CHANGE_CONTROL.md` §2, implicit). Nothing required checking `origin/main` specifically, and nothing required a failed push to block further use of the ID it was meant to create. |
| **Proposed Rule** | `governance/CHANGE_CONTROL.md` gets an explicit "Allocating a new Change ID" rule: fetch `origin/main` first, allocate from what's actually pushed there, and treat a failed push as "not allocated yet," reported plainly rather than left as a buried `status_note`. |
| **Supersedes** | The twelve stale dashboard `proposals`/`decisions` documents at IDs 0024-0029 and 0033-0038 (2026-09-27 and 2026-10-04 vintage) — re-filed as SHULL-CHG-0046 through 0051. The real git records at those same ID numbers (0024, 0025, 0026, 0027, 0028, 0029, 0033, 0034, 0035, 0036, 0037, 0038) are untouched; they were never wrong, just collided with. |
| **Affected Agents** | `secretary`, `janitor` (ID allocation discipline) |
| **Affected Skills** | `weekly-system-review` |
| **Affected Courses** | None |
| **Risk** | Medium — a process defect, not a content defect, but one that could silently corrupt a real record if a future collision were resolved by overwriting instead of re-filing |
| **Recommendation** | Adopt |
| **Decision** | Approved via the Secretary's Desk dashboard (not a chat message) at 2026-10-22T13:41:09Z. Confirmed in chat 2026-10-22: "scretary desk approved." |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `governance/CHANGE_CONTROL.md` (new "Allocating a new Change ID" section), `workflows/weekly-system-review.md` (step 4 of the sync contract) |
| **Verified** | The twelve stale dashboard decisions (0024-0029, 0033-0038) were written back with `applied: true` and a note pointing here, rather than left pending forever or applied against the wrong files. The real `governance/proposals/SHULL-CHG-0024-*.md` through `SHULL-CHG-0038-*.md` files were read and confirmed unchanged by this record. |

## Why re-file instead of renumber

Renumbering the stale 2026-09-27/10-04 findings to slot them in earlier (say, as "0024b") would make
the collision invisible in the audit log — exactly the kind of silent correction
`governance/CHANGE_CONTROL.md` §1 ("Never edit history; append") exists to prevent. Re-filing them as
new, current records (0046-0051) with this record explaining why is slower but leaves the actual
sequence of events — including the mistake — readable from `change-log/CHANGELOG.md` alone.

## Addendum: a third collision, caught before it shipped (2026-10-22)

While merging this exact record into `main`, a *third* instance of the failure this record describes
turned up: this session and a parallel session (branch `claude/festive-noether-yhgdn7`) independently
drafted SHULL-CHG-0046 through 0052 — the same seven IDs, same seven topics, different file content —
because neither had visibility into the other. Unlike the 2026-09-27/10-04 collisions, this one was
caught at merge time rather than discovered later, precisely because both sides' work reached git
(the allocation rule this record added — fetch `origin/main` first — assumes a single session; it does
not yet cover two sessions allocating from the same base commit at the same time). The parallel
session's branch also independently implemented SHULL-CHG-0053 (a Secretary's Desk click, with your
direct confirmation, counts as a recorded decision) and resolved SHULL-CHG-0035/0036/0037 — all merged
into `main` alongside this record. **Open gap, not yet fixed:** the allocation rule needs a lease or
announcement step for the case of two sessions working the backlog at once, not just one session with
a stale checkout. Worth a follow-up record if this keeps happening.
