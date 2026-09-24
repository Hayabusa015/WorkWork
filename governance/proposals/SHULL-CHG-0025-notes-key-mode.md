---
id: SHULL-CHG-0025
title: Guided-notes --key mode — student copy and key from one spec, one renderer
status: APPROVED
opened: 2026-09-24
decided: 2026-09-24
source: Coordinator session (code, written and tested) + Matthew Shull (approval)
decided_by: Matthew Shull
---

# SHULL-CHG-0025 — Guided-notes key mode

## What happened

`templates/notes/build_notes_docx.py` is the canonical, production ("Option A") renderer for SHULL
guided/Cornell notes packets — governed by `governance/proposals/SHULL-CHG-0014-guided-notes-template.md`
and documented in `templates/notes/README.md`. `.claude/skills/build-document/SKILL.md`, section
"Guided and Cornell notes", already states the requirement in one line: **"Always two files —
student copy and filled key — generated from the same source so they cannot drift."**

The renderer never did this. It had exactly one rendering mode: blanks and ruled lines for every
recall line, unconditionally, off whatever the spec's `notes` array held. There was no `--key`
flag, no filled-answer output, nothing.

This was a half-finished feature, not a hypothetical gap. `templates/notes/recall.py`'s `offences()`
already reads a notes line defensively as either a plain string or a dict — `entry if isinstance(entry,
str) else entry.get("text", "")` — anticipating a `{"text": ..., "key": ...}` shape. The renderer's
actual loop never read that shape; it assumed every notes line was a plain string (`n.startswith(...)`)
and would have raised on a dict. The check was written for a shape the renderer never implemented.

There was also a latent, related leak: a `problem` block's `"answer"` field printed unconditionally
(`if prob.get("answer"): para(notes, prob["answer"], 9.5)`), with no student/key gate at all. No
shipped spec had used it yet, so it had not leaked in practice — but the first spec that added a
worked-example answer would have put it on the student copy too.

Both are fixed together in the same code change, because both are the same student-vs-key gate.

## Current behavior (before this change)

- One rendering mode. `build_notes_docx.py specs/<spec>.json out.docx` always produces the student
  variant — blanks and ruled lines for every recall line.
- A notes line could only be a plain string; a `{"text", "key"}` dict would crash the renderer,
  despite `recall.py` already checking that shape.
- A `problem` block's `"answer"` field rendered on every copy, unconditionally, with no mode check.
- No key file has ever been produced by this pipeline. Every guided-notes packet shipped from this
  renderer to date is student-copy-only.

## New behavior (already written and tested in `build_notes_docx.py`)

1. **A `--key` CLI flag.** `python3 build_notes_docx.py --key specs/<spec>.json out.docx`. Without
   it, output is byte-for-byte the same as before — verified against both existing example specs
   (`specs/geo_u01_s01.2-s01.4.json`, `specs/phys_u01_s01.1-s01.4.json`).
2. **A `row.notes` line may be a plain string (unchanged) or `{"text": "<line with a blank>", "key":
   "<the filled answer>"}`** — the shape `recall.py` already expected and checked against.
3. **In `--key` mode:** a dict notes line renders its `key` text — bold, in the display accent
   colour — in place of the blank ruled lines. A `problem` block's `answer` now prints **only** in
   `--key` mode, never on the student copy. A must-write line (`*`/`✎` prefix) renders identically
   in both modes, since it was already a complete statement, not a blank.
4. **Data-quality gate.** In `--key` mode, a plain-string notes line that still contains a run of
   underscores (a blank) or ends in a colon (a "Define X:" label needing an answer under it), and
   has no `key` field to fill it, makes the build refuse — naming the section and the offending
   line. Same "the build refuses" posture this renderer already uses for the recall/question rule
   (SHULL-CHG-0023) and the problem/work-box rule (SHULL-CHG-0016). An incomplete key does not ship
   silently.
5. **Output naming and footer.** `--key` mode appends `_Key` to the default output filename (when no
   explicit output path is given) and appends `  ·  KEY` to the running footer, so a key page is
   visually self-identifying without opening it.

