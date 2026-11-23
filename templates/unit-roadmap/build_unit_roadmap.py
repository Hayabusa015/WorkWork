#!/usr/bin/env python3
"""Unit Roadmap builder (SHULL-CHG-0100).

    python3 templates/unit-roadmap/build_unit_roadmap.py templates/unit-roadmap/specs/chem_u06.json

One page, filed at the front of a unit's binder section. Writes the HTML and PDF to
output/<course>/u<NN>/ under the standards/NAMING.md name, then checks:
  · every taught section in courses/<course>/DECISIONS.md has an entry in the spec, and the spec
    names no section the decisions file does not (codes are never built from a spec alone)
  · the page count is exactly 1

The unit title, phase and section titles are read from DECISIONS.md, never typed in the spec:
a fact lives in one place. The spec holds only what is particular to this page.
"""
import html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "templates"))
from _shull_name import document_name, short_title  # noqa: E402

SKIP = re.compile(r"RETIRED|DROPPED|FOLDED", re.I)


TAG = re.compile(r"\s*`([A-Z]+)`")


def split_tags(title):
    """'Spontaneity `EXT`' -> ('Spontaneity', ['EXT']). A backticked word in the curriculum map
    is a marker (EXT = extension/bonus section), never part of the printed title."""
    return TAG.sub("", title).strip(), TAG.findall(title)


def tag_html(tags):
    return "".join(f' <span class="tag">{html.escape(t)}</span>' for t in tags)


def unit_from_decisions(course, unit):
    """(phase name, unit title, [(code, title, tags)] of taught sections) from the curriculum map.
    tags is a list such as ['EXT']; the title never carries the backticks."""
    text = (REPO / "courses" / course / "DECISIONS.md").read_text()
    phase = None
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^### Phase \d+ — (.+?) \(", line)
        if m:
            phase = m.group(1)
        m = re.match(rf"^\*\*U{unit} (.+?)\*\*", line)
        if not m:
            continue
        title = m.group(1)
        body = []
        for nxt in lines[i + 1:]:
            if not nxt.strip() or nxt.startswith(("**U", "#", "*")):
                break
            body.append(nxt.strip())
        sections = []
        for part in " ".join(body).split(" · "):
            m2 = re.match(rf"^({unit}\.\d+)\s+(.+)$", part.strip())
            if m2 and not SKIP.search(part):
                stitle, tags = split_tags(m2.group(2))
                sections.append((m2.group(1), stitle, tags))
        return phase, title, sections
    raise SystemExit(f"U{unit} is not in courses/{course}/DECISIONS.md. Never build against a code "
                     "that is not there (CLAUDE.md §3).")


