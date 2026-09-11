"""Editable SHULL worksheet prototypes, built from course-specific JSON.

python templates/practice/build_practice.py --all --out /absolute/output
python templates/practice/build_practice.py specs/physics.json --out /absolute/output

Templates remain prototypes until the teacher accepts the rendered layouts.
Colors are resolved only from brand/tokens.json. No network or Drive writes.
"""
import argparse
import json
import math
from pathlib import Path
import sys
import zipfile
from copy import deepcopy

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL, WD_ROW_HEIGHT_RULE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from _shullos import section_codes

TOKENS = json.loads((REPO / "brand/tokens.json").read_text(encoding="utf-8"))
INK = TOKENS["ground"]["asphalt"]["hex"].lstrip("#")
LINE = TOKENS["ground"]["graphite"]["hex"].lstrip("#")
MUTED = TOKENS["ground"]["footer"]["hex"].lstrip("#")
WHITE = TOKENS["ground"]["white"]["hex"].lstrip("#")
FONT = TOKENS["typography"]["fallback"]["family"]
CODE = {"chemistry": "CHEM", "physics": "PHYS", "geology": "GEO"}
PAGE_W = 8.5
LEFT = float(TOKENS["print"]["margins"]["left"].removesuffix("in"))
RIGHT = float(TOKENS["print"]["margins"]["right"].removesuffix("in"))
WIDTH = PAGE_W - LEFT - RIGHT
CARD_W, CARD_H, SLOT_W, SLOT_H = 3.65, 1.85, 3.75, 1.95

def validate_spec(s):
    course = s.get("course")
    if course not in CODE:
        raise ValueError("unknown course")
    sec = s.get("section", "")
    if sec not in (section_codes(course) or set()) or int(sec.split(".")[0]) != s.get("unit"):
        raise ValueError("section is not in the authoritative course map")
    for field in ("title", "review", "recap", "directions"):
        if not s.get(field):
            raise ValueError("missing " + field)
    if course == "geology":
        if s.get("equations") or s.get("questions"):
            raise ValueError("Geology has no math or calculation questions")
        cards = s.get("cards", [])
        if len(cards) != 6 or sorted(c["order"] for c in cards) != list(range(1, 7)):
            raise ValueError("six cards need distinct sequence positions")
        if len({c["id"] for c in cards}) != 6:
            raise ValueError("card ids must be distinct")
        return
    questions = s.get("questions", [])
    if len(questions) != 8 or [q["number"] for q in questions] != list(range(1, 9)):
        raise ValueError("practice set requires eight numbered questions")
    if [q["tier"] for q in questions] != ["Warm-up"] * 2 + ["Practice"] * 3 + ["Challenge"] * 2 + ["Connect"]:
        raise ValueError("practice progression must be 2 / 3 / 2 / 1")
    if not s.get("equations"):
        raise ValueError("equations reminder required")
    for q in questions:
        if not q.get("answer"):
            raise ValueError("every question needs a separate-key answer")
        if q.get("figure") not in (None, "calorimeter", "force_graph", "cart"):
            raise ValueError("unsupported figure")
        if course == "physics" and (q.get("work_height") or q.get("lines") or q.get("table")):
            raise ValueError("Physics answers belong in the notebook")
        if course == "chemistry" and q.get("calculation") and not q.get("work_height"):
            raise ValueError("Chemistry calculations require a work box")

def blend(fg, bg, fraction):
    a, b = bytes.fromhex(fg), bytes.fromhex(bg)
    return "".join(f"{round(x * fraction + y * (1-fraction)):02X}" for x, y in zip(a, b))

def border(cell, color=LINE, edges=("top", "left", "bottom", "right"), style="single", sz=6):
    pr = cell._tc.get_or_add_tcPr()
    old = pr.find(qn("w:tcBorders"))
    if old is not None:
        pr.remove(old)
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement("w:" + edge)
        e.set(qn("w:val"), style if edge in edges else "nil")
        e.set(qn("w:sz"), str(sz))
        e.set(qn("w:color"), color)
        borders.append(e)
    pr.append(borders)

