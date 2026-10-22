# SHULL-CHG-0050 — Agents README lists a `model` frontmatter field no agent has

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0050 |
| **Date** | 2026-10-22 (first raised in the 2026-10-18 weekly sweep) |
| **Source** | Janitor (2026-10-18 weekly sweep). Re-checked against the repository on 2026-10-22. The "REPEAT" tag was not verified here. |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | **CONFLICT: two options, no recommendation. The user chooses.** See section 2. |
| **Supersedes** | `.claude/agents/README.md` lines 3-4, the list of frontmatter fields. |
| **Reason** | Claim VERIFIED as still true. The README says agent files carry `name`, `description`, `tools` and `model`. A search of `.claude/` finds no line beginning `model:` in any file. The seven agent files carry `name`, `description` and `tools` only (checked on `secretary.md`; the search covers all seven). `scripts/validate_agents.py` line 20 requires only `name`, `description`, `tools`, so the validator already treats `model` as absent. Which one is wrong, the README or the agents, is a design choice: giving agents a `model` pins which model runs each role. |
| **Affected Agents** | All seven, under option B only. |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low under option A; medium under option B (it changes which model each agent runs on). |
| **Recommendation** | None. The user chooses. |
| **Decision** | Pending. |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | No |

---

## 1. Current Rule — verbatim

`.claude/agents/README.md` lines 3-4:

> Seven agents, defined as `<name>.md` with YAML frontmatter (`name`, `description`, `tools`,
> `model`). Claude Code discovers subagents here, which is why they live under `.claude/` rather than

`scripts/validate_agents.py` line 20:

> REQUIRED = ("name", "description", "tools")

## 2. Options (CONFLICT — the user decides)

**Option A — fix the README.** Remove `model` from the list on line 4, so it matches the seven agent
files and the validator. Agents then inherit the session's model. Small, safe, edits one line.

**Option B — add `model` to the agents.** Add a `model:` line to each of the seven agent files and add
`model` to `REQUIRED` in `scripts/validate_agents.py`. The user must say which model each agent gets.
The Secretary does not choose models. This edits `.claude/agents/`, which is outside the four
directories the Secretary may write to, so the user should also say who applies it.

Neither option is applied until the user chooses.
