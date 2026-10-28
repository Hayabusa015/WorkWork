#!/usr/bin/env python3
"""SHULL Science: project-activity builder (handout, grading sheet, teacher key).

    python3 templates/activity/build_activity.py <spec.json> <out_dir>

One spec makes three PDFs: the student handout, the one-page grading sheet and the
teacher key. The rubric rows live once in the spec and both the handout and the grading
sheet are rendered from them, so the "look for" text cannot drift from the handout.

Visual vocabulary is the lab template's (templates/lab/): the same masthead, eyebrow,
chip, h2 rule and running footer, and the same generated token sheet,
templates/lab/shull-lab-tokens.css. No hex is typed here (validate_tokens.py). Margins
and print sizes are read from brand/tokens.json.

Checks before writing: the section code exists in the course DECISIONS.md, and each
document renders to the page count the spec declares. A miss fails the build. It does
not shrink anything to fit.
"""
import json, os, sys
from html import escape

from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "scripts"))
sys.path.insert(0, os.path.join(REPO, "templates"))
from _shullos import section_codes          # noqa: E402
from _shull_name import document_name       # noqa: E402

TOKENS = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
TOKEN_CSS = os.path.join(REPO, "templates", "lab", "shull-lab-tokens.css")
COURSE_CLASS = {"chemistry": "chem", "physics": "phys", "geology": "geo"}


