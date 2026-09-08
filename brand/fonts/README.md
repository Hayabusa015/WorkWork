# Fonts

**Archivo** and **Archivo Narrow** — SIL Open Font License, redistributable, committed here.

Chosen in SHULL-CHG-0006 because they are neo-grotesques with true condensed cuts, close in
character to Trade Gothic Next. The previously documented ladder named Poppins, which is geometric
and a poor stylistic match, and which is **not installed in the build container** despite a skill
file asserting that it is.

A SessionStart hook installs these to `~/.fonts` and runs `fc-cache`, so the QA render and the
shipped PDF are the same artifact. Before this, every QA pass inspected Liberation Sans metrics
while the document declared Trade Gothic Next.

**Trade Gothic Next is Monotype-licensed. Never commit it.** It is named first in the font stack so
files resolve correctly on Matt's own machine.

*Status: fonts not yet added. Phase 8.*
