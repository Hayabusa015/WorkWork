# SHULL-CHG-0098 — Watch item: notes pages that pass LibreOffice verify spill in Word and Google Docs

> **Watch item, single instance.** Nothing is proposed for adoption yet. If it recurs, a follow-up
> record proposes the default. No conflict with a LOCKED rule is known.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0098 |
| **Date** | 2026-11-22 |
| **Source** | Researcher finding, weekly sweep 2026-11-22 (`reports/2026-W47/researcher.md` row 13) |
| **Current Rule** | `templates/notes/README.md`, "How a page is held to one sheet": pages are measured by `--verify`, which renders with LibreOffice. `stretchHeadroomIn` is not documented there. |
| **Proposed Rule** | None now. If it recurs: make a headroom default in `templates/notes/build_notes_docx.py` and document it in the README section above. |
| **Supersedes** | Nothing. |
| **Reason** | Geology U3 pages that passed `--verify` spilled in Word/Google Docs on Matt's screen (2026-11-12). The fix was a per-spec `stretchHeadroomIn: 0.85`, used only in the Geo U3 spec files (and read by `build_notes_docx.py`; grep 2026-11-22). Physics U3 notes do not carry it. `SHULL-CHG-0068-print-document-format-fixes.md` also warns that "Word may place a line slightly differently". The verifier checks a different renderer from the one Matt opens files in. |
| **Affected Agents** | Builder, Auditor. |
| **Affected Skills** | build-document. |
| **Affected Courses** | All three (notes builder is shared). |
| **Risk** | Low. |
| **Recommendation** | Watch the next sweep. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |
