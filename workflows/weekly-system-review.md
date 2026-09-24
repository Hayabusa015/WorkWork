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

**Scheduled 2026-09-24 (Phase 13 activated).** A Routine fires a fresh session weekly, Sunday
21:56 UTC, running this workflow end to end and stopping at PENDING proposals for user sign-off.
Push and email notification is on, so a sweep with findings reaches the user even outside a session.
Activated once the system had real exercise behind it — see the 2026-09-24 CLAUDE.md/README
stale-status correction, found and fixed by hand, as the case in point for why this needed to be
routine rather than incidental.

Cron is evaluated in UTC. Ohio is UTC−4 until 2026-11-01, UTC−5 after — **the schedule needs
revisiting at the DST change** (21:56 UTC will drift an hour relative to Ohio local time), and that
is a known gap rather than something the cron expression solves on its own. Whoever is running the
system after 2026-11-01 should re-check the fire time against local expectations.

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
