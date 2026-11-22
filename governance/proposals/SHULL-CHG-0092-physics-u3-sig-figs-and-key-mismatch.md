# SHULL-CHG-0092 — Physics U3 answers break the two-sig-fig rule, and the notes and slide keys disagree

> No rule change unless Matt amends the 2026-10-21 entry. Any fix to student material is a classroom
> deliverable and routes through the Overseer, in the same pass as SHULL-CHG-0074.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0092 |
| **Date** | 2026-11-22 |
| **Source** | Researcher finding, weekly sweep 2026-11-22 (`reports/2026-W47/researcher.md` row 4) |
| **Current Rule** | `courses/physics/DECISIONS.md`, 2026-10-21 "Value of g: 9.8 m/s² (two significant figures), Unit 2 onward": "Because 9.8 has two significant figures, answers that depend on g are reported to two significant figures." |
| **Proposed Rule** | Matt confirms whether the rule holds for U3 final answers, with intermediates allowed a guard digit. Then the notes, slides and slide solutions are made to agree. If the rule stands, only unfiled or rebuilt U3 material changes (no-retrofit). |
| **Supersedes** | Nothing, unless Matt amends the 2026-10-21 entry. |
| **Reason** | U3 final answers mostly use three figures: 588 N, 19.6 N, 14.7 N, 24.5 N, 42.4 N, 826 N, 546 N, 36.8 N, 13.1 N, 40.1 N, 2.45 m/s², 3.27 m/s². The notes key and the slide key also round the same problems differently: sled 2.46 vs 2.5; frictionless ramp 3.35 vs 3.4; 25 kg box 1.46 vs 1.5; angled pull 2.51 vs 2.5; 35° incline 2.41 vs 2.4 m/s². The Researcher re-solved 20 slide problems and the notes worked examples by hand; the arithmetic is correct everywhere and only the rounding is inconsistent. |
| **Affected Agents** | Overseer, Builder, Auditor (verify-content). |
| **Affected Skills** | build-document, build-presentation, verify-content. |
| **Affected Courses** | Physics. |
| **Risk** | Medium. A student checking notes against slides sees two different answers to the same problem. |
| **Recommendation** | Ask the question, then fix in the SHULL-CHG-0074 remap pass. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

The values are as the Researcher reported them; the Secretary did not re-solve them.
Files: `templates/notes/specs/make_phys_u03_s03.1-s03.6_notes.py`,
`templates/worksheet/specs/phys_u03_slide_solutions.py`, U3 deck specs.

## Open question

1. Does the two-significant-figure rule hold for U3 final answers, with intermediate steps allowed a
   guard digit?
