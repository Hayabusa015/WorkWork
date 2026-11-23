# SHULL-CHG-0078 — Change IDs still collide after the allocation rule

Repeat of: SHULL-CHG-0052

> **Options record. Renumbering is Matt's decision** (`docs/PLAN_2026-11-13_consolidate-and-ship.md`
> §4b step 4: "renumber only if Matt approves"). A desk click cannot choose an option
> (CHANGE_CONTROL §4); it needs Matt's answer in chat naming the option.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0078 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 8) |
| **Current Rule** | `governance/CHANGE_CONTROL.md` §2 "Allocating a new Change ID" (added f5e3502, 2026-10-22): "Before writing a new record, `git fetch origin main` and take the next integer after the highest `SHULL-CHG-NNNN` that exists in `governance/proposals/` **on that freshly-fetched `origin/main`**". |
| **Proposed Rule** | Matt picks one of the options below. Under every option, until it is done: new references cite the record file path, not the bare ID. |
| **Supersedes** | Nothing until an option is chosen. Option 2 or 3 would supersede the record IDs it renames. |
| **Reason** | Five collisions were allocated after the rule existed: 0054 ×3 (10-23, 10-26, 10-28), 0066 ×2 (11-09, 11-09), 0068 ×3 (11-09, 11-10, 11-10), 0069 ×2 (11-10, 11-11), 0070 ×2 (11-10, 11-11). The 0046 pair straddles the rule (10-21, 10-22) and is acknowledged in CHANGELOG. 0023 ×4 and 0024 ×5 predate the rule. The 2026-11-10 renumber 0058/0059 → 0068/0069 (d0c5392) collided again with records on other branches. CHANGELOG separates records by path; bare-ID commit subjects do not (f716dcf and 7204bf4 are both "SHULL-CHG-0070"). Three colliders are Path A course records, but they carry Change IDs, so the rule applies to them. |
| **Affected Agents** | Secretary, main session, Janitor and Researcher (all allocate or cite IDs). |
| **Affected Skills** | weekly-system-review. |
| **Affected Courses** | None directly. |
| **Risk** | Medium. Approvals and commits can be attributed to the wrong record. |
| **Recommendation** | None made. The options differ in how much history they rewrite in references, and that trade-off is Matt's. |
| **Decision** | Option 1, chosen by the user in chat, 2026-11-23: "option 1 plus the validator", answering the main session's question naming options 1–3 and the duplicate-ID validator (open question 2 and the Researcher's proposed validator). |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

This sweep's main session fetched `origin/main` before allocating 0074–0089 (highest found:
SHULL-CHG-0073), as §2 requires. Per §2, these IDs are not real until they are pushed to `origin/main`.

## Options

| Option | What happens | Cost |
|---|---|---|
| 1. Leave as is | Keep duplicates. The file path is the identifier wherever the ID is ambiguous. Fix SHULL-CHG-0077 so the desk can show both. | No renames. Bare-ID commit subjects stay ambiguous forever. |
| 2. Renumber post-rule colliders only | For each of 0054, 0066, 0068, 0069, 0070, the earliest record keeps the number. Later ones get fresh IDs from `origin/main`, with a pointer line in the old position. | Rewrites references to about 7 records. Commit subjects cannot be changed. |
| 3. Renumber every collision | As option 2, also for 0023, 0024, 0046. | Most churn; touches long-settled records. |

## Open question

1. Which option? If 2 or 3: confirm the tie-break (earliest dated record keeps the number).
2. The allocation rule did not prevent these. Should §2 also require a check for an existing file with
   the same ID immediately before push? That would be a separate governance change.

## Researcher corroboration (2026-W47)

The Researcher reported the same recurrence independently (`reports/2026-W47/researcher.md` row 7). It
adds:

- **Inferred cause: branch merges.** Parallel feature branches each allocated correctly from a fresh
  `origin/main`, then all landed together in the 26-branch consolidation merge (`ccr-bdef5882`). The
  §2 rule assumes a record reaches `main` before the next session allocates. Branch work defeats that
  assumption.
- **Proposed duplicate-ID validator.** No script in `scripts/` checks proposal filenames for
  duplicates. A validator would fail when two `governance/proposals/SHULL-CHG-NNNN-*` files share
  NNNN, making this a mechanism rather than documentation. It would need its own approval, and it
  would fail on the existing duplicates until an option above is chosen (or the existing set is
  allow-listed).
- **Amend the allocation rule for parallel branch work.** Two candidate approaches: reserve the ID by
  pushing a stub record to `main` first, or renumber at merge time. That is a governance change and is
  not adopted here.
- For renumbering, the Researcher recommends option 2 or 3 above, following the SHULL-CHG-0052
  precedent (supersede, don't rewrite). The choice stays with Matt.