def css():
    m = TOKENS["print"]["margins"]
    ps = TOKENS["typography"]["printScale"]
    floor = TOKENS["typography"]["floors"]["printBody"]["pt"]
    line_w = TOKENS["print"]["weights"]["writingLine"]["min"]
    return f"""
@page {{
  size: letter;
  margin: {m['top']} {m['right']} {m['bottom']} {m['left']};
  @bottom-left {{
    content: string(foot);
    font-family: var(--display); font-size: {ps['footer']}pt; letter-spacing: 0.14em;
    color: var(--footer); margin-bottom: 0.14in;
  }}
  @bottom-right {{
    content: "PAGE " counter(page) " OF " counter(pages);
    font-family: var(--display); font-size: {ps['footer']}pt; letter-spacing: 0.14em;
    color: var(--footer); margin-bottom: 0.14in;
  }}
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: var(--body); font-size: {ps['body']}pt; line-height: 1.38; color: var(--ink); }}
b {{ font-weight: bold; }}
.foot {{ string-set: foot content(); font-size: 0; height: 0; overflow: hidden; }}
.page {{ page-break-before: always; }}
.page.first {{ page-break-before: auto; }}

/* masthead, page 1 only (lab template) */
.masthead {{ border-bottom: 2pt solid var(--ink); padding-bottom: 7pt; }}
.eyebrow {{ font-family: var(--display); font-weight: 600; font-size: 8pt;
  letter-spacing: 0.22em; color: var(--accent); margin-bottom: 3pt; }}
.titlerow {{ display: flex; align-items: flex-end; }}
h1 {{ font-family: var(--display); font-weight: bold; font-size: 19pt; line-height: 1.1; flex: 1 1 auto; }}
h1 .accent {{ color: var(--accent); }}
.chip {{ flex: 0 0 auto; margin-left: 12pt; font-family: var(--display); font-weight: 600;
  font-size: 8pt; letter-spacing: 0.10em; border: 1.1pt solid var(--accent-display);
  border-radius: 9pt; padding: 2.5pt 9pt; white-space: nowrap; }}

/* page head, pages 2 on */
.pagehead {{ border-bottom: 1.4pt solid var(--ink); padding-bottom: 5pt; margin-bottom: 7pt; }}
.pagehead h1 {{ font-size: 15pt; }}

.id-row {{ display: flex; gap: 16pt; margin: 10pt 1pt 4pt 1pt; }}
.id-row .f {{ border-bottom: 0.9pt solid var(--ink); height: 16pt; }}
.lbl {{ font-family: var(--display); font-size: {floor}pt; letter-spacing: 0.18em; color: var(--label); margin-top: 2.5pt; }}

h2 {{ font-family: var(--display); font-weight: 600; font-size: 9pt; letter-spacing: 0.20em;
  border-bottom: 1pt solid var(--accent-display); padding-bottom: 2.5pt; margin: 11pt 0 5pt 0; }}
p {{ margin-bottom: 6pt; }}
.lead {{ margin-bottom: 7pt; }}

ol.parts {{ list-style: none; counter-reset: q; }}
ol.parts > li {{ counter-increment: q; position: relative; padding-left: 20pt; margin-bottom: 6pt; }}
ol.parts > li::before {{ content: counter(q); position: absolute; left: 0; top: 0;
  font-family: var(--display); font-weight: bold; color: var(--accent); width: 12pt; text-align: right; }}

.hips {{ display: flex; gap: 14pt; margin: 4pt 0 6pt 0; }}
.hip {{ flex: 1 1 0; border-left: 2.5pt solid var(--accent-display); padding: 2pt 0 2pt 9pt; }}
.hip .term {{ font-family: var(--display); font-weight: bold; font-size: 11pt; }}
.hip .plain {{ font-family: var(--display); font-weight: 600; font-size: 8pt; letter-spacing: 0.16em; color: var(--accent); margin-bottom: 3pt; }}
.note {{ border: 1pt solid var(--structure); padding: 6pt 9pt; margin-top: 8pt; }}

ul.dot {{ list-style: none; }}
ul.dot li {{ padding-left: 11pt; position: relative; margin-bottom: 4pt; }}
ul.dot li::before {{ content: ""; position: absolute; left: 0; top: 4pt; width: 3.4pt; height: 3.4pt; background: var(--accent-display); }}

/* tables: hairline rules, no shading */
table {{ border-collapse: collapse; width: 100%; table-layout: fixed; font-size: {ps['tableCell']}pt; line-height: 1.25; }}
th {{ font-family: var(--display); font-weight: 600; font-size: {floor}pt; letter-spacing: 0.08em;
  text-align: left; color: var(--label); border-bottom: 1.2pt solid var(--ink); padding: 3pt 4pt; vertical-align: bottom; }}
td {{ border-bottom: 0.6pt solid var(--rule-hairline); padding: 2.8pt 3.5pt; vertical-align: top; }}
td.name {{ font-weight: bold; }}
tr.group td {{ font-family: var(--display); font-weight: 600; font-size: 8.4pt; letter-spacing: 0.16em;
  color: var(--accent); border-top: 1.2pt solid var(--accent-display); border-bottom: 0.6pt solid var(--rule-hairline); padding-top: 6pt; }}
tr {{ page-break-inside: avoid; }}

.about {{ display: flex; gap: 16pt; font-size: 9.6pt; }}
.about ul {{ flex: 1 1 0; }}

/* outline page */
.zone {{ position: relative; padding: 6pt 8pt; }}
.facts {{ border: 2.2pt solid var(--accent-display); }}
.pics {{ border: 1.6pt dashed var(--ink); }}
.zlabel {{ font-family: var(--display); font-weight: bold; font-size: 9pt; letter-spacing: 0.16em; }}
.facts .zlabel {{ color: var(--accent); }}
.zhint {{ font-size: 8.6pt; color: var(--label); }}
.zrow {{ display: flex; gap: 9pt; margin-bottom: 9pt; }}
.tl {{ display: flex; margin-top: 5pt; border: 0.9pt solid var(--structure); }}
.tl .cell {{ padding: 3pt 6pt; border-left: 0.9pt solid var(--structure); }}
.tl .cell:first-child {{ border-left: none; }}
.tl .pname {{ font-family: var(--display); font-weight: 600; font-size: 8.4pt; letter-spacing: 0.14em; }}
.tl .pdates {{ font-size: 8.4pt; color: var(--label); }}
.tlends {{ display: flex; justify-content: space-between; font-family: var(--display); font-size: {floor}pt;
  letter-spacing: 0.18em; color: var(--label); margin-top: 2pt; }}
.fill {{ display: flex; align-items: flex-end; height: 0.40in; border-bottom: {line_w} solid var(--ink); }}
.fill span {{ font-family: var(--display); font-weight: 600; font-size: 8.2pt; letter-spacing: 0.06em; color: var(--label); padding-bottom: 2pt; }}
.sitedot {{ display: inline-block; width: 7pt; height: 7pt; border-radius: 50%; background: var(--ink); vertical-align: -0.5pt; margin-right: 4pt; }}
.maplegend {{ position: absolute; right: 8pt; bottom: 6pt; border: 0.9pt solid var(--structure); padding: 3pt 7pt; font-size: 8.6pt; }}
.legend {{ font-size: 9pt; margin-top: 5pt; }}
.pick {{ margin-top: 6pt; }}
.formats {{ display: flex; gap: 10pt; font-size: 9.6pt; line-height: 1.32; }}
.fbox {{ border: 1pt solid var(--structure); padding: 6pt 9pt; }}
.fbox p {{ margin-bottom: 4pt; }}
.fnote {{ margin-bottom: 5pt; }}
.ftitle .fl {{ font-family: var(--body); font-weight: normal; letter-spacing: 0; color: var(--ink); font-size: 9.6pt; margin-left: 4pt; }}
.scorebox {{ width: 30pt; }}
.fbox ul.dot li {{ margin-bottom: 3pt; }}
.ftitle {{ font-family: var(--display); font-weight: bold; font-size: 9pt; letter-spacing: 0.16em; color: var(--accent); margin-bottom: 4pt; }}
.parts2 {{ display: flex; gap: 14pt; }}
.parts2 ol {{ flex: 1 1 0; }}
.parts2 ol.parts > li {{ margin-bottom: 4pt; }}
.zlabel .zhint {{ font-family: var(--body); font-weight: normal; letter-spacing: 0; margin-left: 4pt; }}
.outline h2, h2.tight {{ margin-top: 10pt; }}
.zrow .zlabel .zhint {{ display: block; margin-left: 0; }}
.zrow .zone .zhint {{ font-size: 8.4pt; }}
table.aboutt {{ margin-top: 4pt; font-size: 9.4pt; }}
.swatch {{ display: inline-block; width: 22pt; height: 9pt; vertical-align: -1pt; margin-right: 4pt; }}
.swatch.f {{ border: 2.2pt solid var(--accent-display); }}
.swatch.p {{ border: 1.6pt dashed var(--ink); }}

/* plan */
.plan .row {{ display: flex; align-items: flex-end; margin-bottom: 3pt; }}
.plan .row .k {{ flex: 0 0 auto; font-weight: 600; margin-right: 8pt; padding-bottom: 2pt; }}
.plan .row .v {{ flex: 1 1 0; margin-right: 6pt; border-bottom: {line_w} solid var(--ink); height: 20pt; }}
.plan .more {{ border-bottom: {line_w} solid var(--ink); height: 20pt; margin-bottom: 3pt; }}

/* rubric */
table.rub td {{ padding: 5pt 5pt; }}
table.rub td.part {{ font-weight: bold; width: 17%; }}
table.rub td.part .pts {{ display: block; font-weight: normal; font-size: 8.4pt; color: var(--label); }}
table.rub td.score {{ width: 9%; }}
table.sheet td {{ height: 0.62in; }}
.scorebox {{ border: 1pt solid var(--structure); height: 22pt; width: 34pt; }}
.total {{ display: flex; justify-content: flex-end; align-items: center; gap: 8pt; margin-top: 8pt;
  font-family: var(--display); font-weight: bold; font-size: 10pt; letter-spacing: 0.12em; }}
.total .scorebox {{ width: 54pt; height: 24pt; }}
.pointer {{ font-size: 9pt; color: var(--label); margin-top: 8pt; }}
.notes {{ border: 1pt solid var(--structure); height: 2.7in; margin-top: 4pt; }}

/* key */
.key table {{ font-size: 8.6pt; }}
.key ul.dot li {{ font-size: 9.4pt; margin-bottom: 4.5pt; }}
.prov {{ font-family: var(--display); font-weight: 600; font-size: 8pt; letter-spacing: 0.14em; }}
"""


