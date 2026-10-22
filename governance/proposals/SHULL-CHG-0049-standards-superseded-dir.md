# SHULL-CHG-0049 — standards/README.md references a directory that does not exist

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0049 |
| **Date** | 2026-10-22 (first raised in the 2026-10-18 weekly sweep) |
| **Source** | Janitor (2026-10-18 weekly sweep). Re-checked against the repository on 2026-10-22. The "REPEAT" tag was not verified here. |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | **CONFLICT: two options, no recommendation. The user chooses.** See section 2. |
| **Supersedes** | `standards/README.md` line 11, under either option (option A deletes it, option B makes it true). |
| **Reason** | Claim VERIFIED as still true. `standards/README.md` lists `superseded/` as a directory. No file or directory named `standards/superseded*` exists. The row describes a purpose, "Proposals considered and declined", that `governance/CHANGE_CONTROL.md` section 3 already assigns to REJECTED records in `governance/proposals/` ("Kept, not deleted — so it is not re-proposed"). |
| **Affected Agents** | Janitor, Secretary. |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low |
| **Recommendation** | None. This needs a user choice between two designs; the Secretary does not pick. |
| **Decision** | Pending. |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | No |

---

## 1. Current Rule — verbatim

`standards/README.md` line 11:

> | `superseded/` | Proposals considered and declined, kept so they are not re-proposed |

Evidence: a glob for `standards/superseded*` returns no files.

## 2. Options (CONFLICT — the user decides)

**Option A — remove the row.** Delete line 11 of `standards/README.md`. Declined proposals continue to
live as REJECTED records in `governance/proposals/`, which is already the rule in
`governance/CHANGE_CONTROL.md` section 3. Result: one home for declined proposals, no new directory.
Consistent with the one rule in `CLAUDE.md` section 1.

**Option B — create the directory.** Create `standards/superseded/` with a short README and move or
copy superseded standards there. This gives a second place where "considered and declined" material
lives, next to REJECTED records, and a decision would be needed about which one is authoritative.
Note also that the row's wording ("Proposals considered and declined") describes records, not
superseded standards, so the directory name and the description do not match; the row would need a
rewrite either way.

Neither option is applied until the user chooses one. If the user chooses neither, the record stays
PENDING and the Janitor will raise it again.
