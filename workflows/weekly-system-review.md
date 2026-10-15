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

## Sign-off dashboard

**Secretary's Desk** — https://claude.ai/artifact/3zkvkaJB4EM8vYg2Jei5JT — is a Claude Artifact that
mirrors `governance/proposals/*.md` for the user to review and sign off from a browser instead of
reading raw markdown. Git remains authoritative; the dashboard is a synced view plus a decision
inbox, never a second copy of the truth:

- **`proposals` collection** — one document per Change ID, re-synced from the `.md` files whenever
  a session runs this workflow. Read-only from the page's side.
- **`decisions` collection** — written by the user clicking Approve / Reject / Defer on a PENDING
  item. This is new state, not a duplicate: it is the intake for a human decision that doesn't exist
  anywhere until they make it. Each document is `{change_id, decision, note, decided_at, applied}`.

**Approve in the dashboard is a decision, not an implementation.** It does not touch git. Every run
of this workflow must, after updating `governance/proposals/`:

1. Push the current state of every proposal into the `proposals` collection (`ArtifactData`
   `action: "batch"`, `set` per changed/new document) so the dashboard reflects reality.
2. Query the `decisions` collection for `applied: false` documents. For each one, treat the
   `decision` as the user's answer for that Change ID exactly as if they had said it in chat —
   `approved` moves the record to APPROVED (implement only if also asked to, per the Secretary's
   normal two-job split), `rejected`/`deferred` update `Status` and the decision log accordingly —
   then write the same document back with `applied: true` and `applied_at` set, and re-sync that
   proposal's `proposals` document so the dashboard shows the outcome without another manual step.
3. Never silently drop an `applied: false` decision. If a decision arrived for a Change ID that no
   longer exists or was already resolved another way, say so in the report rather than skipping it.

## The failure mode this exists to catch

The legacy system detected drift correctly. Its librarian flagged the stale Physics map while two
other files still said the map was missing — and nothing happened, because a fix list in a document
is not a mechanism.

**So: a finding still open next week gets raised again and marked a repeat.** Silence is not
consent, and a proposal that has sat PENDING for a month is itself a finding.
