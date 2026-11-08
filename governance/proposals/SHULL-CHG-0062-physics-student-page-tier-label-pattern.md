# SHULL-CHG-0062 — Physics student pages: a corrected pattern on question count and tier labels

> **REPEAT x3.** The same correction has come from Matt three times. No conflict with a LOCKED rule
> found this run. The Secretary has not re-checked whether the 2/2/1/1 ramp is LOCKED; the Researcher
> should confirm its status before any decision is applied.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0062 |
| **Date** | 2026-11-08 |
| **Source** | Researcher finding, weekly sweep 2026-11-08 |
| **Current Rule** | Enforced Physics worksheet ramp of 2/2/1/1 questions per tier; tier tag on the student page (grey since SHULL-CHG-0055). See `courses/physics/DECISIONS.md`. |
| **Proposed Rule** | See Decision. Not adopted. |
| **Supersedes** | If adopted: the 2/2/1/1 ramp and the tier tag on Physics student pages, in part. Nothing replaced until Matt answers. |
| **Reason** | Evidence of the same correction three times, from `courses/physics/DECISIONS.md` lines 302-400 and 490-521, SHULL-CHG-0055 and SHULL-CHG-0019. |
| **Affected Agents** | Designer. |
| **Affected Skills** | Worksheet build skill and `templates/worksheet/build_worksheet_docx.py` (not checked this run). |
| **Affected Courses** | Physics. |
| **Risk** | Low to medium. Changes how every Physics worksheet is built. |
| **Recommendation** | Ask Matt; decide once rather than a fourth monkeypatch. |
| **Decision** | Approved by the user via the Secretary's Desk, 2026-11-08T22:43:22.709Z. Still open — Question for Matt, not answered by the click: make "no tier label on the student page" and a larger default ramp (about 9-10 questions) the standing Physics rule, and retire the monkeypatch? |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

Drive verification is not needed; this is a repo-only finding.

---

## 1. The three corrections

| # | Correction | Result so far |
|---|---|---|
| a | Larger sets than the enforced 2/2/1/1 ramp: S1.1 at 4/3/1/1, S1.2 at 3/3/3/1 | Each done by a one-off "not a precedent" monkeypatch |
| b | Tier tag suppressed on S1.2 ("do not add the little buttons") | One-off |
| c | 2026-10-28: "I almost don't even like the difficulty label" | SHULL-CHG-0055 only recoloured the tag grey |

## 2. What this does not do

- It does not change the ramp or the tag. It asks.
- It does not touch any filed worksheet.
