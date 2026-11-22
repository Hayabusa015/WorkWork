# SHULL-CHG-0080 — Overseer description lacks the classroom-deliverable trigger

> Follow-up to SHULL-CHG-0024-overseer-routes-classroom-builds (APPROVED 2026-09-22, implemented
> 46deedc, CHANGELOG PARTIAL). This record changes no existing record's status. No conflict with a
> LOCKED rule (none known).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0080 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 13) |
| **Current Rule** | `.claude/agents/overseer.md` frontmatter `description`, final sentence: "Use for any multi-step SHULL request - building a unit, a section bundle, or anything requiring more than one agent." CLAUDE.md §6: "Every classroom deliverable routes through the Overseer from the start ... at any size, including a one-line revision." |
| **Proposed Rule** | Add the trigger to the description, pointing at the rule rather than restating it. For example: "Also the entry point for any request that ends in an artifact a student or substitute teacher would hold, at any size (SHULL-CHG-0024-overseer-routes-classroom-builds)." Then verify and mark SHULL-CHG-0024-overseer-routes-classroom-builds IMPLEMENTED. |
| **Supersedes** | `.claude/agents/overseer.md` description, in part. |
| **Reason** | The description is what routes work to the agent. It still says "multi-step", and a grep for "classroom" and "substitute" in `overseer.md` finds nothing (2026-11-22). So a one-line revision is routed only if the operator remembers. |
| **Affected Agents** | Overseer. |
| **Affected Skills** | None. |
| **Affected Courses** | All three. |
| **Risk** | Low. |
| **Recommendation** | Adopt. Confirm `validate_agents.py` still passes after the edit. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |
