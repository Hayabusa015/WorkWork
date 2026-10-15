---
id: SHULL-CHG-0025
title: Add a humanize skill (blader/humanizer) that points at the anti-AI-slop standard
status: IMPLEMENTED
opened: 2026-10-15
source: User
decided: 2026-10-15
decided_by: Matthew Shull
---

# SHULL-CHG-0025 — Humanize skill

## What he asked for

"Add this skill to the repo to follow" — https://github.com/blader/humanizer (MIT, v3.1.0).

## Current Rule

`standards/ANTI_AI_SLOP_STANDARD.md` and `.claude/skills/anti-ai-slop/SKILL.md` hold the prose
checks. The humanizer pattern list overlaps them.

## Proposed Rule

Add `.claude/skills/humanize/SKILL.md`:

- Procedure and pattern list from upstream, credited, with its MIT notice.
- Prose only. Never touches filenames, code, data, or content on a student page that the
  decisions file defines.
- Adapted to SHULL: voice comes from `standards/VOICE.md`. The upstream dash ban applies to
  prose, not file names or folder names.
- Runs inside the `anti-ai-slop` pass (step: after Specificity and Padding), not instead of it.
- Patterns the standard already states are referenced, not restated. Only genuinely new patterns
  (upstream §1–§5, §8, §12, §22) are added to the standard in the same change.

## Supersedes

Nothing.

## Risk

low. Edits to the standard are additive.

## Recommendation

Approve.

Decision: Approved by Matthew Shull, 2026-10-15.
Status: IMPLEMENTED
Implemented By: 77fbb9d
Verified: Verified 2026-10-15: validators clean; skill listed in skills README and called from anti-ai-slop.
