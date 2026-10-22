# governance — the rules for changing rules

| File | Owns |
|---|---|
| `GOVERNANCE.md` | The two-layer rule, the precedence order, the authority matrix, agent limits |
| `CHANGE_CONTROL.md` | The change-record format and the two change paths |
| `proposals/` | Secretary change records: PENDING · APPROVED · REJECTED · DEFERRED · IMPLEMENTED |

Adapted from `SHULL_System_Governance.md`, which was already CONFIRMED and largely correct.
**Adopted, not rewritten.** The substantive change is that Layer 2 moves from Claude Project
Knowledge into `courses/*/DECISIONS.md`, because Project Knowledge has no version history and no
write path.

A to-do list inside a document is not a mechanism. The legacy governance file carried a
well-written fix list that nobody worked through, and the drift it described was still live days
later. That is why the validators in `scripts/` exist.

*Status: written (Phase 8). `proposals/` now holds dozens of change records spanning Phases 8–13 —
count them with `ls governance/proposals/ | wc -l` rather than trusting a number here.*
