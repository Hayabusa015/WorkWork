"""Checks for the binding side of printed pages, SHULL-CHG-0103.

    python3 templates/test_binding.py

Mirror margins set, the three hole guides present on odd AND even pages and on the
correct side of each, and the hole zone kept clear - in the .docx builders (worksheet,
key, notes, practice prototype), in the WeasyPrint lab template, and in the audit that
checks them (scripts/audit_binding.py), including that it fails a page it should fail.
The rendered checks need LibreOffice (soffice) and are skipped without it.
"""
import glob, json, os, shutil, subprocess, sys, tempfile, unittest
from docx import Document
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _shull_print import BINDING, PAGE_W_IN, guides, hole_zone, page_css, text_block_in  # noqa

AUDIT = os.path.join(REPO, "scripts", "audit_binding.py")
WS = os.path.join(HERE, "worksheet")
EMU_IN, TW_IN = 914400, 1440
TOKENS = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
SOFFICE = shutil.which("soffice")


def to_pdf(docx, outdir):
    subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", outdir, docx],
                   check=True, capture_output=True)
    return os.path.join(outdir, os.path.splitext(os.path.basename(docx))[0] + ".pdf")


def guide_offsets(story_el):
    """x offsets (inches, from the page edge) of the hole guides anchored in a story."""
    out = []
    for anchor in story_el.iter("{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}anchor"):
        doc_pr = anchor.find("{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}docPr")
        if doc_pr is None or not doc_pr.get("name", "").startswith("SHULL hole guide"):
            continue
        ph = anchor.find("{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}positionH")
        assert ph.get("relativeFrom") == "page"
        out.append(int(ph[0].text) / EMU_IN)
    return out


def run_audit(pdf):
    r = subprocess.run([sys.executable, AUDIT, pdf], capture_output=True, text=True)
    return r.returncode, r.stdout


class Tokens(unittest.TestCase):
    def test_values_come_from_tokens(self):
        b, h = TOKENS["print"]["binding"], TOKENS["print"]["holeGuides"]
        self.assertEqual(BINDING.inside_in, float(b["inside"].removesuffix("in")))
        self.assertEqual(BINDING.diameter_in, h["diameterIn"])
        self.assertEqual(BINDING.centres_from_top_in, h["centresFromTopIn"])
        self.assertEqual(BINDING.stroke_hex, TOKENS["ground"][h["stroke"]]["hex"])

    def test_guides_flip_with_parity_and_sit_in_the_zone(self):
        for page in (1, 2, 3, 4):
            x0, x1 = hole_zone(page)
            for x, _ in guides(page):
                self.assertTrue(x0 <= x - BINDING.radius_in and x + BINDING.radius_in <= x1)
        self.assertLess(guides(1)[0][0], PAGE_W_IN / 2)
        self.assertGreater(guides(2)[0][0], PAGE_W_IN / 2)

    def test_css_mirrors(self):
        css = page_css(0.30, 0.35, 0.45)
        self.assertIn(f"@page :right {{ margin: 0.3in 0.35in 0.45in {BINDING.inside_in}in;", css)
        self.assertIn(f"@page :left {{ margin: 0.3in {BINDING.inside_in}in 0.45in 0.35in;", css)


