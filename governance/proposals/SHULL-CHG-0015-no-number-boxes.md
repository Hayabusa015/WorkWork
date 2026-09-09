# SHULL-CHG-0015 — A numbered list is just the number

| Field | Value |
|---|---|
| **Date** | 2026-09-09 |
| **Source** | User instruction: *"when we have a numbered list, please do not put a square box around the number. Just put the number. On any format. Anything. Labs, guidance notes, worksheets."* |
| **Current Rule** | `SHULL_DESIGN_SYSTEM.md` §8 and `NAMING.md` §4: number squares carry problem numbers and organizer unit numbers on print, outlined or light-fill. |
| **New Rule** | **No box, square, circle or marker around a list number. Just the number. Every format, no exceptions.** |
| **Supersedes** | The number-square rule in `SHULL_DESIGN_SYSTEM.md` §8 and `NAMING.md` §4 |
| **Decision** | **Approved by the user** |
| **Status** | **IMPLEMENTED** |

## Where the box was drawn

Three templates, and it was written into four documents as a rule:

| File | Was | Now |
|---|---|---|
| `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` | 14×14pt accent-outlined rounded box | bare number, accent, right-aligned |
| `templates/lab/SHULL_Lab_TEMPLATE_TEACHER_KEY.html` | same, in the warn colour | bare number, warn colour |
| `templates/slide/build.js` layout 05 | **solid asphalt square** behind the step numeral | bare numeral, asphalt |

Documents corrected: `brand/SHULL_DESIGN_SYSTEM.md` §8, `standards/NAMING.md` §4,
`.claude/skills/build-presentation/SKILL.md`, `templates/lab/README.md`.

## Two details worth recording

**The numbers are right-aligned in the hanging indent.** Without a fixed-width box, 9 and 10 would
otherwise start at different places and the text column would wobble. Right-aligning the numeral
holds the text edge straight — the thing the box was doing incidentally.

**The slide numeral changed colour, not just shape.** It was the course accent on a solid asphalt
square. With the square gone it sits on the parchment step card, where a course deep variant
measures 4.8:1 — under the 5.5 target. It is asphalt now, which clears comfortably.

## What this does NOT change

**Circles on dark slide dividers stay.** That is a section marker, not a list number, and
`NAMING.md` now says so explicitly rather than leaving the two rules adjacent and confusable.

Checkbox squares (`☐`) in checklists stay. A checkbox is a thing students mark, not a list number.

## Verification

Lab master and teacher key re-rendered; slide deck rebuilt and re-audited — geometry clean, contrast
clean, no fill introduced. Both crops inspected at 150 dpi.
