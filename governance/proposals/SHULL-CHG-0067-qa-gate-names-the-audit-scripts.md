# SHULL-CHG-0067 — The QA gate names the slide audit; Auditor and Designer point at it

> **Change ID is provisional.** Allocated as the next integer after `SHULL-CHG-0066`, itself
> provisional, on a freshly fetched `origin/main` (2026-11-09). The session that wrote it can push
> only to its own branch, `claude/blissful-dijkstra-xkbx5q`. Under `governance/CHANGE_CONTROL.md`
> §2 the ID is not real until this record reaches `origin/main`.
>
> No conflict with a LOCKED rule is known.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0067 |
| **Date** | 2026-11-09 |
| **Source** | User. Matt asked the main session on 2026-11-09 to improve the agents, then said: "yes to A, B, C and draft D and E". This is E. The Secretary did not write this record; the main session drafted it at the user's request. |
| **Current Rule** | See §1, verbatim. |
| **Proposed Rule** | See §2. Two options. Option B is recommended. |
| **Supersedes** | Option A: nothing; it adds lines to `.claude/agents/auditor.md` and `.claude/agents/designer.md`. Option B: nothing; it adds one line to `standards/QA_GATE.md`, "Deliverable-specific additions", Slide decks. |
| **Reason** | The mechanical checks exist as scripts, but the two agents that must run them are not told their names. `standards/QA_GATE.md` names `audit_print_ink.py` (§5) and `audit_fonts.py --key` (§1). It does not name `audit_slide_geometry.py`; that appears only in the `build-presentation` skill and `templates/slide/README.md`, which the Auditor is not told to read. A contrast failure sat in the Chemistry sample deck from 2026-10-28 until a manual run on 2026-11-09 (SHULL-CHG-0066 item 1). |
| **Affected Agents** | Auditor, Designer. |
| **Affected Skills** | None. `audit-deliverable` was not re-read this session; check whether it already names the script before implementing. |
| **Affected Courses** | None. |
| **Risk** | Low. |
| **Recommendation** | Option B. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

Drive verification is not needed; this is a repository-only change.

---

## 1. Current Rule — verbatim

`.claude/agents/auditor.md`:

> Run `standards/QA_GATE.md` in full.

> - **Render it and look at it.** Then check `pdffonts`: Archivo or Archivo Narrow. DejaVu or
>   Liberation means the render used different metrics than the classroom copy will.

`.claude/agents/designer.md`, "Before handing off":

> Run the QA gate yourself. Render it and look at it. Confirm `pdffonts` shows Archivo, not DejaVu or
> Liberation

`standards/QA_GATE.md`, "Deliverable-specific additions", Slide decks: a list of what must be true
of a deck. It names no command.

## 2. Proposed Rule

**Option A — name the scripts in the two agent files.** Each agent gains a short "Run these"
list: `audit_slide_geometry.py` for a deck, `audit_print_ink.py` for a print PDF,
`audit_fonts.py` for any rendered PDF.

Cost: the script names would then live in the QA gate and in two agent files. That is the
duplication `CLAUDE.md` §1 exists to prevent, and the copies will drift when a script is added.

**Option B — recommended. Put the missing name in the QA gate, once.** Add one line to
`standards/QA_GATE.md`, Slide decks:

> Run `python3 scripts/audit_slide_geometry.py <deck>.pptx`. It must report zero problems.

The agent files are not changed. Both already say to run the QA gate, so they pick the line up.
The script name then lives in one authoritative place, beside the two it already names.

## 3. Questions for Matt

1. Option A or option B?
2. Should "zero problems" be a hard requirement, or may the Auditor pass a deck with a recorded
   exception? Proposed: hard requirement, since the audit already separates navigation text from
   content.

## 4. Verification, once implemented

- `validate_references.py` and `validate_agents.py` pass.
- A grep shows `audit_slide_geometry.py` named in `standards/QA_GATE.md`.
