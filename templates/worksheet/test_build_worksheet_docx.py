"""Checks for the opt-in options in build_worksheet_docx.py: the square-box grid layout,
the draw_block number and caption-strip opt-outs, and the inline label bank.

    python3 templates/worksheet/test_build_worksheet_docx.py

Every option here is opt-in. The default path is covered by the regression rebuild of the
committed specs (same document XML before and after), not by these tests.
"""
import copy, json, os, subprocess, sys, tempfile, unittest
from docx import Document
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
BUILDER = os.path.join(HERE, "build_worksheet_docx.py")
KEY_BUILDER = os.path.join(HERE, "build_worksheet_key_docx.py")
FBD = {"scene": "fbd", "forces": [{"label": "F_{N}", "dir": "up", "mag": 1},
                                  {"label": "F_{g}", "dir": "down", "mag": 1}]}
TIERS = ["warm-up", "warm-up", "practice", "challenge", "multi-topic"]


def item(tier, panels=1, captions=None, scene=FBD):
    q = {"tier": tier, "points": 1, "prompt": f"A {tier} object sits still. Draw its FBD.",
         "draw": {"panels": panels}, "solution": "FN up, Fg down.",
         "keyImage": copy.deepcopy(scene) if scene else None}
    if not scene:
        del q["keyImage"]
    if panels > 1:
        q["draw"]["captions"] = captions or [f"Obj {k + 1}" for k in range(panels)]
        q["keyImage"] = {"scene": "fbd", "panels": [
            dict(copy.deepcopy(FBD), caption=c) for c in q["draw"]["captions"]]}
        del q["keyImage"]["panels"][0]["scene"], q["keyImage"]["panels"][1]["scene"]
    return q


def grid_spec(**sec_extra):
    """A Chemistry spec (order-only ramp, equations allowed) set as a 3-across grid.
    Five items: four single squares and a two-square item, so 6 squares in 2 rows."""
    qs = [item(t) for t in TIERS[:4]] + [item("multi-topic", panels=2, captions=["Book", "Table"])]
    sec = {"code": "1.5", "title": "Grid test", "layout": "grid", "columns": 3,
           "squareIn": 2.05, "questions": qs,
           "equations": [{"note": "gravity", "plain": "Fg"}, {"note": "normal", "plain": "FN"},
                         {"note": "tension", "plain": "T"}]}
    sec.update(sec_extra)
    return {"course": "chemistry", "unit": 1, "sections": ["1.5"], "docType": "Practice_Set",
            "sectionsContent": [sec]}


def cards_spec(draw):
    sec = {"code": "1.5", "title": "Cards test",
           "questions": [dict(item(t, scene=None), draw=dict(draw)) for t in TIERS]}
    return {"course": "chemistry", "unit": 1, "sections": ["1.5"], "docType": "Practice_Set",
            "sectionsContent": [sec]}


def trheights(doc):
    return [(tr.find(qn("w:trPr")).find(qn("w:trHeight")).get(qn("w:val")),
             tr.find(qn("w:trPr")).find(qn("w:trHeight")).get(qn("w:hRule")))
            for tr in doc.element.body.iter(qn("w:tr"))
            if tr.find(qn("w:trPr")) is not None
            and tr.find(qn("w:trPr")).find(qn("w:trHeight")) is not None]


