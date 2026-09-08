---
name: verify-content
description: Check the academic and scientific accuracy of a deliverable against the curriculum and against reality - calculations, units, formulas, standards alignment, data interpretation, and safety claims. Use before anything with science in it ships. Reports; never rewrites.
---

# verify-content

Course facts: `courses/<course>/DECISIONS.md`. Integrity rules:
`standards/ANTI_AI_SLOP_STANDARD.md` §4.

## Check, in this order

**1. Does it belong here?** Is the content in this course, this unit, this section — and does the
code exist in the decisions file? Content that is correct but misplaced is still a defect.

**2. Prior knowledge.** Does it assume something not yet taught? Check the sequencing rules — they
differ per course, and the Physics-versus-Chemistry sig-figs difference is the one that bites.

**3. Every calculation, re-solved independently.** Not verified by pattern, not checked against the
key. Worked from the problem statement. **Including in each parallel version.**

**4. Units and significant figures.** Every numeric answer carries a unit. Every setup shows units
cancelling. Precision appropriate to the data.

**5. Formulas.** Correct, and appearing **with their names**.

**6. Data and graphs.** Correct axes, labels, units, scale. Believable measurements with modest
variation — not a perfectly linear trend unless the science calls for it.

**7. Distractors.** Do they represent real student misconceptions? Each course's decisions file
lists the ones worth writing against.

**8. Standards alignment**, when requested. **If the exact code is uncertain, say so rather than
guessing.** A wrong standard code on a document is worse than none.

**9. Safety and disposal.** Every claim verified against the SDS and district policy.
**Never invent a safety claim.** Uncertain handling or disposal is flagged for teacher
verification, not guessed.

## Never

- Fabricate a source, quotation, data origin, accepted value, chemical property, or local policy.
- Present a PROVISIONAL or UNKNOWN item as confirmed.
- Confuse an observation with an inference — in the material, or in your own report.

## Report

| # | Item | Finding | Evidence | Severity | Recommendation |
|---|---|---|---|---|---|

**You recommend. You do not rewrite.** Findings route through the Overseer.
