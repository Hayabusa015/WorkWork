---
name: weekly-system-review
description: Run the recurring SHULL OS health and learning review - Researcher findings and Janitor maintenance - and turn them into PENDING proposals for user review. Report-only. Use on the weekly schedule, or when asked to run the sweep.
---

# weekly-system-review

> **This review is report-only. It changes nothing.**
> Autonomous self-modification is prohibited — spec Parts 31 and 47.

## Three hard limits

1. **Never edit `brand/`, `standards/`, `governance/`, or `courses/`.** Not once, not for something
   small.
2. **Every finding leaves as a PENDING proposal with a Change ID.** No finding is self-applied.
3. **If the review finds nothing, say so in one line and commit nothing.** A weekly report that
   manufactures work to look useful trains the reader to ignore it.

## Procedure

**1. Run the validators.**

```bash
python3 scripts/validate_layers.py
python3 scripts/validate_codes.py
python3 scripts/validate_tokens.py
python3 scripts/measure_tokens.py --check
python3 scripts/validate_agents.py
```

**2. Janitor sweep** — broken references, duplicate rules, conflicting rules, stale documentation,
orphaned files, deprecated standards still referenced, inconsistent naming, layer violations.

**Never flag `legacy/`.** Never flag materials listed in `brand/palette-archive/` as brand defects —
they are covered by the no-retrofit policy.

**3. Researcher pass** — content accuracy, currency, **recurring user corrections**. The same fix
twice is a pattern worth naming; that is the most valuable thing this review produces.

**4. Check the open questions** in each course's decisions file. Anything now answerable by evidence
gets surfaced — but the answer is proposed, never adopted.

**5. Write it up.** Findings to `reports/YYYY-WW/`. Proposals to `governance/proposals/`, status
PENDING.

## Report format

| # | File | Problem | Your action | Time |
|---|---|---|---|---|

Blocking first, then shortest fix first. Anything over ten minutes breaks into smaller rows.
No prose, no preamble.

## When a finding conflicts with a LOCKED rule

Write the proposal. **Mark the conflict explicitly. Do not resolve it.** The user decides.

## The thing to actually watch for

The legacy system's failure was never detection — its librarian caught the stale Physics map while
two other files were still wrong. The failure was **follow-through**. If a finding from last week is
still open this week, **raise it again and say it is a repeat.** Silence is not consent.