def fmt(s):
    """Spec text is trusted and may carry <i>/<b>; everything else is plain."""
    return s


def masthead(doc, code, idfields=True):
    title = escape(doc["title"])
    acc = doc.get("titleAccent")
    if acc:
        title = title.replace(escape(acc), f'<span class="accent">{escape(acc)}</span>', 1)
    out = [f'<div class="masthead"><div class="eyebrow">{escape(doc["kicker"])}</div>'
           f'<div class="titlerow"><h1>{title}</h1><div class="chip">{escape(code)}</div></div></div>']
    if idfields and doc.get("idFields"):
        cells = "".join(f'<div style="flex:{w}"><div class="f"></div><div class="lbl">{escape(l)}</div></div>'
                        for l, w in doc["idFields"])
        out.append(f'<div class="id-row">{cells}</div>')
    return "".join(out)


def pagehead(kicker, title):
    return (f'<div class="pagehead"><div class="eyebrow">{escape(kicker)}</div>'
            f'<div class="titlerow"><h1>{escape(title)}</h1></div></div>')


def descriptor(level, text):
    return f"{escape(level)}. {fmt(text)}"


# ---------------------------------------------------------------- handout
def page_one(spec, d):
    """Page 1: the job, the condensed outline (top), what the poster needs (bottom)."""
    po = d["pageOne"]; z = po["zones"]
    h = [masthead(d, spec["code"]), f'<h2>{escape(po["jobHeading"])}</h2><p>{fmt(po["job"])}</p>']

    def label(key):
        lab, hint = z[key]
        return f'<div class="zlabel">{escape(lab)} <span class="zhint">{fmt(hint)}</span></div>'

    h.append(f'<h2>{escape(po["outlineHeading"])}</h2><div class="outline">')
    h.append(f'<div class="zone facts" style="height:0.36in;margin-bottom:6pt">{label("name")}</div>')
    cells = "".join(
        f'<div class="cell" style="flex:{p["start"] - p["end"]}"><span class="pname">{escape(p["name"].upper())}</span> '
        f'<span class="pdates">{p["start"]} to {p["end"]}&nbsp;mya</span></div>' for p in spec["periods"])
    h.append(f'<div class="zone facts" style="margin-bottom:6pt">{label("timeline")}<div class="tl">{cells}</div></div>')
    h.append(f'<div class="zrow" style="height:1.55in;margin-bottom:0">'
             f'<div class="zone pics" style="flex:36">{label("drawing")}</div>'
             f'<div class="zone facts" style="flex:28">{label("about")}</div>'
             f'<div class="zone pics" style="flex:36">{label("map")}'
             f'<div class="maplegend"><span class="sitedot"></span>{escape(z["mapLegend"])}</div></div></div>')
    lf, lp, lw = po["legend"]
    h.append(f'<p class="legend"><span class="swatch f"></span>{escape(lf)} &nbsp; '
             f'<span class="swatch p"></span>{escape(lp)} &nbsp; {escape(lw)}</p></div>')

    h.append(f'<h2>{escape(po["needsHeading"])}</h2><div class="parts2">')
    items = [f"<li><b>{escape(a)}</b> {fmt(b)}</li>" for a, b in po["parts"]]
    half = (len(items) + 1) // 2
    h.append('<ol class="parts">' + "".join(items[:half]) + '</ol><ol class="parts" start="4" style="counter-reset: q 3">'
             + "".join(items[half:]) + "</ol></div>")
    h.append('<table class="aboutt"><colgroup><col style="width:16%"><col style="width:84%"></colgroup><thead><tr>')
    h += [f"<th>{escape(c)}</th>" for c in po["aboutColumns"]]
    h.append("</tr></thead>")
    h += [f'<tr><td class="name">{escape(f["label"])}</td><td>{fmt(f["options"])}</td></tr>' for f in spec["aboutFields"]]
    h.append(f'</table><p class="pick">{fmt(po["pick"])}</p>')
    return "".join(h)


