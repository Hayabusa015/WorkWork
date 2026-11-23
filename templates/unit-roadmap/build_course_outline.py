#!/usr/bin/env python3
"""Course Outline builder (SHULL-CHG-0106).

    python3 templates/unit-roadmap/build_course_outline.py chemistry

One page, filed at the front of the class binder: every unit by phase, with its taught sections.
No dates, quarters or pacing. Writes the HTML and PDF to output/<course>/reference/ under the
course-level Reference name (standards/NAMING.md §2), then checks the page count is exactly 1.

Everything printed comes from courses/<course>/DECISIONS.md through the same parser as the Unit
Roadmap (build_unit_roadmap.unit_from_decisions): unit titles, phases, section codes and titles.
Retired, dropped and folded codes are skipped. The unit and section counts are counted, not typed.
"""
import html, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO / "templates"))
from build_unit_roadmap import unit_from_decisions, tag_html, CHEM_PAIR  # noqa: E402
from _shull_name import document_name, reference_titles  # noqa: E402

TOPIC = "Course Outline"           # its REF row in the course Short titles table
GRADES = "Grades 10–12"            # as on every Unit Roadmap spec
BODY = {"chemistry": CHEM_PAIR, "physics": "phys", "geology": "geo"}   # same pairing as the roadmaps (SHULL-CHG-0109)


def course_map(course):
    """[(phase number, phase name, [(unit, title, [(code, title, tags)])])] in curriculum order."""
    text = (REPO / "courses" / course / "DECISIONS.md").read_text()
    m = re.search(r"^## Curriculum map.*?(?=^## )", text, re.S | re.M)
    if not m:
        raise SystemExit(f"no curriculum map in courses/{course}/DECISIONS.md")
    phases = []
    for line in m.group(0).splitlines():
        p = re.match(r"^### Phase (\d+) — (.+?) \(", line)
        if p:
            phases.append((int(p.group(1)), p.group(2), []))
        u = re.match(r"^\*\*U(\d+) ", line)
        if u and phases:
            n = int(u.group(1))
            _, title, sections = unit_from_decisions(course, n)
            phases[-1][2].append((n, title, sections))
    return phases


def render(course):
    phases = course_map(course)
    units = [u for _, _, us in phases for u in us]
    n_sections = sum(len(s) for _, _, s in units)
    bands = []
    for num, name, us in phases:
        cols = []
        for n, title, sections in us:
            lis = "".join(f'<li><span class="sc">{c}</span>{html.escape(t)}{tag_html(tags)}</li>'
                          for c, t, tags in sections)
            cols.append(f'<div class="unit"><div class="uh"><span class="ub">U{n}</span>'
                        f'<span class="cnt">{len(sections)} sections</span></div>'
                        f'<div class="ut">{html.escape(title)}</div><ul class="secs">{lis}</ul></div>')
        rng = f"U{us[0][0]}–U{us[-1][0]}" if len(us) > 1 else f"U{us[0][0]}"
        bands.append(f'<section class="phase"><div class="ph"><span>Phase {num} · {html.escape(name)}</span>'
                     f'<span class="rng">{rng}</span></div><div class="units">{"".join(cols)}</div></section>')
    word = course.title()
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{word} Course Outline</title>
<link rel="stylesheet" href="../../../templates/lab/shull-lab-tokens.css">
<link rel="stylesheet" href="../../../templates/_shull_header.css">
<link rel="stylesheet" href="../../../templates/unit-roadmap/unit_roadmap.css">
<link rel="stylesheet" href="../../../templates/unit-roadmap/course_outline.css">
</head><body class="{BODY[course]}">
<span class="code-string">SHULL SCIENCE · {word.upper()} · U{units[0][0]}–U{units[-1][0]}</span>
<header class="rm-head"><div class="rm-top"><div class="rm-left">
<div class="rm-chip">Course Outline</div>
<div class="rm-kick"><span class="sh-course"></span> · Phases 1–{len(phases)}</div></div>
<div class="sh-meta rm-meta"><div><b class="sh-teacher"></b> · High School <span class="sh-course"></span></div><div class="sh-school"></div>
<div>{len(units)} units · {n_sections} sections · {GRADES}</div></div></div>
<h1 class="rm-title">{html.escape(word)} <span class="rm-acc">Roadmap</span></h1></header>
{"".join(bands)}
<section class="okey"><span><b>U#</b> unit number</span>
<span><b>S#.#</b> section: 7.4 (written S7.4) is Unit 7, Section 4</span>
<span><b class="tag">EXT</b> extension (bonus) section</span></section>
</body></html>'''
    return page, len(units), n_sections


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    course = sys.argv[1]
    if TOPIC not in reference_titles(course):
        raise SystemExit(f"'{TOPIC}' is not a REF row in courses/{course}/DECISIONS.md Short titles")
    page, n_units, n_sections = render(course)
    out = REPO / "output" / course / "reference"
    out.mkdir(parents=True, exist_ok=True)
    name = document_name("Reference", [], None, topic=TOPIC, scope="course")
    html_path = out / name.replace(".pdf", ".html")
    html_path.write_text(page)

    from weasyprint import HTML
    doc = HTML(filename=str(html_path)).render()
    pdf = out / name
    doc.write_pdf(pdf)
    pages = len(doc.pages)
    print(f"{pdf.relative_to(REPO)}  units={n_units} sections={n_sections} pages={pages}")
    if pages != 1:
        print("FAIL: the Course Outline is one page. Never shrink the type; raise it with the teacher.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
