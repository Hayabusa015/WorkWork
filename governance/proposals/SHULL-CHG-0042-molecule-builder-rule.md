# SHULL-CHG-0042 — Molecular structures are built with the molecule script

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0042 |
| **Date** | 2026-10-16 |
| **Source** | User — Matt, current conversation, 2026-10-16. Prompted by the commit on branch `ccr-0e393b80-9whfe8` that added `scripts/build_diagram_molecule.py` (SMILES to branded PNG via RDKit; formula and molar mass computed from the same molecule) and `scripts/science_tools.py`. |
| **Current Rule** | See §1 below, verbatim, with file and section. |
| **Proposed Rule** | See §2 below, verbatim. |
| **Supersedes** | Refines, does not replace, `.claude/skills/build-presentation/SKILL.md` §Images (line 68): "Anything students **read** as science is hand-built. Anything they only **look** at may be generated." That sentence stays. The new rule carves out one class of figure (molecular structures) and names how it is built. No rule is deleted. |
| **Reason** | A hand-drawn or AI-generated structure can disagree with its own label, and nobody catches it at a glance (the same argument `build-presentation` §Images makes about Bohr diagrams). The script derives picture, formula, and molar mass from one SMILES, so they cannot disagree. Matt wants it used automatically whenever a structure is drawn or needed. |
| **Affected Agents** | Builder agents that load the four build skills; Auditor (new checklist line); Secretary (implementation only, and only upon approval). |
| **Affected Skills** | `build-presentation`, `build-document`, `build-lab`, `build-assessment`, `audit-deliverable`. `verify-content` is referenced, not edited. |
| **Affected Courses** | All three. Chemistry mainly; Geology and Physics rarely. No course `DECISIONS.md` is touched (build mechanics, not a course fact). |
| **Risk** | Low |
| **Recommendation** | Approve. |
| **Decision** | Approved by Matthew Shull, 2026-10-16 ("Approve it, have the Secretary apply it"). |
| **Status** | **APPROVED** |
| **Implemented By** | (not yet implemented) |
| **Verified** | no (not yet implemented) |

---

## 1. Current Rule — verbatim

### 1a. `.claude/skills/build-presentation/SKILL.md`, "Images" (lines 66-70)

> Anything students **read** as science is hand-built. Anything they only **look** at may be generated.
> A generated Bohr diagram will have the wrong electron count in a way nobody catches at a glance.
> Geology specimen photographs for identification are **shot, never generated**.

### 1b. The four insertion points (text each new item sits beside)

| Skill | Section (line) | Text the new item sits beside |
|---|---|---|
| `build-presentation` | "Images" (68-70) | 1a above. New item follows directly after it. |
| `build-document` | "Every document" (47-53) | "**Ruled lines are for prose. Open boxes are for math.** This holds everywhere." New item follows it. |
| `build-lab` | "The rules that are not yours to change" (24-37) | "- **Every formula appears with its name.**" New item follows it. |
| `build-assessment` | "Every item" (11-20) | "- Uses vocabulary already taught, or defines it." New item follows the list. |
| `audit-deliverable` | "4. Then the rest of the gate" (48-53) | "Clipped text — highest priority, scan every page edge · page budget · grayscale · codes match and exist in the decisions file · voice · separate answer key · every number re-solved." New check is added to this list. |

Exact line numbers are approximate and will be re-read by the Secretary at implementation time.

## 2. Proposed Rule — verbatim

1. Add to `.claude/skills/build-presentation`, `build-document`, `build-lab`, `build-assessment`: any
   molecular structure appearing on a student-facing page is produced with
   `scripts/build_diagram_molecule.py` from a SMILES string. Never hand-drawn, never AI-generated,
   never a pasted web image. If RDKit cannot draw it well (large polymers, crystal lattices, etc.),
   stop and ask Matt — do not improvise.
2. Every SMILES string is verified against the source by `verify-content` before the figure is built.
   The script's `--name` label is typed by the builder and is not checked by the script.
3. Add a line to the `audit-deliverable` checklist: flag any molecular structure not produced by the
   script.

## 3. Scope limits

- **Molecules only.** Does not cover Bohr models, ionic lattices, or other non-molecule figures. Those
  stay hand-built (per the unchanged `build-presentation` §Images) until each gets its own script.
- **The audit line is a backstop, not a guarantee.** It relies on the Auditor recognising a structure
  on the page and checking how it was made.
- **The `--name` label is not checked by the script.** Only the SMILES-derived picture, formula, and
  molar mass are mutually consistent. A wrong name over a correct structure passes the script.

## 4. Enforcement note

**The rule is only as strong as the audit.** A hook cannot detect molecule content: a hand-drawn or
pasted structure is just an image to any mechanical check. So enforcement is the skill text for
builders, `verify-content` for the SMILES, and the `audit-deliverable` line as the last gate. If the
Auditor misses it, nothing else will.

## 5. Out of scope — separate future proposals

- A `pint`-based randomized-problem builder.
- A `mendeleev` cross-check of element data.

Neither is authorised or implied by this record. `scripts/science_tools.py` is mentioned only as
background; no rule here depends on it.

## 6. Conflicts

None found with a LOCKED rule. The `build-presentation` §Images sentence is kept intact and the new
rule adds a specific method for one class of figure. No CONFLICT, PROVISIONAL, or UNKNOWN item is
converted by this record.

## 7. Not done by this record

No skill, standard, brand, or course file was edited. `change-log/CHANGELOG.md` was not edited. This
is a proposal only; implementation waits for a committed record with `Status: APPROVED` and a
verbatim `Decision:` quote (`governance/CHANGE_CONTROL.md` §4).

## 8. Verification plan (for the Secretary, after approval)

- Each of the five skill files contains the new text at the cited section and nothing else changed
  (`git diff` limited to those files plus the record and changelog row).
- `scripts/validate_references.py` and `scripts/validate_agents.py` pass.
- `scripts/build_diagram_molecule.py` is run once on a known SMILES to confirm the path cited in the
  skills resolves and the script executes.
- Fill in `Implemented By` with the commit SHA and `Verified` with the result.
