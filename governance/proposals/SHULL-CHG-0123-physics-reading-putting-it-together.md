# SHULL-CHG-0123 — Physics unit readings end with a "Putting It Together" section

> **No LOCKED rule is overridden. Nothing CONFLICT, PROVISIONAL or UNKNOWN is converted.** This adds
> a new Physics rule. No existing rule text is replaced.
>
> **Two labelled edits** (`governance/CHANGE_CONTROL.md` §1):
> - **Edit 1, course fact (Path A).** The rule and its audit check go in `courses/physics/DECISIONS.md`.
>   This change affects Physics only, so under the CLAUDE.md §2 test it belongs in that course's
>   DECISIONS file. Edit 1 is the whole rule.
> - **Edit 2, pointer only.** `workflows/unit-textbook.md` gets two sentences that point to course
>   DECISIONS files for course-specific reading elements. They restate nothing (CLAUDE.md §1). Without
>   them, an Auditor working from the workflow alone could miss the Physics check. Edit 2 changes no
>   behaviour for Chemistry or Geology.
>
> **Change ID allocation caveat.** This draft was written without shell access, so `git fetch origin
> main` could not be run (§2 "Allocating a new Change ID"). In the local checkout
> (`claude/ecstatic-pascal-9cro1w`, reported equal to main), 0122 is the highest ID, and grep finds no
> reference to 0123 or higher. Under §2 this ID is **not allocated** until the record is pushed to
> `origin/main`. The main session must confirm 0123 against a freshly fetched `origin/main` before it
> commits this record.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0123 |
| **Date** | 2026-11-26 |
| **Source** | User. Matt, main session, 2026-11-26. His idea: "for the physics ones, should we apply like a final cross connection at the end to like how previous units are going to connect to this? … motion in 1 and 2 dimensions connect to F equals ma … connect work and force … Should we apply connectors at the end of each unit so that we can kind of describe how all of this is going to connect to one cohesive Newtonian mechanic examples?" The main session proposed a design: a closing section, one problem solved two ways, a chain diagram, a next-unit line, and no new terms or tear-off questions. He was asked "Should every Physics unit reading end with a 'Putting It Together' section: the same problem solved with this unit's tool and an earlier unit's tool, a small chain diagram of the mechanics units, and one line about what's next?" He chose "Physics readings (Recommended)" ("Make it a rule for Physics readings."). He was also asked whether to add it to the filed U4 now, and chose "Yes, revise and re-file". |
| **Current Rule** | None. Neither `courses/physics/DECISIONS.md` nor `workflows/unit-textbook.md` has a closing cross-unit section. Related rules that are **not** replaced: the per-section Connection box (a real-world sidebar, exactly one per section, enforced by `templates/reading/build_reading_docx.py` l.1714–1724), and the cover's Key Refreshers block (`workflows/unit-textbook.md` item 1, which looks back at the start of a reading in all three courses). |
| **Proposed Rule** | Edit 1: a new section, "Unit readings: Putting It Together", in `courses/physics/DECISIONS.md` (exact text below), plus a decision-log entry at the top of the Physics log. Edit 2: two pointer sentences in `workflows/unit-textbook.md` (exact text below). |
| **Supersedes** | Nothing. This is a new Physics rule. The Connection box and Key Refreshers rules stay unchanged and still apply. |
| **Reason** | Matt wants Physics students to see the mechanics units as one connected Newtonian picture, not as separate toolkits. Today no rule asks for this, so each reading would add it or skip it ad hoc. The feature affects one course, so it is a Physics course fact. Writing it down with its limits keeps the section from turning into new content: no new terms, no tear-off questions, and the same sourcing and audit as the rest of the reading. |
| **Affected Agents** | Textbook Page Designer (writes and builds the section), Auditor (new check), Researcher (sources any facts in the problem), Overseer (intake: names the chain for U6 onward, routes the U4 revision). Secretary (implementation only, and only on approval). |
| **Affected Skills** | None edited. `.claude/skills/verify-content/SKILL.md` is unchanged. The Auditor reaches the check through the workflow pointer (Edit 2). |
| **Affected Courses** | Physics only. It covers every Physics unit reading from U1 onward that is new or revised after approval. U0 is excluded (see the rule). **U4 is the first application.** Matt chose "Yes, revise and re-file" for the filed `Unit 4 Reading - Work & Energy`. That revision is a classroom deliverable. It goes through the Overseer as its own build and is not part of this record's implementation. |
| **Risk** | Low. (1) **Builder:** `build_reading_docx.py` has no block for this section yet. It needs a new optional block, which the U4 revision will add (builder notes below). Until then, no Physics reading can be built to the rule. Only U4 exists, so nothing else is affected. (2) **Pagination:** the section adds roughly half a page to a page. The existing blank-back rule (`workflows/unit-textbook.md` step 3) absorbs parity changes before the tear-off. (3) **Scope creep:** the main risk is the section turning into a second lesson. The limits in the rule and the audit check guard against that. |
| **Recommendation** | Approve. Matt chose it ("Physics readings (Recommended)"). One open sub-question for the main session, listed at the end: what U10's next-unit line should say. The draft omits that line for U10. |
| **Decision** | 2026-11-26, user, in the main session. Asked "Approve SHULL-CHG-0123 ('Putting It Together' for every Physics unit reading) as summarized above?" (the rule's placement, three contents, limits, home and audit check were summarized): "Approve". Asked "Unit 10 is the last unit, so it has no 'next unit.' What should its closing line be?": "Look back over the year (Recommended)" — so U10 closes with one sentence tying the course together instead of omitting the line. |
| **Status** | **APPROVED** |
| **Implemented By** | — |
| **Verified** | — |

---

## What changes, exactly

| Edit | File | Change | Protected? |
|---|---|---|---|
| 1a | `courses/physics/DECISIONS.md` | New section "Unit readings: Putting It Together — CONFIRMED", inserted after "Tests — CONFIRMED" and before "Ohio standards" | Yes, Secretary only |
| 1b | `courses/physics/DECISIONS.md` "Decision log" | New entry at the top, above "2026-11-26 — Scoped exception: work space in the U4 reading's On Your Own boxes" | Yes, Secretary only |
| 1c | `courses/physics/DECISIONS.md` header | `**Last updated:**` set to the implementation date | Yes, Secretary only |
| 2 | `workflows/unit-textbook.md` | One paragraph after item 5 of "Prepare the unit reading…", and one bullet at the end of the "Independent accuracy and print review" list | No (it goes in with Edit 1 under this ID) |

Not changed: `templates/reading/build_reading_docx.py` (the builder work goes in with the U4
revision; see below), `.claude/skills/*`, the Connection box and Key Refreshers rules, and every other file.

## Edit 1a: new section for `courses/physics/DECISIONS.md`

```markdown
## Unit readings: Putting It Together — CONFIRMED

> **Every Physics unit reading ends with a "Putting It Together" section.** It shows how this
> unit connects to earlier ones. It does not introduce new content.

**Placement.** After the last numbered section's content, and before the tear-off leaf and any
blank back placed before it (`workflows/unit-textbook.md` step 3). It has no section code. It is
not listed in the cover's In This Unit box, and it gets no tear-off question.

**Contents, in this order:**
1. **One problem, solved two ways.** Solve one problem twice: once with this unit's tool, and
   once with a tool from an earlier unit. Both solutions reach the same answer, and the text says
   so. Example (U4): a crate's final speed, found first from ∑F = ma plus a kinematic equation,
   then from W_net = KE_f − KE_i. Both solutions follow the build rules above: units cancel, the
   sign convention is stated, net force is written ∑F, and g = 9.8 m/s² with its significant
   figures.
2. **A small chain diagram.** For U1–U5 it shows the mechanics units: U1/U2 kinematics → U3
   forces → U4 energy → U5 momentum. From U6 onward it shows the relevant chain of earlier units
   this unit builds on. The Overseer names that chain at intake. Either way, the current unit is
   highlighted by outline or line weight, not a solid fill. Unit numbers and titles come from the
   curriculum map above. They are never typed from memory.
3. **What's next.** One sentence pointing to the next unit, by its number and title from the
   curriculum map. U10 is the last unit and omits this sentence.

**Limits.**
- No new bold terms. Nothing here counts toward the ten vocabulary terms.
- No tear-off question draws on this section, on either side of the leaf.
- No new content. Every equation and idea used has already been taught in this unit or an
  earlier one.
- Facts and numbers are sourced, solved independently and audited like the rest of the reading.
- It does not replace the per-section Connection box or the cover's Key Refreshers.
- U0 has no earlier unit, so it gets no Putting It Together section, just as it gets no Key
  Refreshers. A reading filed before SHULL-CHG-0123 gets the section only at a revision, and
  only if the teacher asks. U4 is the first application.

**Audit check.** The Auditor confirms that:
- the section sits after the last numbered section and before the tear-off leaf and any blank
  back;
- both solutions, solved independently from the printed givens, agree on the same answer to the
  same significant figures;
- the second tool really belongs to an earlier unit in the curriculum map;
- the chain diagram's unit numbers and titles match the map, the highlighted unit is the current
  one, and the diagram reads in grayscale at print size;
- the next-unit sentence names the correct unit;
- there is no bold term and nothing not already taught, and no tear-off question draws on the
  section.

A failure goes back to the designer, like any other reading finding.
```

## Edit 1b: decision-log entry (top of the Physics log)

The main session records Matt's words in the Decision field. The implementer copies them from
there, verbatim, into the quoted part.

```markdown
### 2026-11-26 — Unit readings end with "Putting It Together"
Every Physics unit reading from U1 onward ends with a "Putting It Together" section, placed after
the last section and before the tear-off leaf. It has one problem solved two ways (this unit's
tool and an earlier unit's), a small chain diagram of the units with the current one highlighted,
and one sentence about the next unit. It adds no bold terms, no tear-off question and no new
content. The rule and its audit check are the "Unit readings: Putting It Together" section above.
Asked whether every Physics unit reading should end this way, Matt chose "Physics readings
(Recommended)" ("Make it a rule for Physics readings."). Asked whether to add it to the filed U4
reading now, he chose "Yes, revise and re-file". U4 is the first application.
Supersedes: None (new rule; the Connection box and Key Refreshers rules are unchanged).
Status: CONFIRMED · SHULL-CHG-0123
```

## Edit 2: pointer text for `workflows/unit-textbook.md`

After item 5 of "Prepare the unit reading and its detachable submission", before "Print at the
intended scale…", insert:

```markdown
**Course-specific reading elements.** A course's `DECISIONS.md` may add a reading element for that
course alone, e.g. the Physics "Unit readings: Putting It Together" section. Build it as that file
says; this workflow does not restate it.
```

At the end of the "Independent accuracy and print review" bullet list, append:

```markdown
- Check any course-specific reading element against the audit check in that course's
  `DECISIONS.md`.
```

## Builder note (for the U4 revision; not part of this record's implementation)

The reading builder needs a new **optional** block, e.g. `"type": "puttingTogether"`. Observations from
`templates/reading/build_reading_docx.py`:

- **Use a new block type, not `example` or `connection`.** l.1721 refuses an `example` or
  `onYourOwn` whose `n` is not the current section. A second `connection` in the last section
  would break the "exactly one Connection box" check at l.1723.
- **Refuse bold inside it.** The vocabulary check (l.1702–1710) scans only `p` blocks. The new
  type should join the `opener`/`connection` bold refusal at l.1726.
- **Make it re-solvable.** `check_worked` (l.1427–1438) re-solves only `example` and `onYourOwn`
  blocks that carry `verify`. Extending it to the new block, with one `verify` per solution and a
  check that the two answers agree, gives the "same answer" claim a machine check.
- **Position check.** It must be the last body block, after the last section's content.
- **Chain titles.** Read the chain's unit titles from `courses/physics/DECISIONS.md`, the same way
  section titles are read now (l.1686–1687), rather than typing them in the spec.
- **Keep it optional.** Leave the block optional in the builder, so Chemistry and Geology are
  unaffected. The Physics requirement is enforced by the Auditor through Edit 1a. Making the builder
  require it for Physics would need its own record.

## Open sub-question for the main session (one question)

For U10, the last unit, the draft **omits** the next-unit sentence. The alternative is a closing
sentence that looks back over the course. This only matters when U10 is built, so it does not block
approval.

## Verification plan (for a checker other than the implementer, after approval)

1. The implementing commit's diff touches only `courses/physics/DECISIONS.md` (Edits 1a–1c),
   `workflows/unit-textbook.md` (Edit 2), this record's `Implemented By`/`Verified`, and its
   `change-log/CHANGELOG.md` row. The commit message carries SHULL-CHG-0123.
2. The new DECISIONS text matches Edit 1a byte for byte. The Worksheets, Tests and curriculum-map
   sections are byte-identical before and after.
3. The quoted words in the log entry match the recorded Decision field verbatim.
4. `python3 scripts/validate_references.py` and `python3 scripts/validate_change_ids.py` pass.
5. Fill in `Implemented By` with the commit SHA and `Verified` with the results. The U4 revision
   is verified separately, through the Overseer's QA gate.