def page_plan(spec, d):
    pp = d["planPage"]; rub = spec["rubric"]
    h = [pagehead(pp["kicker"], pp["title"])]
    fm = pp.get("format")
    if fm:
        ps, sl = fm["poster"], fm["slide"]
        note = f'<p class="fnote">{fmt(fm["note"])}</p>' if fm.get("note") else ""
        h.append(f'<h2 style="margin-top:6pt">{escape(fm["heading"])}</h2>{note}<div class="formats">'
                 f'<div class="fbox" style="flex:28"><div class="ftitle">{escape(ps["title"])}</div>'
                 + "".join(f"<p>{fmt(x)}</p>" for x in ps["lines"]) + '</div>'
                 f'<div class="fbox" style="flex:72"><div class="ftitle">{escape(sl["title"])} <span class="fl">{fmt(sl["lead"])}</span></div>'
                 '<ul class="dot">' + "".join(f"<li>{fmt(x)}</li>" for x in sl["bullets"]) + '</ul></div></div>')
    lead = f'<p class="lead">{fmt(pp["planLead"])}</p>' if pp.get("planLead") else ""
    h.append(f'<h2>{escape(pp["planHeading"])}</h2>{lead}<div class="plan">')
    # Each plan row holds one or more [label, flex] fields. flex 0 = label only, no write line.
    for row in pp["fields"]:
        cells = []
        for k, n in row:
            if n == 0:
                cells.append(f'<div class="k" style="padding-bottom:2pt;margin-left:14pt">{fmt(k)}</div>')
            else:
                cells.append(f'<div class="k">{fmt(k)}</div><div class="v" style="flex:{n} 1 0"></div>')
        h.append(f'<div class="row">{"".join(cells)}</div>')
    h.append(f'</div><h2>{escape(rub["heading"])}</h2><table class="rub"><colgroup>'
             '<col style="width:15%"><col style="width:37%"><col style="width:22%"><col style="width:18%"><col style="width:8%"></colgroup><thead><tr>')
    h += [f"<th>{escape(c)}</th>" for c in pp["columns"]]
    h.append("</tr></thead>")
    for r in rub["rows"]:
        lv = r["levels"]
        h.append(f'<tr><td class="part">{escape(r["part"])}<span class="pts">{r["points"]} points</span></td>'
                 f'<td>{descriptor(lv[0], r["full"])}</td><td>{descriptor(lv[1], r["partial"])}</td>'
                 f'<td>{descriptor(lv[2], r["none"])}</td><td class="score"><div class="scorebox"></div></td></tr>')
    h.append(f'</table><div class="total">TOTAL<div class="scorebox"></div>/ {rub["total"]}</div>')
    return "".join(h)


