# Change Control

**Any permanent change** to brand, palette, typography, design standards, agent responsibilities,
skill behaviour, governance, or a course-wide convention **must be recorded.**

---

## 1. The two paths

**Path A — a course change.** Most changes. Edit that course's `DECISIONS.md`, append a dated entry
to the top of its decision log, commit. No standard or skill is touched.

**Path B — a build or brand change.** Rare. A change record is written, approved, and only then
applied by the Secretary.

If a change touches both layers, it is split into two edits and each is labelled.

## 2. The change record

Lives in `governance/proposals/`, one file per record, named `SHULL-CHG-NNNN-short-slug.md`.

```
Change ID:        SHULL-CHG-0009
Date:
Source:           Researcher | Janitor | Auditor | User | Migration
Current Rule:     [verbatim, with file and section]
Proposed Rule:    [verbatim]
Supersedes:       [file §]
Reason:
Affected Agents:
Affected Skills:
Affected Courses:
Risk:             low | medium | high
Recommendation:
Decision:
Status:           PENDING | APPROVED | REJECTED | DEFERRED | IMPLEMENTED
Implemented By:   [commit SHA]
Verified:         [yes/no — and how]
```

### Three fields that are not decoration

- **`Supersedes:`** — carried over from the legacy model, where it was described as "what makes
  drift visible instead of silent." A change that replaces a rule must name the rule it replaces.
- **`Implemented By:`** — ties the record to the actual diff. Without it, a record is a claim.
- **`Verified:`** — **a change is not done until it has been checked.** APPROVED is not IMPLEMENTED,
  and IMPLEMENTED is not verified.

## 3. Status

| Status | Meaning |
|---|---|
| **PENDING** | Written, awaiting the user |
| **APPROVED** | The user said yes. The Secretary may now act. |
| **REJECTED** | Declined. **Kept, not deleted** — so it is not re-proposed. |
| **DEFERRED** | Not now. Carries a reason. |
| **IMPLEMENTED** | Applied, with a commit SHA and a verification note |

## 4. Who may do what

- **Researcher, Janitor, Auditor** produce findings. They never write a proposal directly into an
  authoritative file.
- **The Secretary** turns findings into records, and is the **only** agent that may edit `brand/`,
  `standards/`, `governance/`, or `courses/` — and only against an APPROVED record.
- **The user** approves. Nothing else does.

> **Autonomous self-modification is prohibited.** The weekly review is report-only, permanently,
> until the user says otherwise.

## 5. The decision-log entry

Alongside the record, a one-paragraph entry goes at the **top** of the affected course's decision
log. **Never edit history; append.**

```markdown
### 2026-09-07 — Geology unit numbering
Plate Tectonics is U4. Glacial U8, Oceans & Climate U9, Earth's Resources U10.
Supersedes: SHULL_System_Governance.md §8 working record (U5/U9/U10).
Status: CONFIRMED · SHULL-CHG-0004
```

## 6. The commit

One change, one commit, and the Change ID in the message. Git history is the audit log;
`change-log/CHANGELOG.md` is the human-readable index into it.

## 7. Rollback

Every rule change is one revertible commit. Drive mutations are logged to
`reports/drive-operations/` **before** they happen — object ID, prior name, prior parent — because a
mutation that was not logged cannot be rolled back.

A Drive move done by copy-and-trash changes the file ID, so its rollback is imperfect. That is why
`standards/DRIVE_ARCHITECTURE.md` blocks moves until test T-3 passes.
