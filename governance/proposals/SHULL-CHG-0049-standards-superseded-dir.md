# SHULL-CHG-0049 — standards/README.md references a directory that does not exist

| Field | Value |
|---|---|
| **Date** | 2026-10-18 |
| **Source** | Janitor, weekly system review |
| **Resolves** | `standards/README.md` listed a `superseded/` row ("Proposals considered and declined, kept so they are not re-proposed") but `standards/superseded/` was never created. The original finding (filed under the now-void ID SHULL-CHG-0028, see SHULL-CHG-0052) flagged this as a genuine CONFLICT: build the directory, or remove the row, because `governance/proposals/` already has a REJECTED status that serves the same purpose. |
| **Current Rule** | `standards/README.md` documented a directory that does not exist on disk. |
| **Proposed Rule** | Remove the row. `governance/proposals/` (status `REJECTED`, kept rather than deleted per `governance/CHANGE_CONTROL.md` §3) already is the one place a declined proposal lives — a second `standards/superseded/` mechanism would duplicate it, which is the exact defect this system exists to prevent. |
| **Supersedes** | `standards/README.md`'s `superseded/` row |
| **Affected Agents** | None — documentation only |
| **Affected Skills** | None |
| **Affected Courses** | None |
| **Risk** | Low |
| **Recommendation** | Adopt (remove the row, do not build the directory) |
| **Decision** | Approved via the Secretary's Desk dashboard (not a chat message) at 2026-10-22T13:41:00Z. Confirmed in chat 2026-10-22: "scretary desk approved." The choice between removing the row and building the directory was a judgment call made in applying this approval, not separately confirmed — flagging it here per `CLAUDE.md` §2 precedence rules ("stop and ask" when genuinely unclear). If a real need for a standards-level superseded archive shows up later, re-open as a new record rather than reviving this row. |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `standards/README.md` |
| **Verified** | The `superseded/` row no longer appears in `standards/README.md`; `ls standards/` confirms no such directory exists, and `grep -n superseded standards/README.md` returns nothing. |