def margins(cell, top=60, bottom=60, left=90, right=90):
    pr = cell._tc.get_or_add_tcPr()
    old = pr.find(qn("w:tcMar"))
    if old is not None:
        pr.remove(old)
    mar = OxmlElement("w:tcMar")
    for edge, value in (("top",top),("bottom",bottom),("left",left),("right",right)):
        e = OxmlElement("w:" + edge)
        e.set(qn("w:w"), str(value)); e.set(qn("w:type"), "dxa"); mar.append(e)
    pr.append(mar)

def table(container, widths, rows=1):
    t = container.add_table(rows=rows, cols=len(widths))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for col, width in zip(t.columns, widths):
        col.width = Inches(width)
    for row in t.rows:
        row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
        for c, w in zip(row.cells, widths):
            c.width = Inches(w); border(c, edges=()); margins(c)
    return t

def para(container, text="", size=10.5, bold=False, color=INK, after=3, before=0,
         first=False, align=None, italic=False, keep=False):
    p = container.paragraphs[0] if first else container.add_paragraph()
    if first:
        p.clear()
    f = p.paragraph_format
    f.space_after = Pt(after); f.space_before = Pt(before)
    f.line_spacing = 1.06; f.keep_together = True; f.keep_with_next = keep
    r = p.add_run(text)
    r.font.name = FONT; r.font.size = Pt(size); r.bold = bold; r.italic = italic
    r.font.color.rgb = RGBColor.from_string(color)
    if align is not None:
        p.alignment = align
    return p

def collapse(cell):
    """Remove leading empty paragraph before nested tables and collapse final one."""
    for p in list(cell.paragraphs):
        if not p.text and not p._p.xpath(".//w:drawing"):
            if p._p is not cell._tc[-1]:
                cell._tc.remove(p._p)
            else:
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.line_spacing = Pt(1)
                p.add_run().font.size = Pt(1)

def gap(doc, pt=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = Pt(pt)
    p.add_run().font.size = Pt(1)

def accent(s):
    return TOKENS["courses"][s["course"]]["primaryDeep"]["hex"].lstrip("#")

def code(s):
    return f'{CODE[s["course"]]} · U{s["unit"]:02d} / S{float(s["section"]):04.1f}'

def make_doc(s, key=False):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Inches(PAGE_W); sec.page_height = Inches(11)
    sec.top_margin = Inches(0.50)
    sec.bottom_margin = Inches(float(TOKENS["print"]["margins"]["bottom"].removesuffix("in")))
    sec.left_margin = Inches(LEFT); sec.right_margin = Inches(RIGHT)
    sec.header_distance = Inches(0.18); sec.footer_distance = Inches(0.19)
    normal = doc.styles["Normal"]
    normal.font.name = FONT; normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(3)
    for style in ("Title", "Heading 1", "Heading 2"):
        doc.styles[style].font.name = FONT
        doc.styles[style].font.color.rgb = RGBColor.from_string(INK)
    doc.core_properties.author = "Matthew Shull"
    doc.core_properties.title = s["title"] + (" Teacher Key" if key else "")
    doc.core_properties.subject = "SHULL worksheet prototype"
    p = para(sec.header, f'SHULL {s["course"].upper()}  ·  JAMES A. GARFIELD LOCAL SCHOOLS',
             7, True, MUTED, first=True, after=0)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(WIDTH), WD_ALIGN_PARAGRAPH.RIGHT)
    foot = sec.footer
    p = para(foot, f'SHULL SCIENCE  ·  {"TEACHER KEY" if key else "SECTION PRACTICE"}',
             7, True, MUTED, first=True, after=0)
    # A right tab positions the code and page fields without an extra table.
    from docx.enum.text import WD_TAB_ALIGNMENT
    p.paragraph_format.tab_stops.add_tab_stop(Inches(WIDTH), WD_TAB_ALIGNMENT.RIGHT)
    r = p.add_run("\t" + code(s) + "  ·  ")
    r.font.name = FONT; r.font.size = Pt(7); r.font.color.rgb = RGBColor.from_string(MUTED)
    for instr in ("PAGE",):
        fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), instr); p._p.append(fld)
    return doc

