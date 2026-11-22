# SHULL-CHG-0096 — Make the lab Alconox/disposal block (and Safety section) conditional on chemicals or glassware

Repeat of: the same one-off exception twice (Physics S1.3 lab, Physics 3.1 lab)

> **CONFLICT WITH A LOCKED RULE.** The lab template is locked (`courses/physics/DECISIONS.md` line
> 409: "Deviation from the locked lab template"), and the Alconox block is stated as verbatim
> boilerplate in `templates/lab/README.md` and the build-lab skill. This record proposes changing
> that rule. **The Secretary does not resolve the conflict.** Matt decides. Until he does, the locked
> rule stands, and each exception still needs its own explicit approval.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0096 |
| **Date** | 2026-11-22 |
| **Source** | Researcher finding, weekly sweep 2026-11-22 (`reports/2026-W47/researcher.md` row 10) |
| **Current Rule** | `templates/lab/README.md` lines 102-103: "**Alconox cleanup block.** Disposal items 4–6 are standing boilerplate. **Keep them verbatim.** Only items 1–3 change per lab." `.claude/skills/build-lab/SKILL.md` lines 31-32: "**The Alconox block** — disposal items 4–6 — is standing boilerplate. **Keep it verbatim.** Only items 1–3 change per lab." |
| **Proposed Rule** | Not adopted. Question for Matt: should the Alconox/disposal block, and the generic Safety section, apply only when a lab uses chemicals or glassware? If yes, this becomes a Path B template change, stated in one place, with the README and skill pointing at it. |
| **Supersedes** | If adopted: `templates/lab/README.md` lines 102-103 and `.claude/skills/build-lab/SKILL.md` lines 31-32, in part. |
| **Reason** | Both Physics labs built so far dropped the block for the same reason: no chemicals or glassware. These are `courses/physics/DECISIONS.md` 2026-09-14 (S1.3 lab, line 409 onward) and 2026-11-12 (3.1 lab, line 276 onward). The 3.1 lab also dropped the Safety section. Each entry says "Not a precedent". This is the same shape as the Physics ramp history (SHULL-CHG-0062): a locked rule that keeps getting a one-off exception for one course. |
| **Affected Agents** | Designer, Builder. |
| **Affected Skills** | build-lab. |
| **Affected Courses** | All three (template is shared). Physics most affected. |
| **Risk** | Medium. It removes safety text from labs. Any condition must be precise enough that a Chemistry or Geology lab with hazards never loses it. |
| **Recommendation** | None. This changes a LOCKED template and the call is Matt's. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. Should the Alconox/disposal block, and separately the generic Safety section, apply only when a lab
   uses chemicals or glassware? Or should the locked rule stand, with exceptions approved one at a
   time?