class DocxStructure(unittest.TestCase):
    """The .docx carries mirror margins, even/odd footers, and the guides on each side."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        spec = os.path.join(WS, "specs", "geo_u02_s02.3_dinosaur_poster.json")
        cls.stu = os.path.join(cls.tmp, "stu.docx")
        cls.key = os.path.join(cls.tmp, "key.docx")
        for builder, out in (("build_worksheet_docx.py", cls.stu),
                             ("build_worksheet_key_docx.py", cls.key)):
            subprocess.run([sys.executable, os.path.join(WS, builder), spec, out],
                           check=True, capture_output=True, cwd=WS)
        notes = os.path.join(HERE, "notes")
        cls.notes = os.path.join(cls.tmp, "notes.docx")
        subprocess.run([sys.executable, os.path.join(notes, "build_notes_docx.py"),
                        os.path.join(notes, "specs", "chem_u01_s01.1-s01.5_notes_student.json"),
                        cls.notes], check=True, capture_output=True, cwd=notes)
        pdir = os.path.join(cls.tmp, "practice")
        subprocess.run([sys.executable, os.path.join(HERE, "practice", "build_practice.py"),
                        os.path.join(HERE, "practice", "specs", "physics.json"), "--out", pdir],
                       check=True, capture_output=True, cwd=os.path.join(HERE, "practice"))
        cls.practice = sorted(glob.glob(os.path.join(pdir, "*.docx")))

    def check(self, path, outside_in):
        doc = Document(path)
        st = doc.settings.element
        self.assertIsNotNone(st.find(qn("w:mirrorMargins")), path)
        self.assertIsNotNone(st.find(qn("w:evenAndOddHeaders")), path)
        for s in doc.sections:
            self.assertAlmostEqual(s.left_margin.inches, BINDING.inside_in, places=3)
            self.assertAlmostEqual(s.right_margin.inches, outside_in, places=3)
            odd = guide_offsets(s.footer._element)
            even = guide_offsets(s.even_page_footer._element)
            r = BINDING.radius_in
            self.assertEqual(len(odd), BINDING.count)
            self.assertEqual(len(even), BINDING.count)
            for x in odd:
                self.assertAlmostEqual(x + r, BINDING.centre_from_edge_in, places=3)
            for x in even:
                self.assertAlmostEqual(x + r, PAGE_W_IN - BINDING.centre_from_edge_in, places=3)
            # The even footer says what the odd one says - its running text was copied.
            txt = lambda f: "".join(p.text for p in f.paragraphs)
            self.assertEqual(txt(s.footer), txt(s.even_page_footer))
            self.assertTrue(txt(s.footer).strip())

    def test_worksheet(self):
        self.check(self.stu, 0.5)

    def test_worksheet_key(self):
        self.check(self.key, 0.5)

    def test_notes(self):
        self.check(self.notes, 0.5)

    def test_practice_prototype(self):
        self.assertTrue(self.practice)
        outside = float(TOKENS["print"]["margins"]["right"].removesuffix("in"))
        for p in self.practice:
            self.check(p, outside)

    def test_text_block_is_page_less_both_margins(self):
        import _shull_docx
        self.assertAlmostEqual(_shull_docx.TEXT_W_IN, PAGE_W_IN - BINDING.inside_in - 0.5)
        self.assertAlmostEqual(text_block_in(0.5), _shull_docx.TEXT_W_IN)

    def test_tables_do_not_hang_into_the_margin(self):
        doc = Document(self.stu)
        for tbl in doc.element.body.iterchildren(qn("w:tbl")):
            self.assertIsNotNone(tbl.tblPr.find(qn("w:tblInd")))

    @unittest.skipUnless(SOFFICE, "needs LibreOffice")
    def test_rendered_key_odd_and_even(self):
        """Three pages through LibreOffice: guides left on 1 and 3, right on 2, zone clear."""
        pdf = to_pdf(self.key, self.tmp)
        import pymupdf
        self.assertGreaterEqual(len(pymupdf.open(pdf)), 2, "need an even page to test")
        rc, out = run_audit(pdf)
        self.assertEqual(rc, 0, out)
        self.assertIn("p2  right", out)

    @unittest.skipUnless(SOFFICE, "needs LibreOffice")
    def test_rendered_notes(self):
        rc, out = run_audit(to_pdf(self.notes, self.tmp))
        self.assertEqual(rc, 0, out)


class LabTemplate(unittest.TestCase):
    def test_lab_key_template(self):
        sys.path.insert(0, os.path.join(HERE, "lab"))
        import build_lab
        tmp = tempfile.mkdtemp()
        out = os.path.join(tmp, "key.pdf")
        doc = build_lab.render(os.path.join(HERE, "lab", "SHULL_Lab_TEMPLATE_TEACHER_KEY.html"), out)
        self.assertGreaterEqual(len(doc.pages), 2)
        rc, txt = run_audit(out)
        self.assertEqual(rc, 0, txt)

    def test_templates_set_no_margin_of_their_own(self):
        for f in ("SHULL_Lab_TEMPLATE_MASTER.html", "SHULL_Lab_TEMPLATE_TEACHER_KEY.html"):
            src = open(os.path.join(HERE, "lab", f)).read()
            page = src[src.index("@page {"):src.index("}", src.index("@page {"))]
            self.assertNotIn("margin:", page.split("@")[1], f)


class AuditCatches(unittest.TestCase):
    """The audit fails what it exists to fail."""

    def make(self, draw):
        import pymupdf
        tmp = tempfile.mkdtemp()
        doc = pymupdf.open()
        for n in (1, 2):
            pg = doc.new_page(width=PAGE_W_IN * 72, height=11 * 72)
            draw(pg, n)
        out = os.path.join(tmp, "t.pdf")
        doc.save(out)
        return out

    @staticmethod
    def circles(pg, n, flip=False):
        import pymupdf
        h = BINDING.stroke_hex.lstrip("#")
        col = tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        for x, y in guides(n + (1 if flip else 0)):
            pg.draw_circle(pymupdf.Point(x * 72, y * 72), BINDING.radius_in * 72,
                           color=col, width=max(BINDING.stroke_pt, 0.5))

    def test_clean_page_passes(self):
        rc, out = run_audit(self.make(lambda pg, n: (self.circles(pg, n),
                                                    pg.insert_text((72, 300), "Body text"))))
        self.assertEqual(rc, 0, out)

    def test_ink_in_zone_fails(self):
        rc, out = run_audit(self.make(lambda pg, n: (self.circles(pg, n),
                                                    pg.insert_text((0.66 * 72 if n == 2 else 0.2 * 72, 300), "Punched"))))
        self.assertEqual(rc, 1, out)
        self.assertIn("p1:", out)
        self.assertIn("in the hole zone", out)

    def test_unflipped_guides_fail(self):
        rc, out = run_audit(self.make(lambda pg, n: self.circles(pg, 1)))
        self.assertEqual(rc, 1, out)
        self.assertIn("p2: a hole guide is missing on the right edge", out)

    def test_filled_guides_fail(self):
        import pymupdf
        def draw(pg, n):
            for x, y in guides(n):
                pg.draw_circle(pymupdf.Point(x * 72, y * 72), BINDING.radius_in * 72,
                               color=(0, 0, 0), fill=(0, 0, 0))
        rc, out = run_audit(self.make(draw))
        self.assertEqual(rc, 1, out)
        self.assertIn("guide ink out of bounds", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
