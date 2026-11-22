# SHULL-CHG-0087 — Twenty Python wheel files committed at the repository root

> **Deletion requires Matt's explicit approval** (CLAUDE.md §4). Nothing has been removed.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0087 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 25) |
| **Current Rule** | None. No rule covers committed binaries. CLAUDE.md §4: "Permanent deletion requires explicit user approval." |
| **Proposed Rule** | Remove the 20 `*.whl` files from the repository root (`git rm`, still recoverable from history) and add `*.whl` to `.gitignore`. |
| **Supersedes** | Nothing. |
| **Reason** | 20 wheels (about 38 MB; count confirmed by glob 2026-11-22) came in through WIP commit 1e8a084 (2026-10-04) and reached `main` in the consolidation. Nothing references them and they are not source. They include numpy, pandas, pydantic, sqlalchemy, mendeleev and Pint. |
| **Affected Agents** | Secretary or main session (removal once approved). |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low. Check first that no offline build step installs from them. |
| **Recommendation** | Remove after Matt confirms. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. Were these wheels put there on purpose, for example for an offline or sandboxed install? If so,
   should they move to a documented folder instead of being removed?
