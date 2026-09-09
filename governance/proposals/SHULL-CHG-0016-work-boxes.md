# SHULL-CHG-0016 — A problem to solve gets a box to solve it in

| Field | Value |
|---|---|
| **Date** | 2026-09-09 |
| **Source** | Matthew supplied his Physics U1 packet: *"notice how we left boxes for students to work the practice problems. anytime problems need solved in guided notes leave a box for them to do it"* |
| **New Rule** | **Every problem a student is asked to solve in guided notes carries a bordered work box.** Not writing lines — a box, at least 1.4 in tall, that will not split across a page. |
| **Decision** | **Approved by the user** |
| **Status** | **IMPLEMENTED, and enforced at build time** |

Legacy packet snapshotted at `legacy/guided-notes/PHYS_U1_S1.1-S1.4_Guided_Notes.docx`,
md5 `0f07ffa7df40cec6eabefa3350562b7b`.

## What his packet does, measured rather than eyeballed

A worked example in the notes column is four parts, in order:

1. **Label** — `EXAMPLE — THROWN STRAIGHT UP`
2. **Statement** — one or two sentences, with the sign convention stated
3. **GIVEN / NEED table** — 2×2 nested, 0.72 in label column
4. **WORK box** — 1×1 nested table, `trHeight` 1411 dxa (**0.98 in**), `hRule="atLeast"`,
   `cantSplit`, hairline border on all four sides, no fill
5. **Answer line** with blanks

`hRule="atLeast"` and `cantSplit` are the two details that matter and are easy to miss. The box
**grows** if the content needs it but never shrinks below its minimum, and it **never breaks across
a page** — a work box split over a page turn is useless to a student.

Implemented at 1.4 in rather than his 0.98 in: kinematics problems with a sign check need the room,
and `hRule="atLeast"` means the extra costs nothing when it is not used.

## Enforced, not documented

`build_notes_docx.py` refuses to build when a row's label contains EXAMPLE, PRACTICE, PROBLEM,
SOLVE, CALCULATE or YOUR TURN and the row has no `problem` block:

```
build_notes_docx: these rows look like problems to solve and have no work box:
   U1 / S1.1 · WORKED EXAMPLE
   ...
Add a "problem" block, or "noWorkBox": true if it genuinely is not one.
```

The opt-out is explicit and recorded in the spec. A rule that only lives in a document is not a
mechanism — that is the finding T-7 produced three times over, and this one starts as a mechanism.

## Two things found on the way

**A misdetect I caught before building on it.** My first extractor treated "two nested tables" as
the signature of a worked example. That flagged S1.2's *four kinematic equations* reference table —
which is a table of equations, not a problem. Detection now keys on a nested table whose first cell
literally reads `GIVEN`. Precise, and it matches how he actually builds them.

**The work-box label was invisible.** First build put it in `ground.ruleHairline` — the border
colour — which measures **1.62:1 on white**. The border is not read; the label is. It is the course
accent now.

## Not migrated, and it is a real gap

His S1.2 row holds a **4×2 equation table** — each kinematic equation beside "leaves out ______".
The spec has no structure for a table inside a notes cell, so it flattens to text. The notes builder
supports Cornell rows, problems and must-write lines; it does not support arbitrary nested tables.
**Open**, and it will matter for Physics more than for the other two courses.

## Palette and type

His packet uses "Quiet Voltage" (`A97BFF` violet, `0B0A0E` ink) and Poppins/Liberation — superseded
by SHULL-CHG-0002 and -0006. It rebuilds on Quantum Gold Deep and Archivo. Same as SHULL-CHG-0014
finding 1; no new decision.

## Verification

Rebuilt from his own content: 7 pages, 6 work boxes, 6.65% marked, **no solid fills**, Archivo
embedded. The enforcement was tested by stripping every `problem` block from the spec — the build
refused and named all six rows.
