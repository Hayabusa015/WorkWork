# SHULL-CHG-0050 — Agents README claims a `model` frontmatter field no agent has

| Field | Value |
|---|---|
| **Date** | 2026-10-18 |
| **Source** | Janitor, weekly system review |
| **Resolves** | `.claude/agents/README.md` described each agent's frontmatter as `name`, `description`, `tools`, `model` — but none of the seven agent files set a `model:` field. |
| **Current Rule** | The README claimed a field that does not exist in any of the seven definitions. |
| **Proposed Rule** | The README lists only the fields the agents actually carry (`name`, `description`, `tools`), and notes that none pin a model — they inherit whatever model runs the session. |
| **Supersedes** | `.claude/agents/README.md:3-4` |
| **Affected Agents** | None — documentation only; no agent definition changes |
| **Affected Skills** | None |
| **Affected Courses** | None |
| **Risk** | Low |
| **Recommendation** | Adopt |
| **Decision** | Approved via the Secretary's Desk dashboard (not a chat message) at 2026-10-22T13:40:58Z. Confirmed in chat 2026-10-22: "scretary desk approved." |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `.claude/agents/README.md` |
| **Verified** | `grep -l "^model:" .claude/agents/*.md` returns nothing, matching the corrected README text. |