**Option B is explicitly out of scope.** `templates/notes/build_notes.py` (the HTML→PDF renderer)
does not get `--key` in this change. This is the same asymmetry `templates/notes/README.md` already
documents for Option B lacking work boxes, the equation bar, and diagram blocks: Option B renders
the Cornell structure only, and a spec that needs the missing feature is refused by Option B rather
than built short.

## Supersedes

No prior written *rule* is replaced outright — `.claude/skills/build-document/SKILL.md`'s "always
two files" line was already correct; nothing in it changes. What this record retires is the gap
between that stated rule and the code: the renderer's previous unconditional single-variant
rendering, and the previous unconditional printing of a `problem` block's `answer` field
(`build_notes_docx.py`, pre-fix: `if prob.get("answer"): para(notes, prob["answer"], 9.5)`, no mode
gate). Both are named here so the prior behavior is on the record, not just silently replaced.

## Where it's written

- `templates/notes/build_notes_docx.py` — the fix itself. Already written and tested by the
  coordinator session; **not touched by the Secretary** (outside the Secretary's authority to edit
  directly — `templates/` is not `brand/`, `standards/`, `governance/`, or `courses/`).
- `templates/notes/recall.py` — **no change needed.** Its `offences()` function already read a notes
  line as `{"text": ...}` when the entry was not a plain string; the renderer has simply caught up
  to the shape the check anticipated.
- `templates/notes/README.md` — new subsection under "## Build" documenting the `--key` flag and the
  `{"text", "key"}` notes-line shape.
- `change-log/CHANGELOG.md` — index row.

## Affected

- **Agents:** Designer (builds guided-notes packets and their keys against this renderer going
  forward), Auditor (checks a shipped packet against this rule — a student copy with a leaked
  answer, or a key with an unfilled blank, are both now things to check for).
- **Skills:** `build-document` — this closes the gap between what the skill already required
  ("always two files") and what the renderer could do.
- **Courses:** all three. Chemistry, Physics, and Geology share this one renderer; no course
  `DECISIONS.md` is touched by this record — this is a build-mechanics (Layer 1) change, not a
  course fact.

## Risk

**Low.** Additive and backward compatible: the default (no `--key`) code path is unchanged and was
verified to still build both existing example specs identically. The new path only activates on an
explicit flag, and it refuses to ship an incomplete key rather than silently producing one.

## Verification

Performed by the coordinator session prior to this record:

- Built both existing example specs (`geo_u01_s01.2-s01.4.json`, `phys_u01_s01.1-s01.4.json`)
  without `--key` — output unaffected by the change.
- Built a patched copy of a spec with `"key"` fields added to every blank-bearing line, with
  `--key` — confirmed the key text filled correctly in place of ruled lines.
- Built the same patched spec **without** `--key` — confirmed the student copy still shows blanks,
  with zero leakage of any `key` text.
- PDF-rendered both outputs and grepped for the filled key text and the `· KEY` footer marker to
  confirm presence in the key build and absence in the student build.

**Implemented By:** pending. The code change already exists in the working tree; this record, the
`templates/notes/README.md` addition, and the `change-log/CHANGELOG.md` row land in the same commit
as that code, made by the coordinator (who holds the git/Bash access this Secretary session does
not). The commit SHA is to be added here once that commit lands, per `governance/CHANGE_CONTROL.md`
— **`Implemented By` is not decoration; a record without it is a claim.**

**Verified:** pending in the same sense — the functional tests above were run and reported by the
coordinator *before* the commit exists to point at. Once committed, this line should be updated to
name who independently confirmed the working tree matches this record (the same caveat
`SHULL-CHG-0024` carries, for the same reason: this Secretary session has no git tool to run that
check itself).

## Decision

Matthew Shull, in conversation, 2026-09-24: **"fix that, it should be added and fixed."** Explicit
approval of the fix described above, including closing the `problem.answer` leak as part of the same
change.