def heading(doc, s, continuation=False, key=False):
    p = para(doc, s["title"] + (" Teacher Key" if key else ""), 25 if not continuation else 20,
             True, after=1)
    p.style = doc.styles["Title"]
    para(doc, s["subtitle"] if not continuation else "Continue in your notebook" if s["course"]=="physics" else "Apply and connect",
         10.5, color=MUTED, after=5)
    p = para(doc, code(s) + ("  ·  ANSWERS AND TEACHER NOTES" if key else "  ·  " + s["duration"]), 8.5, True, accent(s), after=5)
    if not key:
        fields = table(doc, [WIDTH*.46, WIDTH*.22, WIDTH*.14, WIDTH*.18])
        for c, txt in zip(fields.rows[0].cells, ["NAME", "DATE", "PERIOD", "SCORE"]):
            margins(c, 20, 20, 0, 80)
            para(c, txt + "  " + "_" * (28 if txt=="NAME" else 10 if txt=="DATE" else 6),
                 8.5, color=MUTED, first=True, after=2)
        gap(doc, 3)

def equation_bar(doc, s):
    para(doc, "EQUATIONS TO USE", 8.5, True, accent(s), after=2)
    eqs = s["equations"]
    t = table(doc, [WIDTH/len(eqs)]*len(eqs))
    for c, eq in zip(t.rows[0].cells, eqs):
        margins(c, 0, 0, 0, 60)
        if eq.get("plain"):
            para(c, eq["plain"], 11, True, first=True, after=0)
        else:
            inner = table(c, [.52, WIDTH/len(eqs)-.58])
            lhs, rhs = inner.rows[0].cells
            for cell in (lhs,rhs):
                margins(cell,0,0,0,0)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            para(lhs, eq["lhs"]+" =", 10.5, True, first=True, after=0)
            frac = table(rhs, [WIDTH/len(eqs)-.62], 2)
            for cell, txt in zip((frac.cell(0,0),frac.cell(1,0)), (eq["num"],eq["den"])):
                margins(cell,0,0,20,20)
                para(cell,txt,10.5,first=True,after=0,align=WD_ALIGN_PARAGRAPH.CENTER)
            border(frac.cell(0,0), edges=("bottom",), sz=5)
            collapse(rhs); collapse(c)
    para(doc, s["equation_note"], 8.5, color=MUTED, after=5, before=2)

def top_review(doc,s):
    para(doc, "QUICK REVIEW", 8.5, True, accent(s), after=2)
    para(doc,s["review"],10.5,after=4)
    para(doc, "BEFORE YOU START  " + s["recap"],9.5,after=4)
    if s.get("equations"):
        equation_bar(doc,s)
    para(doc,s["directions"],9.5,after=4)
    if s.get("rubric"):
        para(doc,s["rubric"],8.5,True,color=MUTED,after=6)