def build_activity(spec, d):
    pages = [page_one(spec, d), page_plan(spec, d)]
    return "".join(f'<section class="page{" first" if i == 0 else ""}">{p}</section>' for i, p in enumerate(pages))


# ---------------------------------------------------------------- grading sheet
def build_rubric(spec, d):
    rub = spec["rubric"]
    h = [masthead(d, spec["code"]), f'<h2>{escape(d["scoreHeading"])}</h2><table class="rub sheet"><colgroup>'
         '<col style="width:16%"><col style="width:36%"><col style="width:14%"><col style="width:10%"><col style="width:24%"></colgroup><thead><tr>']
    h += [f"<th>{escape(c)}</th>" for c in d["columns"]]
    h.append("</tr></thead>")
    for r in rub["rows"]:
        h.append(f'<tr><td class="part">{escape(r["part"])}<span class="pts">{r["points"]} points</span></td>'
                 f'<td>{fmt(r["full"])}</td><td>{" · ".join(escape(x) for x in r["levels"])}</td>'
                 f'<td class="score"><div class="scorebox"></div></td><td></td></tr>')
    h.append(f'</table><div class="total">TOTAL<div class="scorebox"></div>/ {rub["total"]}</div>')
    h.append(f'<p class="pointer">{fmt(d["pointer"])}</p>')
    h.append(f'<h2>{escape(d["notesHeading"])}</h2><div class="notes"></div>')
    return f'<section class="page first">{"".join(h)}</section>'


