# Agents — who is responsible

Seven agents, defined as `<name>.md` with YAML frontmatter (`name`, `description`, `tools`,
`model`). Claude Code discovers subagents here, which is why they live under `.claude/` rather than
a top-level `agents/`.

| Agent | Owns |
|---|---|
| `overseer` | Interprets the request, plans, delegates, verifies, writes the task report |
| `researcher` | Content accuracy, patterns, recurring corrections. Reports only. |
| `designer` | Applies the design system to a deliverable |
| `librarian` | Drive: retrieve, create, name, file, verify |
| `janitor` | System health: broken references, duplicates, stale docs, orphans. Reports only. |
| `secretary` | Turns findings into proposals; the **only** agent that may edit authoritative files |
| `auditor` | Independent QA. Reports; never fixes what it finds. |

**Do not add an eighth agent without a demonstrated need.**

Authority is enforced three ways: the `tools:` grant in each agent's frontmatter, a PreToolUse hook
in `.claude/settings.json`, and the validators in `scripts/`. See `governance/GOVERNANCE.md`.

*Status: all seven written and validated against the authority matrix (Phase 8).*
