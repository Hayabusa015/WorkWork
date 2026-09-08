# SHULL OS

The operating system for Matthew Shull's teaching workflow — Chemistry, Physics, and Geology at
James A. Garfield Local Schools, Ohio.

**Status: Phase 7 of 14.** The skeleton and governance exist. Standards, agents, and skills do not
yet. Do not build classroom deliverables from this repository until Phase 14 passes — the installed
legacy SHULL skills are still the working system.

---

## 1. The one rule

> **A fact lives in exactly one place.**

Duplication is the defect. Not forgetting to update — duplication. Every conflict this system has
had came from the same fact being written twice and one copy going quietly stale.

If duplication is genuinely unavoidable, the duplicate **must** point at the authoritative source
rather than restating it.

## 2. Source of truth

| What | Authoritative home |
|---|---|
| Design rules, tokens, typography | `brand/` |
| Quality, voice, naming, Drive layout, QA | `standards/` |
| Course facts — curriculum, pacing, policy, assessment shape | `courses/<course>/DECISIONS.md` |
| Who is responsible | `.claude/agents/` |
| How a repeatable task is performed | `.claude/skills/` |
| Rules for changing rules | `governance/` |
| Finished teaching documents | **Google Drive** — `SHULL Science/` |
| Verified Drive folder IDs | `config/drive.json` |

**Google Drive is canonical for finished documents. This repository is canonical for the system
itself. Claude Projects are working context — never storage, never authority.**

### The line, stated as a test

> Changing it affects **all three courses** → it belongs in a standard or a skill.
> Changing it affects **one course** → it belongs in that course's `DECISIONS.md`.

A thinner summary-box border is a standard. Moving Plate Tectonics from U4 to U5 is a course
decision.

### Precedence when sources disagree

1. Matt's direct instruction in the current conversation
2. For course facts — the course `DECISIONS.md`
3. For build mechanics — the standard, then the skill
4. LOCKED over INHERITED over PROVISIONAL
5. Newer dated entry over older

When a skill states a course fact that the decisions file contradicts, **the decisions file wins and
the skill is reported stale.** It is not silently obeyed and it is not silently ignored.

When the layers genuinely overlap and it is not clear which is which: **stop and ask. One question.
Do not build on a guess.**

## 3. Before you build anything

Confirm the unit and section code exists in that course's `DECISIONS.md`. **Never build against a
`U#/S#.#` code that appears only in a skill file.** This is the check that would have caught the
Geology numbering problem before a packet printed with the wrong footer.

## 4. Safety and change control

- **Only the Secretary writes to `brand/`, `standards/`, `governance/`, and `courses/`, and only
  against an APPROVED proposal ID.** Everyone else proposes.
- Every rule change is a commit carrying its Change ID. Git history is the audit log.
- **Permanent deletion requires explicit user approval.** Drive objects can only be trashed
  (recoverable), never permanently deleted, by design.
- The weekly review is **report-only**. Autonomous self-modification is prohibited.
- Never present a PROVISIONAL, CONFLICT, or UNKNOWN item as settled.
- Never invent a unit title, section number, lab, date, policy, or assessment rule. Ask, or label it
  PROVISIONAL in the teacher notes — never on a student page.

## 5. Why this repository exists

Skills were previously installed through the Claude UI. **A reinstall overwrote user edits once.**
There was no version history, no diff between intended and installed, and no write path for any
agent to durably change a rule.

Git is the only durable write path in this system. That is the whole argument for the repository,
and it is why the Secretary can exist at all.

Claude cannot write to Claude Project Knowledge or to installed skills. Nothing propagates on its
own. If a document claims otherwise, it is wrong.

## 6. Working here

- `legacy/` is a **read-only** verbatim snapshot of the pre-migration system. Never edit it. It is
  excluded from every validator.
- `docs/` holds the migration analysis and the decision record. Read
  `docs/DECISIONS_2026-09-07.md` before acting on anything in `docs/CONFLICT_REPORT.md` — six of
  seven critical conflicts are resolved there.
- Report audits as tables, not prose.
- Show the plan, get a yes, then build. A "build me all of Unit 5" request is a plan first.
- A returned message is not a completed task. A task is complete when the deliverable has been
  verified to exist, at a verified location.