def sketch_asset(kind, destination):
    """Scientific figures are drawn deterministically, never generated."""
    dest = destination / (kind + ".png")
    if dest.exists():
        return dest
    scale=3
    im=Image.new("RGB",(1200,420),tuple(bytes.fromhex(WHITE)))
    d=ImageDraw.Draw(im); col=tuple(bytes.fromhex(LINE))
    f=ImageFont.truetype(str(REPO/"brand/fonts/Archivo-Regular.ttf"),27)
    bold=ImageFont.truetype(str(REPO/"brand/fonts/Archivo-Bold.ttf"),28)
    def line(points,width=3): d.line(points,fill=col,width=width)
    def text(x,y,s,b=False):d.text((x,y),s,font=bold if b else f,fill=col)
    def arrow(a,b):
        line([a,b],4)
        ang=math.atan2(b[1]-a[1],b[0]-a[0])
        pts=[b,(b[0]-14*math.cos(ang-.45),b[1]-14*math.sin(ang-.45)),
             (b[0]-14*math.cos(ang+.45),b[1]-14*math.sin(ang+.45))]
        d.polygon(pts,fill=col)
    if kind=="calorimeter":
        # Cross-section; leader endpoints identify actual visible components.
        line([(230,135),(260,350),(550,350),(580,135)],5)
        line([(246,135),(275,335),(535,335),(565,135)],3)
        line([(212,128),(595,128)],5)
        line([(255,220),(552,220)],4)
        d.rounded_rectangle((397,40,415,272),radius=8,outline=col,width=3)
        for y in range(70,190,20):line([(397,y),(405,y)],2)
        d.ellipse((391,262,421,292),outline=col,width=3)
        line([(418,84),(670,84)]);text(685,66,"A __________________")
        line([(478,242),(670,242)]);text(685,222,"B __________________")
        line([(550,320),(670,350)]);text(685,330,"C __________________")
        text(50,375,"Cross-section • not to scale")
    elif kind=="force_graph":
        ox,oy=125,322
        for x in (0,1,2,3,4):
            px=ox+x*205;line([(px,oy),(px,oy+8)],2);text(px-7,oy+13,str(x))
        for y in (0,2,4,6):
            py=oy-y*40;line([(ox-8,py),(ox,py)],2);text(ox-40,py-16,str(y))
        arrow((ox,oy),(1040,oy));arrow((ox,oy),(ox,26))
        line([(ox,oy-170),(ox+820,oy-170)],5)
        text(22,1,"Fparallel (N)",True);text(650,376,"Position along motion (m)")
        text(480,42,"Constant force",False)
    elif kind=="cart":
        line([(150,300),(1070,300)])
        d.rectangle((440,150,690,258),outline=col,width=4)
        for x in (485,645):d.ellipse((x-23,255,x+23,301),outline=col,width=4)
        text(510,183,"4.0 kg",True)
        arrow((710,199),(1000,199));text(790,146,"10. N push",True)
        arrow((420,224),(250,224));text(168,172,"2.0 N friction",True)
        text(310,340,"Starts from rest • level floor • 3.0 s")
    else:
        raise ValueError(kind)
    im.save(dest)
    return dest

def add_figure(container, kind, assets, width):
    p=container.add_paragraph()
    p.paragraph_format.space_after=Pt(1)
    p.add_run().add_picture(str(sketch_asset(kind,assets)),width=Inches(width))
    p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    p._p.xpath(".//wp:docPr")[0].set("descr", {
        "calorimeter":"Calorimeter cross-section with three leaders A, B, and C for students to label.",
        "force_graph":"Force versus position graph: constant positive six newtons from zero to four meters.",
        "cart":"Four kilogram cart pushed right by ten newtons against two newtons of friction."}[kind])

def work_box(container,height):
    t=table(container,[WIDTH-.15])
    r=t.rows[0];r.height=Inches(height);r.height_rule=WD_ROW_HEIGHT_RULE.AT_LEAST
    c=r.cells[0];border(c,blend(INK,WHITE,.55),sz=6)
    c.vertical_alignment=WD_ALIGN_VERTICAL.CENTER
    para(c,"Show work here",13,color=blend(INK,WHITE,.15),first=True,after=0,
         align=WD_ALIGN_PARAGRAPH.CENTER)

