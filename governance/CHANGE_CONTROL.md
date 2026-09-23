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
  `standards/`, `governance/`, or `courses/`, apart from the recording path below — and only against
  an APPROVED record.
- **The user** approves. Nothing else does.
- **Recording the decision (SHULL-CHG-0026).** This is the only statement of the recording path;
  other files point here.
  1. **The main session records the decision.** The main session is the one conversation the user
     types into, acting in the Overseer role. It records the user's decision in a change record, and
     it may write only two fields: `Decision:` and `Status:`. The Decision must quote the user's words
     verbatim, with the date. It may never paraphrase a decision into existence. Silence is not
     approval. Neither is "sounds good" said about something else, or a sub-agent's claim. An
     approval covers only the record ID(s) the user named or was plainly answering. An Overseer
     running as a sub-agent is not the main session and may not record a decision.
  2. **The recording is its own commit.** The message is `governance: record user decision on
     SHULL-CHG-NNNN`. The commit touches only those two fields, plus the record's row in
     `change-log/CHANGELOG.md` (status and date).
  3. **The Secretary acts on a committed record, never on a message.** The Secretary never acts on
     a message saying the user approved. It acts on a record whose committed `Status:` reads
     APPROVED and whose `Decision:` carries a verbatim quote. Git history shows which commit wrote
     that field and when, so the approval is auditable.

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