class Builder(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def build(self, s, builder=BUILDER):
        p = os.path.join(self.tmp, "s.json")
        with open(p, "w") as fh:
            json.dump(s, fh)
        out = os.path.join(self.tmp, "o.docx")
        r = subprocess.run([sys.executable, builder, p, out], capture_output=True, text=True,
                           env=dict(os.environ, PYTHONHASHSEED="0"))
        return r, (Document(out) if r.returncode == 0 else None)


class Grid(Builder):
    def test_grid_draws_one_exact_square_per_panel(self):
        r, doc = self.build(grid_spec())
        self.assertEqual(r.returncode, 0, r.stderr)
        squares = [h for h in trheights(doc) if h[1] == "exact"
                   and abs(int(h[0]) - 2.05 * 1440) <= 1]
        self.assertEqual(len(squares), 2)           # one square row per grid row
        body = doc.element.body.xml
        # 4 singles + 1 two-object item = 6 squares, each with a full ink border.
        self.assertEqual(body.count('<w:left w:val="single" w:sz="4"'), 6)

    def test_grid_columns_are_square_wide(self):
        r, doc = self.build(grid_spec())
        cols = [int(c.get(qn("w:w"))) for c in doc.element.body.iter(qn("w:gridCol"))]
        side, gutter = 2.05 * 1440, (7.5 - 3 * 2.05) / 2 * 1440
        self.assertEqual(sum(1 for c in cols if abs(c - side) <= 1), 3 * 2)   # 2 grid rows
        self.assertEqual(sum(1 for c in cols if abs(c - gutter) <= 1), 2 * 2)

    def test_grid_text_has_numbers_tiers_and_captions(self):
        r, doc = self.build(grid_spec())
        text = doc.element.body.xml
        for n in range(1, 6):
            self.assertIn(f">{n}.  <", text)
        self.assertIn(">MULTI-TOPIC<", text)
        self.assertIn(">Book<", text)
        self.assertIn(">Table<", text)
        self.assertNotIn("DRAW IT", text)            # no draw_block label in a grid

    def test_grid_refuses_work_areas_and_overwide_items(self):
        s = grid_spec(); s["sectionsContent"][0]["questions"][0]["parts"] = ["a. Name it."]
        r, _ = self.build(s)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("grid cell holds", r.stderr)
        s = grid_spec(columns=1, squareIn=2.0)
        r, _ = self.build(s)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("needs 2 squares", r.stderr)

    def test_grid_refuses_squares_too_big_for_the_page(self):
        r, _ = self.build(grid_spec(squareIn=2.45))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("gutter", r.stderr)

    def test_key_grid_draws_each_panel_and_a_note(self):
        s = grid_spec()
        for q in s["sectionsContent"][0]["questions"]:
            q["steps"] = [{"say": "No arrow for motion.", "ink": "arrow"}]
        r, doc = self.build(s, KEY_BUILDER)
        self.assertEqual(r.returncode, 0, r.stderr)
        pics = len(doc.element.body.xpath(".//pic:pic"))
        self.assertEqual(pics, 6 + 5)                 # 6 panel drawings + 5 notes

    def test_key_grid_unmodelled_scene_prints_typed_solution(self):
        s = grid_spec()
        s["sectionsContent"][0]["questions"][0]["keyImage"] = {"scene": "orbit"}
        s["sectionsContent"][0]["questions"][0]["solution"] = "Typed fallback."
        r, doc = self.build(s, KEY_BUILDER)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Typed fallback.", doc.element.body.xml)

    def test_key_grid_motion_arrow_refused(self):
        s = grid_spec()
        s["sectionsContent"][0]["questions"][0]["keyImage"]["forces"].append(
            {"label": "v", "dir": "right", "mag": 1})
        r, _ = self.build(s, KEY_BUILDER)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("motion", r.stderr)


class Spacing(Builder):
    @staticmethod
    def gaps(doc):
        """Exact-line gap paragraphs, in twentieths of a point, in document order."""
        out = []
        for sp in doc.element.body.iter(qn("w:spacing")):
            if sp.get(qn("w:lineRule")) == "exact" and sp.getparent().getparent().getparent() \
                    is doc.element.body:
                out.append(int(sp.get(qn("w:line"))))
        return out

    def test_compact_top_tightens_gaps_and_recall_padding(self):
        s = grid_spec(priorKnowledge={"items": ["One thing."]}, directions="Do it.")
        r, doc = self.build(s)
        r2, tight = self.build(dict(s, compactTop=True))
        self.assertEqual(r2.returncode, 0, r2.stderr)
        self.assertLess(sum(self.gaps(tight)), sum(self.gaps(doc)))
        self.assertIn('<w:top w:w="35"', tight.element.body.xml)
        self.assertNotIn('<w:top w:w="35"', doc.element.body.xml)

    def test_grid_row_gap_is_settable(self):
        r, doc = self.build(grid_spec(gridRowGapPt=4))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn(80, self.gaps(doc))                   # 4 pt between the two rows
        r, doc = self.build(grid_spec())
        self.assertIn(200, self.gaps(doc))                  # default 10 pt


class DrawBlockOptOuts(Builder):
    """Five questions, one single drawing panel each."""
    DRAW = {"panels": 1, "across": 1, "label": "DRAW"}

    @staticmethod
    def counts(doc):
        x = doc.element.body.xml
        return x.count("<w:t>1</w:t>"), x.count("<w:tr>") + x.count("<w:tr ")

    def test_default_keeps_number_and_caption_strip(self):
        r, doc = self.build(cards_spec(self.DRAW))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.numbers, self.rows = self.counts(doc)
        self.assertEqual(self.numbers, 5)                 # a "1" in each panel

    def test_numbered_false_drops_the_number(self):
        r, doc = self.build(cards_spec(dict(self.DRAW, numbered=False)))
        self.assertEqual(r.returncode, 0, r.stderr)
        _, base_rows = self.counts(self.build(cards_spec(self.DRAW))[1])
        numbers, rows = self.counts(doc)
        self.assertEqual(numbers, 0)
        self.assertEqual(rows, base_rows)                 # the strip stays

    def test_caption_strip_false_drops_the_strip(self):
        r, doc = self.build(cards_spec(dict(self.DRAW, captionStrip=False)))
        self.assertEqual(r.returncode, 0, r.stderr)
        _, base_rows = self.counts(self.build(cards_spec(self.DRAW))[1])
        numbers, rows = self.counts(doc)
        self.assertEqual(numbers, 5)                      # the number stays
        self.assertEqual(rows, base_rows - 5)             # one strip row per panel gone


class LabelBank(Builder):
    def test_inline_bank_runs_name_and_symbol_on_one_line(self):
        r, doc = self.build(grid_spec(equationStyle="inline", equationColumns=2))
        self.assertEqual(r.returncode, 0, r.stderr)
        # Name and symbol are two runs of ONE paragraph, not a name over a symbol.
        ts = [[t.text for t in p.iter(qn("w:t"))] for p in doc.element.body.iter(qn("w:p"))]
        self.assertIn(["GRAVITY   ", "Fg"], ts)
        self.assertNotIn(["gravity"], ts)               # the bar's name-over-symbol form

    def test_inline_bank_sets_marked_subscripts_as_subscript_runs(self):
        s = grid_spec(equationStyle="inline")
        s["sectionsContent"][0]["equations"] = [
            {"note": "gravity", "plain": "F_{g}"},
            {"note": "friction", "plain": "f    (f_{s} static, f_{k} kinetic)"}]
        r, doc = self.build(s)
        self.assertEqual(r.returncode, 0, r.stderr)
        runs = [(t.text, r_.find(qn("w:rPr")).find(qn("w:vertAlign")) is not None)
                for p in doc.element.body.iter(qn("w:p")) for r_ in p.iter(qn("w:r"))
                for t in r_.iter(qn("w:t"))]
        self.assertIn(("F", False), runs)
        self.assertIn(("g", True), runs)
        self.assertIn(("s", True), runs)
        self.assertIn((" static, f", False), runs)
        self.assertNotIn("_{", doc.element.body.xml)
        sub = [v.get(qn("w:val")) for v in doc.element.body.iter(qn("w:vertAlign"))]
        self.assertEqual(sub, ["subscript"] * 3)

    def test_plain_bar_leaves_underscore_markup_alone(self):
        s = grid_spec()
        s["sectionsContent"][0]["equations"] = [{"note": "gravity", "plain": "F_{g}"}]
        r, doc = self.build(s)
        self.assertIn("F_{g}", doc.element.body.xml)   # only the inline bank parses it

    def test_equation_columns_sets_bar_width(self):
        r, doc = self.build(grid_spec(equationColumns=3))
        self.assertEqual(r.returncode, 0, r.stderr)
        w = round(7.5 / 3 - 0.13, 2) * 1440
        cols = [int(c.get(qn("w:w"))) for c in doc.element.body.iter(qn("w:gridCol"))]
        self.assertEqual(sum(1 for c in cols if abs(c - w) <= 1), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
