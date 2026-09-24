---
id: SHULL-CHG-0024
title: Section-range grammar for multi-section documents — S##.#-S##.#, both halves zero-padded
status: APPROVED
opened: 2026-09-24
decided: 2026-09-24
source: Auditor
decided_by: Matthew Shull
---

# SHULL-CHG-0024 — Section-range grammar

## What happened

A guided-notes packet was built for Geology Unit 2 (Geologic Time), keyed to a single 60-slide
deck — "Earth's History" — that covers all five of U2's confirmed sections (`2.1`–`2.5`, per
`courses/geology/DECISIONS.md`) in one continuous lecture, rather than one section per deck the way
`standards/NAMING.md` assumed. `standards/NAMING.md` §2 defined only the single-section form
`S##.#`; it had no grammar for a document spanning more than one section.

The build used an ad hoc pattern to handle it:

```
SHULL_GEO_Guided_Notes_U02_S02.1-2.5.docx
SHULL_GEO_Guided_Notes_U02_S02.1-2.5_Key.docx
```

— a zero-padded first half and an **unpadded second half** (`2.5`, not `02.5`).

An independent Auditor flagged this as a should-fix/open item: an unsanctioned, undocumented
convention should not quietly become precedent just because it shipped once. Matt was asked
directly — ratify it as the standard pattern for future multi-section decks, keep it a one-off, or
use something else. **He chose: ratify it as the standard**, in conversation, 2026-09-24.

The Auditor separately found that the packet's in-document chip and running footer rendered
un-padded too — `U2 / S2.1–2.5` instead of the fully zero-padded `U02 / S02.1–S02.5`. That is the
second defect this record closes: the rule that chips and footers must match the filename's padding
was previously only implied by §1 ("one system, not four conventions"), never stated for a range.
Leaving it implied is what let the first build drift on both ends at once.

## Current Rule

`standards/NAMING.md` §2, "The grammar" — defines only `S##.#`, a single zero-padded section before
the decimal. No range form exists anywhere in the standard.

## Proposed Rule (now written)

A document built once, keyed to a single deck/lecture whose content spans **multiple consecutive
sections of one unit**, may use a range in place of a single section code:

```
S##.#-S##.#
```

Both halves zero-padded exactly as the single-section form, both carrying the `S`:

```
SHULL_GEO_Guided_Notes_U02_S02.1-S02.5.docx
SHULL_GEO_Guided_Notes_U02_S02.1-S02.5_Key.docx
```

**Not** `S02.1-2.5` — the ad hoc pattern the first build actually used, which drops the second `S`
and its own zero-pad. Retired in favor of the form above.

**The in-document chip and running footer carry the identical zero-padded digits**, typeset with an
en dash rather than the filename's hyphen-minus (the same hyphen-vs-en-dash split
`standards/DRIVE_ARCHITECTURE.md` §"Grammar" already draws between a folder separator and prose):

```
U02 / S02.1–S02.5
```

Not `U2 / S2.1–2.5` — that was the packet's actual first render.

**Scope, stated explicitly so it isn't stretched:** this is for one deck/document genuinely built
once against material spanning multiple sections. It is not a way to avoid picking a single section
for material that actually belongs to just one — that case still gets a plain `S##.#` code, and if
it's unclear which, that's a question to stop and ask, not a reason to reach for a range.

## Supersedes

No prior written rule defined a range grammar, so nothing in the standard is replaced outright.
What this retires is the **undocumented, half-padded pattern used in the first build**:
`S02.1-2.5` in the filename, `U2 / S2.1–2.5` in the chip/footer.

## Where it's written

- `standards/NAMING.md` §2, new subsection "Multi-section ranges — SHULL-CHG-0024"
- `standards/NAMING.md` §4, "The in-document chip" — new paragraph requiring the chip/footer to
  match the filename's zero-padding for a range
- `standards/NAMING.md`, new "Decision log" section at the end of the file (the file had none before;
  this establishes it, following the same dated / Supersedes / Status: CONFIRMED · ID format used in
  every course `DECISIONS.md`)
- `change-log/CHANGELOG.md` — index row added

## Affected

- **Agents:** Designer (builds against it), Auditor (checks against it going forward)
- **Skills:** any notes/practice-set/slide builder that names a document spanning more than one
  section
- **Courses:** all three — this is a build-mechanics (Layer 1) rule, not a course fact. No course
  `DECISIONS.md` is touched by this record.

## Risk

**Low.** Purely additive: it defines a form that did not previously exist and changes no
already-in-use single-section code. The one packet already built under the ad hoc pattern
(`SHULL_GEO_Guided_Notes_U02_S02.1-2.5.docx` and its `_Key`) is **not renamed by this record** — a
rename requires the Librarian's before-and-after log per `standards/NAMING.md` §5 and is a separate
operation, flagged below rather than folded in here.

## Verification

- `standards/NAMING.md` §2 and §4 read the new grammar and rule, both citing SHULL-CHG-0024.
- `standards/NAMING.md` decision log carries the dated entry, Status: CONFIRMED · SHULL-CHG-0024.
- `change-log/CHANGELOG.md` carries an index row pointing at this record.
- Commit carries the Change ID in its message, per `governance/CHANGE_CONTROL.md` §6.

**Implemented By:** (filled in immediately below in a follow-up commit, once this commit's own SHA
is known — see `change-log/CHANGELOG.md` for the same note)
**Verified:** pending — to be confirmed once the commit SHA is recorded

## Not done here — flagged, not fixed

**The already-built packet's filename and chip/footer still carry the old, unpadded pattern.**
Renaming `SHULL_GEO_Guided_Notes_U02_S02.1-2.5.docx` (and its `_Key`) to the corrected
`...S02.1-S02.5...` form, and rebuilding the chip/footer inside it, is a real fix but a separate
operation — a Drive rename needs the Librarian's before-and-after log per `standards/NAMING.md` §5,
and a rebuild needs whichever agent owns that packet's source. Flagged for the Overseer to route.

**`templates/notes/build_notes.py`, line ~131, already assembles a range as**
`f"S{sections[0]}-S{sections[-1]}"` **— which repeats the `S`, matching this rule — but the section
strings it reads out of the spec JSON are stored unpadded** (`"1.2"`, not `"01.2"`), so today's code
would still emit `S1.2-S1.4`, not `S01.2-S01.4`. That's a code defect, not a standards defect, and
outside the Secretary's authority to touch directly (`templates/` is not `brand/`, `standards/`,
`governance/`, or `courses/`). Flagged for the Designer/Auditor.