def ruled(container,count):
    for _ in range(count):
        p=para(container,"",after=0)
        p.paragraph_format.line_spacing=Pt(18)
        pr=p._p.get_or_add_pPr();pb=OxmlElement("w:pBdr");e=OxmlElement("w:bottom")
        for k,v in {"val":"single","sz":"6","color":blend(INK,WHITE,.35),"space":"1"}.items():
            e.set(qn("w:"+k),v)
        pb.append(e);pr.append(pb)

def question(doc,s,q,assets,checks=True):
    t=table(doc,[WIDTH]);c=t.cell(0,0);margins(c,0,0,0,0)
    para(c,f'{q["number"]}.  {q["concept"]}',11.5,True,first=True,after=2)
    para(c,q["tier"].upper(),8,True,accent(s),after=2)
    prompt=q["prompt"]
    # Lettered subparts stay full-size and each gets its own line.
    import re
    parts=re.split(r"\s+(?=\([a-e]\))",prompt)
    for part in parts:
        para(c,part,10.5,after=2)
    if q.get("figure"):add_figure(c,q["figure"],assets,min(WIDTH-.2,6.2))
    if s["course"]=="physics" and q["number"]==8:
        add_figure(c,"cart",assets,6.6)
    if q.get("table"):
        data=q["table"];tbl=table(c,[2.35,2.65,WIDTH-5.2],len(data["rows"])+1)
        for i,values in enumerate([data["headers"]]+data["rows"]):
            for cell,txt in zip(tbl.rows[i].cells,values):
                border(cell,blend(INK,WHITE,.45),sz=5)
                margins(cell,55,55,90,90)
                para(cell,txt,9.5,i==0,first=True,after=0)
            if i==0:tbl.rows[i]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
    if q.get("check") and checks:
        para(c,"["+q["check"]+"]",8.5,color=MUTED,after=3)
    if q.get("work_height"):work_box(c,q["work_height"])
    if q.get("lines"):ruled(c,q["lines"])
    collapse(c);gap(doc,6 if s["course"]=="chemistry" else 10)

def build_student(s,assets,checks):
    doc=make_doc(s);heading(doc,s);top_review(doc,s)
    if s["course"]=="geology":
        geo_grid(doc,s,False)
        doc.add_page_break()
        heading(doc,s,True)
        para(doc,"YOUR TIMELINE",11.5,True,accent(s),after=3)
        para(doc,"Read across each row, then move down: 1 → 2, then 3 → 4, then 5 → 6. Place all six cards before gluing.",10,after=5)
        geo_grid(doc,s,True)
        para(doc,"EXPLAIN ONE CHANGE",9,True,accent(s),before=5,after=2)
        para(doc,s["reflection"],10,after=2);ruled(doc,2)
    else:
        split=99
        for q in s["questions"]:
            question(doc,s,q,assets,checks)
    return doc

def geo_grid(doc,s,targets,key=False):
    w,h=(SLOT_W,SLOT_H) if targets else (CARD_W,CARD_H)
    cards=sorted(s["cards"],key=lambda c:c["order"]) if targets else s["cards"]
    # Separate rows ensure the six physical cards retain one shared size.
    for rowid in range(3):
        t=table(doc,[w,WIDTH-2*w,w])
        for colid in range(2):
            c=t.cell(0,colid*2);card=cards[rowid*2+colid]
            t.rows[0].height=Inches(h);t.rows[0].height_rule=WD_ROW_HEIGHT_RULE.AT_LEAST
            border(c,blend(INK,WHITE,.65),style="single" if targets else "dashed",sz=6)
            margins(c,70,55,110,110)
            if targets and not key:
                para(c,f'GLUE HERE  ·  {rowid*2+colid+1}',8.5,True,MUTED,first=True,after=0)
            else:
                para(c,("STAGE "+str(card["order"]) if key else "CARD "+card["id"]+"  ·  CUT ON DASHES"),8,True,MUTED,first=True,after=3)
                para(c,card["title"],12,True,after=3)
                para(c,card["text"],10,after=5)
                if key:
                    para(c,"A drawing could show: "+card["drawing"],9.5,color=MUTED,after=0)
                else:
                    para(c,"SKETCH AND LABEL ONE FEATURE",8,True,accent(s),after=1)
                    inner=table(c,[w-.2])
                    inner.rows[0].height=Inches(.63)
                    inner.rows[0].height_rule=WD_ROW_HEIGHT_RULE.AT_LEAST
                    border(inner.cell(0,0),blend(INK,WHITE,.35),sz=5)
                    collapse(c)
        gap(doc,7)

