# Fonts

**Archivo** and **Archivo Narrow** — SIL Open Font License, redistributable, committed here.

Chosen in SHULL-CHG-0006 because they are neo-grotesques with true condensed cuts, close in
character to Trade Gothic Next. The previously documented ladder named Poppins, which is geometric
and a poor stylistic match, and which is **not installed in the build container** despite a skill
file asserting that it is.

A SessionStart hook installs these to `~/.fonts` and runs `fc-cache`, so the QA render and the
shipped PDF are the same artifact. Before this, every QA pass inspected Liberation Sans metrics
while the document declared Trade Gothic Next.

**Patrick Hand** — SIL Open Font License, committed here (`PatrickHand-Regular.ttf`,
`OFL-PatrickHand.txt`). Source: `google/fonts` repository, `ofl/patrickhand`. Added by SHULL-CHG-0043
(PROVISIONAL). **Teacher answer keys only, never a student page** — see `typography.keyHandwriting` in
`brand/tokens.json`. It is deliberately outside the Archivo stack; it has no superscript, subscript,
arrow, or Delta glyphs. sha256 of the ttf: `0f173b3e6cb6d1af25babf7f0057c5ac4ee11f9992b0469bb817e967ef4ad0fc`.

**Trade Gothic Next is Monotype-licensed. Never commit it.** It is named first in the font stack so
files resolve correctly on Matt's own machine.