# ---------------------------------------------------------------- key
def build_key(spec, d):
    h = [masthead(d, spec["code"], idfields=False), f'<h2>{escape(d["factHeading"])}</h2>',
         f'<p class="lead">{fmt(d["factLead"])}</p><table><colgroup>']
    for w in (12, 15, 11, 4, 14, 5, 9, 30):
        h.append(f'<col style="width:{w}%">')
    h.append("</colgroup><thead><tr>" + "".join(f"<th>{escape(c)}</th>" for c in d["factColumns"]) + "</tr></thead>")
    for g in d["facts"]:
        h.append(f'<tr class="group"><td colspan="8">{escape(g["period"].upper())}</td></tr>')
        for r in g["rows"]:
            h.append('<tr><td class="name">' + fmt(r[0]) + "</td>" + "".join(f"<td>{fmt(c)}</td>" for c in r[1:]) + "</tr>")
    h.append("</table>")
    h.append(f'<h2>{escape(d["gradingHeading"])}</h2><ul class="dot">')
    h += [f"<li>{fmt(x)}</li>" for x in d["grading"]]
    h.append(f'</ul><h2>{escape(d["spinoHeading"])}</h2><ul class="dot">')
    h += [f"<li>{fmt(x)}</li>" for x in d["spino"]]
    h.append(f'</ul><h2>{escape(d["mistakesHeading"])}</h2><table><colgroup><col style="width:38%"><col style="width:62%"></colgroup>'
             '<thead><tr><th>STUDENTS SAY OR DRAW</th><th>CORRECTION</th></tr></thead>')
    h += [f"<tr><td>{fmt(a)}</td><td>{fmt(b)}</td></tr>" for a, b in d["mistakes"]]
    h.append("</table>")
    return f'<section class="page first key">{"".join(h)}</section>'


BUILDERS = {"activity": build_activity, "rubric": build_rubric, "key": build_key}


def main():
    if len(sys.argv) != 3:
        print(__doc__); return 2
    spec = json.load(open(sys.argv[1]))
    out_dir = sys.argv[2]; os.makedirs(out_dir, exist_ok=True)

    valid = section_codes(spec["course"]) or set()
    bad = [s for s in spec["sections"] if s not in valid]
    if bad:
        print(f"refused: section(s) {bad} not in courses/{spec['course']}/DECISIONS.md"); return 1

    foot = f'SHULL SCIENCE · {spec["courseLabel"]} · {spec["code"]}'
    failed = 0
    for d in spec["documents"]:
        expect = document_name(d["type"], spec["sections"], spec["unit"], topic=d["topic"],
                               key=d.get("key", False), ext="pdf")
        if expect != d["filename"]:
            print(f"refused: {d['filename']!r} does not follow the naming grammar ({expect!r})"); return 1
        body = BUILDERS[d["kind"]](spec, d)
        html = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
                f'<link rel="stylesheet" href="file://{TOKEN_CSS}"><style>{css()}</style></head>'
                f'<body class="{COURSE_CLASS[spec["course"]]}"><div class="foot">{escape(foot)}</div>{body}</body></html>')
        doc = HTML(string=html, base_url=HERE).render()
        path = os.path.join(out_dir, d["filename"])
        doc.write_pdf(path)
        n = len(doc.pages)
        ok = n == d["pages"]
        failed += not ok
        print(f"{'ok ' if ok else 'FAIL'} {d['filename']}: {n} page(s), budget {d['pages']}")
    if failed:
        print("Over budget. Fix in order: @page margins, base font size, line-height, block margins. "
              "Never shrink one block to fit.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