def build_key(s):
    doc=make_doc(s,True);heading(doc,s,key=True)
    if s["course"]=="geology":
        para(doc,"SEQUENCE  B → D → F → A → E → C",12,True,accent(s),after=7)
        geo_grid(doc,s,True,True)
        para(doc,"Reflection examples",11.5,True,before=5)
        para(doc,"Cloud to collapse: gravity gathers spread-out gas and dust. Disk to growing worlds: pieces join into larger bodies. Young Sun to clearer system: much of the surrounding gas disperses while planets and smaller objects remain.",10)
        doc.add_page_break();heading(doc,s,True,True)
        para(doc,"Teacher preparation",13,True)
        para(doc,s["teacher_notes"],11,after=9)
        para(doc,"Look for",12,True)
        para(doc,"Six cards in the simplified order; a meaningful sketch and at least one label on each; one explanation that describes a physical change. Do not score artistic polish. Accept a verbal explanation alongside a student's labeled drawing when needed.",11,after=9)
        para(doc,"Science nuance",12,True)
        para(doc,"These are milestones rather than six isolated events. Accretion and disk clearing overlap the evolution of the young star; planets need not be complete before fusion begins. Winds, outflows, radiation, and planet formation all contribute to disk evolution. Asteroids and comets are among the leftovers.",11,after=9)
    else:
        for q in s["questions"]:
            if q["number"]==5:
                doc.add_page_break();heading(doc,s,True,True)
            para(doc,f'{q["number"]}. {q["concept"]}',12,True,after=4,before=5)
            para(doc,q["answer"],11,after=11)
        para(doc,"Teacher notes",12,True,before=8)
        para(doc,s["teacher_notes"],10,after=5)
    para(doc,"Content references",10,True,before=8)
    for url in s.get("sources",[]):para(doc,url,8.5,color=MUTED,after=3)
    return doc

def save_dotx(source,dest):
    with zipfile.ZipFile(source) as src, zipfile.ZipFile(dest,"w",zipfile.ZIP_DEFLATED) as out:
        for name in src.namelist():
            data=src.read(name)
            if name=="[Content_Types].xml":
                data=data.replace(b"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml",
                                  b"application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml")
            out.writestr(name,data)

def build(s,out,checks=True):
    validate_spec(s);out.mkdir(parents=True,exist_ok=True)
    assets=out/".assets";assets.mkdir(exist_ok=True)
    kind="Activity" if s["course"]=="geology" else "Practice_Set"
    stem=f'SHULL_{CODE[s["course"]]}_{kind}_U{s["unit"]:02d}_S{float(s["section"]):04.1f}'
    student=out/(stem+".docx");key=out/(stem+"_Key.docx")
    build_student(s,assets,checks).save(student)
    build_key(s).save(key)
    save_dotx(student,out/(f'SHULL_{CODE[s["course"]]}_Worksheet_TEMPLATE.dotx'))
    return student,key

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("spec",nargs="?");ap.add_argument("--all",action="store_true")
    ap.add_argument("--out",required=True,type=Path)
    ap.add_argument("--no-checks",action="store_true")
    args=ap.parse_args()
    files=sorted((HERE/"specs").glob("*.json")) if args.all else [Path(args.spec)]
    for path in files:
        s=json.loads(path.read_text(encoding="utf-8"))
        for produced in build(s,args.out,not args.no_checks): print(produced)

if __name__=="__main__":main()
