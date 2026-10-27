# SHULL-CHG-0054 — An Overseer running as a sub-agent returns a routing brief and does not delegate

> **ID allocation note.** The main session fetched `origin/main` on 2026-10-27 and confirmed
> 0054 was free before committing this record.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0054 (unconfirmed; see the note above) |
| **Date** | 2026-10-27 |
| **Source** | User. Matt asked the main session to propose this on 2026-10-27, after the Geology S2.3 Dinosaur Poster build. The finding came from the main session. |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | See section 2. |
| **Supersedes** | `.claude/agents/overseer.md`, "Delegation" section (lines 42-51), in part. The table stays, but it no longer implies the Overseer always dispatches the agents itself. Also the frontmatter `description` (line 3) clause "delegates to the specialist agents, monitors progress". Nothing LOCKED is replaced. |
| **Reason** | In Claude Code, a sub-agent cannot start other sub-agents. When the Overseer is launched through the Agent tool, the harness does not give it the `Agent` tool, even though `overseer.md` line 4 lists it. In the 2026-10-27 run it also had no Bash and no Drive tools. It wrote a plan, was told to build, and came back INCOMPLETE with nothing routed. The main session then had to dispatch researcher, designer and auditor itself, with no brief to work from. The agent file says the Overseer delegates in every case, so the failure was predictable but nothing in the file says what to do about it. |
| **Affected Agents** | Overseer (the edit). The main session, which dispatches each step when the Overseer is a sub-agent. Researcher, designer, auditor and librarian are unchanged: they get the same work, dispatched by the main session instead. |
| **Affected Skills** | None found. Checked by Grep for "overseer" across `.claude/skills/`: `verify-content` and `audit-deliverable` say findings route through the Overseer, which a routing brief still does. |
| **Affected Courses** | None. This is about how the system runs, not about course content. |
| **Risk** | Low. It adds a fallback for a case that already fails. When the Overseer has the `Agent` tool (main-session role), nothing changes. The QA gate, the filing gate and the verification list are untouched. |
| **Recommendation** | Approve. Optional follow-up, not part of this record: decide whether `Agent` should stay in the `tools:` line of `overseer.md`. It only works when the Overseer is not a sub-agent, and listing it suggests a capability the sub-agent case does not have. If Matt wants that changed, it gets its own record. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

---

## 1. Current Rule — verbatim

`.claude/agents/overseer.md` line 3 (frontmatter `description`):

> Project manager and primary orchestrator for SHULL OS. Interprets the request, determines subject
> and scope, plans, delegates to the specialist agents, monitors progress, [...]

`.claude/agents/overseer.md` line 4:

> tools: Read, Glob, Grep, Skill, Agent, Write, TaskCreate, TaskUpdate, TaskList

`.claude/agents/overseer.md` lines 39-51:

> **One section at a time. Each document QA'd before the next starts.** Say which agent you are routing
> to and why.
>
> ## Delegation
>
> | Need | Agent |
> |---|---|
> | Content accuracy, examples, currency | `researcher` |
> | Build the deliverable to the design system | `designer` |
> | Independent QA | `auditor` |
> | Retrieve, name, file, verify on Drive | `librarian` |
> | System health, broken references, duplicates | `janitor` |
> | Turn a finding into a reviewable proposal | `secretary` |

No line in the file covers the case where the Overseer has no `Agent` tool.

## 2. Proposed Rule

Add this subsection to `.claude/agents/overseer.md`, directly after the Delegation table:

> ### When you are running as a sub-agent (SHULL-CHG-0054)
>
> A sub-agent cannot start sub-agents. If the `Agent` tool is not available to you, you cannot
> delegate. Do not try, and do not return a bare INCOMPLETE. Instead:
>
> 1. Do "Before anything else" and "Plan first" as usual.
> 2. Return the plan with a **routing brief**: one row per step, in build order.
>
>    | Step | Agent | Skill | Inputs | QA gate / done when |
>    |---|---|---|---|---|
>
>    "Inputs" names the exact files, codes and prior outputs the agent needs. "QA gate" names the
>    check that must pass before the next step starts.
> 3. Say plainly that the main session must dispatch each step, and that the results come back to
>    you for the task report.
> 4. When the results come back, run "Verification" and write the task report as usual. You do
>    not mark any step ✓ that you have not seen evidence for.
>
> The main session dispatches. It does not skip a step or re-order the brief without saying so.

Change the frontmatter `description` clause "delegates to the specialist agents" to "delegates to
the specialist agents (or, as a sub-agent, returns a routing brief for the main session to
dispatch)".

Nothing else in `overseer.md` changes. The Verification list, the filing gate, Authority, and the
task report format stay as they are. `governance/CHANGE_CONTROL.md` §4 item 1 already says an
Overseer running as a sub-agent may not record a decision. This record does not restate that.

## 3. Files that assume the Overseer delegates

Searched for "overseer" outside `legacy/` in `workflows/`, `docs/`, `.claude/`, `standards/`,
`governance/` and `app/`.

| File | What it says | Affected? | Proposed handling |
|---|---|---|---|
| `.claude/agents/overseer.md` lines 3, 39-51 | Overseer delegates and routes | **Yes** | The edit in section 2 |
| `workflows/build-deliverable.md` lines 12-26, 30 | The chain `OVERSEER → RESEARCHER → DESIGNER → AUDITOR → LIBRARIAN → OVERSEER` implies the Overseer dispatches each step | **Yes, implicitly** | Add one line under the chain pointing to `overseer.md` "When you are running as a sub-agent". Do not restate the rule. |
| `docs/SHULLOS_IMPLEMENTATION_PLAN.md` line 456 | Tool grants table lists `Agent` for the Overseer | Yes, as history | `docs/` is the migration record. Leave it as is; this record is the note of what changed. |
| `docs/SHULLOS_IMPLEMENTATION_PLAN.md` line 748 | Weekly loop: "Overseer dispatches Researcher + Janitor" | Possibly | This is a "Proposed loop". The Routine starts a fresh session, so the Overseer there is the main session and has `Agent`. Not affected if that holds. The Secretary checks `workflows/weekly-system-review.md` before implementing. |
| `docs/MOBILE_AND_PROJECT_WORKFLOW.md` line 33 | The chain cannot run in a Claude Project (no subagents) | No | Already about a different surface. It's accurate. |
| `governance/GOVERNANCE.md` line 103; `.claude/agents/auditor.md` line 11; `.claude/skills/audit-deliverable/SKILL.md` line 10; `.claude/skills/verify-content/SKILL.md` line 53; `standards/QA_GATE.md` line 7 | "The Overseer routes the fix" | No | A routing brief is still routing. No change. |
| `.claude/agents/librarian.md` line 23; `standards/DRIVE_ARCHITECTURE.md` lines 151, 163 | Overseer hands the Librarian a filing row and marks it Filed | No | The Overseer still writes the brief and the report. The main session dispatches the Librarian. No change. |
| `app/agents.mjs` lines 66, 82 | The app calls the Overseer as one step and the app code dispatches the others | No | Already uses the model this record proposes. |

## 4. What this does not do

- It does not give a sub-agent Overseer any new tool or authority.
- It does not let the main session skip the QA gate, the filing gate, or the verification list.
- It does not change who records a decision.
- It does not remove `Agent` from the Overseer's `tools:` line (see Recommendation).
