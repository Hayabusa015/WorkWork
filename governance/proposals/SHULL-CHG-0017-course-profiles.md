# SHULL-CHG-0017 — The three courses are not the same document

| Field | Value |
|---|---|
| **Date** | 2026-09-09 |
| **Source** | User instruction |
| **Decision** | **Approved by the user** |
| **Status** | **IMPLEMENTED, and enforced at build time** |

His words: *"they have different needs, and it's not gonna be the exact template for each one. Each
one will have its own unique feature… but geology doesn't have math."*

---

## 1. A fraction is stacked. Never inline.

> *"I need equations to be on top and bottom of numerator and denominator with the divisor
> horizontally and not inline in the text."*

**He told me this earlier and I never wrote it down.** It is nowhere in the repository — not in the
design system, not in a course decisions file, not in a skill. A stated requirement that vanished
between being said and being recorded is the exact failure this whole system exists to prevent, and
it happened here, to me, on this project. It is a rule with a mechanism now instead of a memory.

`v = Δx/Δt` is wrong. The numerator sits above the denominator with a horizontal bar between them.

### Built as a table, not as Office Math — and that was a real choice

Word's native equation format (OMML) is the obvious answer. I built it, and it is valid: the
`m:oMath` element is correctly formed and present in the file. **LibreOffice will not import OMML
from `.docx`,** so it rendered as nothing in the QA pipeline — the equations simply vanished from
every PDF and raster this system produces.

That makes OMML unverifiable here. Shipping a document whose most important element cannot be
inspected before it goes out breaks the one rule the QA gate is built on: *never ship a document
unseen.*

A two-row table with a bottom border on the numerator renders identically in Word, LibreOffice,
Google Docs and print, and can be checked. **The trade is real and worth stating: these are not
Word equation objects.** The equation editor will not edit them. If that is ever wanted, OMML is the
route, and the cost is that nothing here can see the output.

## 2. Equations go at the top of the page

> *"At the top of each physics or even chemistry worksheet when there's math, we're gonna need to
> put the equations at the top of the page for the students so they know which equations to
> reference."*

An outlined bar, two across, above the learning targets. Fractions stacked, `lhs =` vertically
centred so the equals sign lands on the fraction bar rather than floating above it. Outlined, never
filled — the ink rule from SHULL-CHG-0014 applies.

**Enforced:** a Physics or Chemistry packet with problems to solve and no equation bar **refuses to
build**. Opt out with `"noEquationBar": true`, explicitly, in the spec.

## 3. Geology has no math. Geology labels diagrams.

> *"if we're diagramming the different layers of the earth, it would be cool to have a nice earth to
> label and diagram. Or if we're doing plate tectonics, we can label the different parts of the
> plates and then identify which part is the trench and which part is the mid ocean ridge."*

**A Geology packet carrying an equation bar or a problem block refuses to build.** Not a warning —
a refusal, the same as a bad section code.

The diagram block is Geology's equivalent of the work box: a figure area beside numbered label
lines, sized in inches, that **never splits across a page**. Chemistry and Physics may use it too —
a labelled apparatus or a Bohr diagram is the same thing.

| | Chemistry | Physics | Geology |
|---|---|---|---|
| Equation bar | when there is math | when there is math | **refused** |
| Work box on problems | required | required | **refused** |
| Diagram to label | available | available | **its main feature** |

## Three defects found while building this

**The heading stranded on the previous page.** `cantSplit` keeps a table *row* together; it does
nothing across two rows. The first diagram block put the heading in row 1 and the figure in row 2,
and the page break landed between them — a student gets a box with no instruction above it, which is
worse than no heading. It is one row now.

**Two calls with `first=True` overwrote each other.** `para(..., first=True)` reuses paragraph 0, so
calling it twice appends a run to the same paragraph. The diagram's heading and figure note ran
together as `LABEL THE SUN'S LAYERS[ CROSS-SECTION OF THE SUN ]`. Caught by walking the built
document rather than reading the source.

**Doubled bullets, again.** His Physics packet writes `▸` into the text; the Geology one writes `•`.
The strip list only knew about `•`. There is now one `debullet()` used everywhere instead of three
copies of a character class.

## Verification

Physics: 7 pages, equation bar with three stacked fractions, 6 work boxes, no solid fills.
Geology: 5 pages, diagram block intact on one page, and it refuses to build with math added.
Both Archivo-embedded and inside the ink budget.
