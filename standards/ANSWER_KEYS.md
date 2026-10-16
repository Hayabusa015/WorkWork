# Answer Keys — the handwritten look

**Authority:** SHULL-CHG-0043 (Stage 2: Items C, D, H), SHULL-CHG-0044 Item F (name the token,
never a font).
**Drawn by:** `scripts/key_solution.py` and `scripts/key_ink.py`. The `"steps"` and `"sketch"` spec
schema is documented **once**, in the docstring of `scripts/key_solution.py`. This file does not
restate it.
**Face and inks:** the key-handwriting face (`typography.keyHandwriting`) and the `keyInk` colour
tokens, all in `brand/tokens.json`. No font name and no hex value is written here.

This is the whole rule. Skills point here and restate none of it.

---

## 1. Scope

**Teacher answer keys only** — the separate `Key` file (`standards/NAMING.md` §2). Student pages are
never handwritten and are unchanged: they stay in the brand face.

A question opts in by carrying `"steps"` in its spec. **A question without `"steps"` keeps its typed
solution until it is given steps.** That is a complete, valid key; nothing blocks on the look.

## 2. Who writes what

| Ink token | Used for |
|---|---|
| `keyInk.pencil` | Math: every physics and chemistry calculation, and every label on a sketch |
| `keyInk.pen` | Written answers and non-math keys, e.g. an electron configuration |
| `keyInk.box` | The box around a final answer or key result, and the boxed unknown on a sketch |
| `keyInk.arrow` | Arrows, vectors, and notes ("carry this", "because", the name of a move) |

All of it in the key-handwriting face (`typography.keyHandwriting`). Boxes and arrows differ **by
shape** as well as colour — a closed rectangle against an open line with a head — so a photocopy
still tells them apart (`standards/QA_GATE.md` §4).

## 3. Strike-through

A crossed-out attempt appears **only for a mistake students genuinely commonly make**, never an
invented one. A short note in the arrow ink names the mistake. "Common" comes from the course
`DECISIONS.md` misconception list or from Matt; if neither supports it, there is no strike-through.

## 4. Algebra steps

The simple algebraic steps are shown. **Each step is on its own line**, with the operation applied
to both sides.

```
2x + 4 = 6        subtract 4 from both sides
    2x = 2        divide both sides by 2
     x = 1
```

A note that names a move is written **in words** — "divide both sides by 2", never a symbol.

## 5. Division is stacked

**Every division in a calculation step is a stacked fraction:** numerator, a bar, denominator.
Never a divide sign, never a slash between numbers or variables.

**Exception (Matt's decision):** a slash inside a unit name — m/s, g/mol — is a label, not a division
step, and stays inline.

## 6. Physics scene sketch

When a physics problem has a story behind its math, the key carries a small scene sketch above or
beside the worked solution.

1. **Built from the problem's own givens, never AI-generated.** The sketch is drawn from the same
   spec data as the question and the solution, so a label cannot disagree with the numbers. Every
   given is labelled with value and unit; the unknown is labelled with its unit and **boxed**.
2. **Drawn in pencil.** Matt: "Sketch is fine. Make it look like its being drawn in pencil." Lines
   look hand-drawn in `keyInk.pencil`; vectors keep the arrow ink and the unknown keeps the box ink.
3. **No sketch is better than a wrong one.** Where the scene builder would misrepresent the story —
   vertical or inclined motion, a multi-phase problem, anything its templates do not model — the
   sketch is **omitted**. The worked solution still carries the key.
4. Physics only, for now. Chemistry story problems and any student-page sketch are out of scope.

## 7. Legibility beats authenticity

If any character could be misread, the key has failed its job and the look yields. Watch
specifically for:

- **2 read as a**, and **1 read as l** (or I);
- **decimal points** — they must stay clear, never lost or mistaken for another mark;
- a heavy colon or period read as a different mark;
- an exponent or subscript read as a coefficient, and a stacked fraction that renders wrongly.

Where a character or step is ambiguous, that character or step falls back to the face's fallback
named in the token, or to the brand face. **A key is never shipped ambiguous.**

## 8. The arithmetic is still re-solved

The handwritten look changes nothing about `standards/QA_GATE.md` §9. `verify-content` re-solves every
number from the problem statement, each parallel version included, and reads each handwritten step
**as printed**, not as the builder meant it. Every label on a sketch — value, unit, direction — is
checked against the problem statement the same way.

## 9. The audit

Rendered keys are **visually inspected page by page** (`audit-deliverable`). No hook can see a wrong
glyph, so this inspection is the last gate. `scripts/audit_fonts.py --key` admits the
key-handwriting face on `Key` files only; on a student file it is a fail.