def md(s):
    """Spec text: escape, then **bold**, _{sub}, ^{sup}, [[no line break]]."""
    s = html.escape(s)
    s = re.sub(r"\[\[(.+?)\]\]", r'<span class="nw">\1</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"_\{([^}]*)\}", r"<sub>\1</sub>", s)
    return re.sub(r"\^\{([^}]*)\}", r"<sup>\1</sup>", s)


def render(spec):
    course, unit = spec["course"], int(spec["unit"])
    phase, title, sections = unit_from_decisions(course, unit)

    have, want = set(spec["sections"]), {c for c, _, _ in sections}
    if have != want:
        raise SystemExit(f"spec and DECISIONS.md disagree on U{unit} sections: "
                         f"missing from spec {sorted(want - have)}, not in DECISIONS {sorted(have - want)}")

    # Standards are optional. A spec with none (no "standards" on any section, or null) prints no
    # standards column, key or legend. A spec with any must carry them on every section, plus the
    # key, label and source.
    has_std = any(spec["sections"][c].get("standards") for c in want)
    if has_std:
        bare = sorted(c for c in want if not spec["sections"][c].get("standards"))
        if bare or not spec.get("standards_key"):
            raise SystemExit(f"U{unit}: standards are all or nothing; sections without standards {bare}, "
                             f"standards_key {'present' if spec.get('standards_key') else 'missing'}")

    words = title.split()
    head = " ".join(words[:-1]) + (" " if len(words) > 1 else "")
    rows = []
    for code, stitle, tags in sections:
        s = spec["sections"][code]
        ican = "".join(f"<li>{md(t)}</li>" for t in s["ican"])
        std_td = ""
        if has_std:
            stds = "".join(f'<span class="std main">{html.escape(c)}</span>' for c in s["standards"].get("main", [])) + \
                   "".join(f'<span class="std sup">{html.escape(c)}</span>' for c in s["standards"].get("support", []))
            std_td = f"<td>{stds}</td>"
        rows.append(f'<tr><td><span class="num">{code}</span><div class="sname">{html.escape(stitle)}{tag_html(tags)}</div>'
                    f'<div class="focus">{md(s.get("focus", ""))}</div></td>'
                    f'<td><ul class="ican">{ican}</ul></td>{std_td}</tr>')
    prior = "".join(f"<li>{md(p)}</li>" for p in spec["builds_on"])
    measured = "".join(f"<li>{md(m)}</li>" for m in spec["measured"])
    codes = f"U{unit} / S{sections[0][0]}–{sections[-1][0]}" if len(sections) > 1 else f"U{unit} / S{sections[0][0]}"
    course_word = course.title()
    if has_std:
        key = "".join(f"<div><b>{html.escape(c)} {html.escape(n)}:</b> {md(d)}</div>" for c, n, d in spec["standards_key"])
        cols = '<col style="width:22%"><col style="width:57%"><col style="width:21%">'
        std_th = f'<th>{html.escape(spec["standards_label"])}</th>'
        # The legend names only the box kinds this page uses (a unit can have supports and no main).
        kinds = []
        if any(spec["sections"][c]["standards"].get("main") for c in want):
            kinds.append('<span class="std main">Bold box</span> main standard')
        if any(spec["sections"][c]["standards"].get("support") for c in want):
            kinds.append('<span class="std sup">Dashed box</span> supporting standard')
        note = f'<p class="stdnote">{md(spec["standards_note"])}</p>' if spec.get("standards_note") else ""
        keyblock = (f'<div class="keyblock"><div class="label">{html.escape(spec["standards_source"])}</div>\n'
                    f'<div class="key">{key}</div>\n'
                    f'<p class="legend">{" · ".join(kinds)}</p>{note}</div>\n')
        bottom_cls = "bottom"
        tail_note = ""
    else:
        cols = '<col style="width:28%"><col style="width:72%">'
        std_th = keyblock = ""
        bottom_cls = "bottom nostd"
        # A unit with no content statement can say so in one line under the measured box.
        tail_note = f'<p class="stdnote">{md(spec["standards_note"])}</p>' if spec.get("standards_note") else ""

    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Unit {unit} Roadmap</title>
<link rel="stylesheet" href="../../../templates/lab/shull-lab-tokens.css">
<link rel="stylesheet" href="../../../templates/_shull_header.css">
<link rel="stylesheet" href="../../../templates/unit-roadmap/unit_roadmap.css">
</head><body class="{ {"chemistry": "chem", "physics": "phys", "geology": "geo"}[course] }">
<span class="code-string">SHULL SCIENCE · {course_word.upper()} · {codes}</span>
<header class="sh-head"><div class="sh-left">
<div class="sh-kick"><span class="sh-chip">U{unit}</span><span class="sh-course"></span> · Unit Roadmap{(" · " + html.escape(phase)) if phase else ""}</div>
<h1 class="sh-title">{html.escape(head)}<span class="sh-acc">{html.escape(words[-1])}</span></h1></div>
<div class="sh-meta"><div><b class="sh-teacher"></b> · High School <span class="sh-course"></span></div><div class="sh-school"></div>
<div>{len(sections)} sections · {html.escape(spec["grades"])}</div></div></header>
<section class="intro"><div class="idea"><div class="label">Big Idea</div><p>{md(spec["big_idea"])}</p></div>
<div class="prior"><div class="label">Builds On</div><ul>{prior}</ul></div></section>
<table class="sec"><colgroup>{cols}</colgroup>
<thead><tr><th>Section</th><th>I Can… (Learning Targets)</th>{std_th}</tr></thead>
<tbody>{"".join(rows)}</tbody></table>
<section class="{bottom_cls}">{keyblock}<div class="box"><div class="label">How Learning Is Measured</div><ul class="assess">{measured}</ul></div></section>{tail_note}
</body></html>''', course, unit, title


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    spec = json.loads(Path(sys.argv[1]).read_text())
    page, course, unit, title = render(spec)
    out = REPO / "output" / course / f"u{unit:02d}"
    out.mkdir(parents=True, exist_ok=True)
    name = document_name("Roadmap", ["a", "b"], unit, unit_title=short_title(course, f"U{unit}"), ext="pdf")
    html_path = out / name.replace(".pdf", ".html")
    html_path.write_text(page)

    from weasyprint import HTML
    doc = HTML(filename=str(html_path)).render()
    pdf = out / name
    doc.write_pdf(pdf)
    pages = len(doc.pages)
    print(f"{pdf.relative_to(REPO)}  pages={pages}")
    if pages != 1:
        print("FAIL: a Unit Roadmap is one page. Shorten the spec text; never shrink the type.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
