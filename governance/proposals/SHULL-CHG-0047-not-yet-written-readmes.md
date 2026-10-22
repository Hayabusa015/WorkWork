# SHULL-CHG-0047 — Three READMEs still say "Status: not yet written"

| Field | Value |
|---|---|
| **Date** | 2026-10-18 |
| **Source** | Janitor, weekly system review |
| **Resolves** | `governance/README.md`, `schemas/README.md`, and `scripts/README.md` each carried a "not yet written" status line long after the files they describe existed and validated clean — in `scripts/README.md`'s case, with real documentation content written *after* the false status line in the same file. |
| **Current Rule** | Each file's closing line claimed its own subject matter was unwritten. |
| **Proposed Rule** | Each status line reflects what is actually on disk, or is removed where the fact is better stated once elsewhere (see SHULL-CHG-0049 for the standards/README case this overlaps). |
| **Supersedes** | `governance/README.md`'s closing line; `schemas/README.md`'s closing line; `scripts/README.md:31` |
| **Affected Agents** | None — documentation only |
| **Affected Skills** | None |
| **Affected Courses** | None |
| **Risk** | Low |
| **Recommendation** | Adopt |
| **Decision** | Approved via the Secretary's Desk dashboard (not a chat message) at 2026-10-22T13:41:07Z. Confirmed in chat 2026-10-22: "scretary desk approved." |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `governance/README.md`, `schemas/README.md`, `scripts/README.md` |
| **Verified** | All three status lines now state what is actually built, with `governance/README.md` deliberately avoiding a hardcoded proposal count (the exact stale-fact pattern this record exists to stop) and pointing at `ls governance/proposals/ | wc -l` instead. |
