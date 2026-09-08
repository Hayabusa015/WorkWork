# Workflow — Weekly system review

**Report-only. Changes nothing.** Autonomous self-modification is prohibited.

Procedure: `.claude/skills/weekly-system-review/SKILL.md`.

---

## The loop

```
repository · Drive · recent work
 ↓
RESEARCHER    content findings, recurring corrections, patterns
JANITOR       broken refs, duplicates, conflicts, stale docs, orphans
 ↓
SECRETARY     findings → numbered proposals, all PENDING
 ↓
USER          approves · rejects · defers
 ↓
SECRETARY     implements APPROVED only, cites the Change ID in the commit
 ↓
CHANGELOG     + git history
 ↓
verification  a change is not done until it has been checked
```

## Schedule

A Routine firing a fresh session. **Not yet scheduled** — Phase 13, and only after the system has
been exercised. A recurring job pointed at a half-built system produces noise, and noise trains the
reader to stop reading.

Cron is evaluated in UTC. Ohio is UTC−4 until 2026-11-01, UTC−5 after — **the schedule needs
revisiting at the DST change**, and that is a known gap rather than something the cron expression
solves on its own.

## What the review must not do

- Edit `brand/`, `standards/`, `governance/`, or `courses/`. Not once.
- Apply its own findings.
- Flag `legacy/`, or flag materials listed in `brand/palette-archive/` as brand defects.
- Manufacture findings to look useful. **Nothing found → one line, no commit.**

## The failure mode this exists to catch

The legacy system detected drift correctly. Its librarian flagged the stale Physics map while two
other files still said the map was missing — and nothing happened, because a fix list in a document
is not a mechanism.

**So: a finding still open next week gets raised again and marked a repeat.** Silence is not
consent, and a proposal that has sat PENDING for a month is itself a finding.
