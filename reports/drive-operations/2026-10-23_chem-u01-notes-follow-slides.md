# Chemistry U01: guided notes rebuilt to follow the slides, 2026-10-23 (SHULL-CHG-0054)

Approved by the user, 2026-10-23, in the main session: *"Gile them. Old can be trashed"*, answering
"Can I file them? Notes and key into Unit 01's Guided Notes folder, the updated deck into
Presentations" and "should the old deck stay or go to the trash?".

Destinations, verified by lookup before filing:
- `SHULL Science / Chemistry / Unit 01 - Matter & Atomic Structure / Guided Notes` — 1W_-i7xLGYSWNKYs9u5EXf6XMOqTjZ7SG (empty before this operation)
- `SHULL Science / Chemistry / Unit 01 - Matter & Atomic Structure / Presentations` — 1bXTWtzWq-13wNTsz7TVD-pN-BwTRQhbx

Built from `templates/notes/specs/make_chem_u01_s01.1-s01.5_notes.py` (commit 6ddcb61). The deck is the
user's U1 deck with the notes tabs added by a one-off patch (record §7); the deck PDF is not filed,
because its fonts (Poppins, Lato) are not installed in the build container and a PDF made there
substitutes them.

| Operation | Object | ID | Before | After | Status |
|---|---|---|---|---|---|
| Upload (gws, drive.file) then reparent + rename | `Unit 1 Guided Notes - Matter & Atoms.docx` | 1DHsDDUdR3V35k-EspqFzZsZUlieC8uXo | n/a | Guided Notes | done, verified |
| Upload then reparent + rename | `Unit 1 Guided Notes Key - Matter & Atoms.docx` | 14IEn2fQxX4o9L0zyAtw8nMMXuFa_u5XS | n/a | Guided Notes | done, verified |
| Upload then reparent + rename | `Unit 1 Guided Notes - Matter & Atoms.pdf` | 1iTzMs2UFXR-7v0_0Y4qPK7dDerQylnCo | n/a | Guided Notes | done, verified |
| Upload then reparent + rename | `Unit 1 Guided Notes Key - Matter & Atoms.pdf` | 1vI6fQicQ0zHmg-swONHGKiakypnH1ULa | n/a | Guided Notes | done, verified |
| Upload then reparent + rename | `Unit 1 Slides - Matter & Atoms.pptx` | 1RZKMoTZwBEgAvr6gjPCJxHbJaGyS-Thm | n/a | Presentations | done, verified |
| Trash (connector) | `Unit 1 - Matter and Atomic Theory Notes.pptx` (the pre-0054 deck, 110,117 bytes, created 2026-09-15) | 1_U_6sqdSUQbAW3RA8C2x8I9uvqm_XEpi | Presentations (1bXTWtzWq-13wNTsz7TVD-pN-BwTRQhbx) | trash (recoverable) | done, verified |

## Verification, 2026-10-23

An independent `parentId` lookup after the moves found the four notes files in Guided Notes and
`Unit 1 Slides - Matter & Atoms.pptx` beside `1.4 Slides - Isotopes.pptx` in Presentations, each with
the ID above. The Upload Inbox is empty. The old deck no longer lists in Presentations and a metadata
lookup on its ID returns "not found": it is in the trash, recoverable.
