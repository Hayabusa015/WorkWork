# SHULL-CHG-0052 — The repository, not the desk, allocates Change IDs

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0052 |
| **Date** | 2026-10-22 (first raised in the 2026-10-18 weekly sweep) |
| **Source** | Janitor (2026-10-18 weekly sweep). Re-checked against the repository on 2026-10-22. |
| **Current Rule** | See section 1. No rule says who allocates Change IDs; that gap is the finding. |
| **Proposed Rule** | See section 3. Prevention only. |
| **Supersedes** | Nothing. It fills a gap in `governance/CHANGE_CONTROL.md` section 2. |
| **Reason** | Claim VERIFIED in part. The Secretary's Desk held proposals numbered 0024-0029 and 0033-0038 from a 2026-09-27 sweep whose commits never reached git. The repository uses those numbers for different records (section 2). Twelve desk decisions on those IDs were therefore recorded against the wrong records and were not applied. Resolution already done (section 4). What remains is a rule to stop it recurring. |
| **Affected Agents** | Secretary, Janitor, Overseer (any session that runs `workflows/weekly-system-review.md`). |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low. It adds a rule about numbering drafts and changes no existing rule. (The desk summary rated this Medium because of the live collision, which is now cleared.) |
| **Recommendation** | Approve. |
| **Decision** | Pending. |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | No |

---

## 1. Current Rule — verbatim

`governance/CHANGE_CONTROL.md` line 20:

> Lives in `governance/proposals/`, one file per record, named `SHULL-CHG-NNNN-short-slug.md`.

It says where records live and how they are named. It does not say which place assigns NNNN.

## 2. What the repository holds now for the colliding IDs

The desk summary said 0035, 0036 and 0037 were PENDING and unrelated. That is out of date. Today:

| ID | Repository record | Status in the file |
|---|---|---|
| 0024 | `SHULL-CHG-0024-short-filenames.md` | IMPLEMENTED |
| 0025 | `SHULL-CHG-0025-humanize-skill.md` | IMPLEMENTED |
| 0026 | `SHULL-CHG-0026-gws-upload-inbox.md` | IMPLEMENTED |
| 0027 | `SHULL-CHG-0027-filing-gate.md` | IMPLEMENTED |
| 0028 | `SHULL-CHG-0028-reconcile-session-files.md` | IMPLEMENTED |
| 0029 | `SHULL-CHG-0029-unit-level-guided-notes-presentations.md` | IMPLEMENTED |
| 0033 | `SHULL-CHG-0033-notes-paged-redesign.md` | IMPLEMENTED |
| 0034 | `SHULL-CHG-0034-approval-recording.md` | APPROVED |
| 0035 | `SHULL-CHG-0035-drive-unit-folders.md` | APPROVED |
| 0036 | `SHULL-CHG-0036-chem-s1.4-fold.md` | IMPLEMENTED |
| 0037 | `SHULL-CHG-0037-multi-section-filenames.md` | REJECTED |
| 0038 | `SHULL-CHG-0038-notes-old-headers.md` | APPROVED |

## 3. Proposed Rule

Add to `governance/CHANGE_CONTROL.md` section 2, after the sentence on file naming:

> **The repository allocates Change IDs.** The next ID is one above the highest `SHULL-CHG-NNNN` file in
> `governance/proposals/` on the branch that will be merged. The Secretary's Desk, the Researcher, the
> Janitor and the Auditor never allocate one. A session that cannot push (no git access, or a branch that
> will not be merged) does not number its drafts: it reports them as unnumbered findings, and the Secretary
> numbers them when the record is committed. A record is not real until its file is committed under that ID.

Affects `workflows/weekly-system-review.md`: its sweep step should say the same in one line, pointing
at `CHANGE_CONTROL.md` section 2, not restating it.

## 4. Resolution already carried out (recorded, not proposed)

Per the main session on 2026-10-22: the stale desk rows for the colliding IDs were archived and the
desk was rebuilt from the repository. The 2026-09-27 decisions on those IDs were not applied to any
repository record and should not be. The findings behind the 2026-10-18 sweep were renumbered SHULL-CHG-0046
to 0051 in the repository. This record does not ask for further cleanup.

## 5. Not verified by the Secretary

The Secretary has no access to the desk's contents and has not inspected the archive. The statement in
section 4 is the main session's account.
