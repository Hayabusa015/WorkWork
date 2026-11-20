"""Checks for build_worksheet_key_docx.py, including keyImage (SHULL-CHG-0071).

    python3 templates/worksheet/test_build_worksheet_key_docx.py
"""
import json, os, subprocess, sys, tempfile, unittest
from docx import Document

HERE = os.path.dirname(os.path.abspath(__file__))
BUILDER = os.path.join(HERE, "build_worksheet_key_docx.py")
FBD = {"scene": "fbd", "forces": [{"label": "F_{N}", "dir": "up", "mag": 1},
                                  {"label": "F_{g}", "dir": "down", "mag": 1}]}


def spec(questions):
    return {"course": "physics", "unit": 3, "sections": ["3.2"], "docType": "Practice_Set",
            "sectionsContent": [{"code": "3.2", "title": "Test", "questions": questions}]}


class KeyBuilder(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def build(self, s):
        p = os.path.join(self.tmp, "s.json")
        with open(p, "w") as fh:
            json.dump(s, fh)
        out = os.path.join(self.tmp, "k.docx")
        r = subprocess.run([sys.executable, BUILDER, p, out], capture_output=True, text=True)
        return r, (Document(out) if r.returncode == 0 else None)

    @staticmethod
    def answer_cells(doc):
        # The masthead is table 0; each answer is a one-cell table after it.
        return [t.rows[0].cells[0] for t in doc.tables[1:]]

    @staticmethod
    def pictures(cell):
        return len(cell._tc.xpath(".//pic:pic"))

    def test_key_image_gets_exactly_one_picture(self):
        r, doc = self.build(spec([{"prompt": "Draw it.", "solution": "FN up, Fg down.",
                                   "keyImage": FBD}]))
        self.assertEqual(r.returncode, 0, r.stderr)
        cells = self.answer_cells(doc)
        self.assertEqual(len(cells), 1)
        self.assertEqual(self.pictures(cells[0]), 1)
        self.assertNotIn("FN up, Fg down.", cells[0].text)   # drawn, so no typed copy

    def test_key_image_with_steps_is_still_one_picture(self):
        r, doc = self.build(spec([{"prompt": "Draw it.", "solution": "x", "keyImage": FBD,
                                   "steps": [{"say": "No motion arrow.", "ink": "arrow"}]}]))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.pictures(self.answer_cells(doc)[0]), 1)

    def test_side_layout_sets_drawing_beside_steps(self):
        """"keyLayout": "side" (opt-in): an item with keyImage and steps becomes a two-column
        row, drawing left and steps right, both pictures with zero wrap distances so
        LibreOffice does not inset and clip them. Items without both keep their old shape."""
        both = {"prompt": "Draw it.", "solution": "x", "keyImage": FBD,
                "steps": [{"answer": ["F_{N} ="], "value": "9.8 N up"}]}
        only_img = {"prompt": "Draw it.", "solution": "y", "keyImage": FBD}
        only_steps = {"prompt": "Solve.", "solution": "z", "steps": [{"answer": ["x ="], "value": "1"}]}
        s = spec([both, only_img, only_steps])
        s["keyLayout"], s["keyFbdIn"], s["keyStepScale"] = "side", 2.4, 0.85
        r, doc = self.build(s)
        self.assertEqual(r.returncode, 0, r.stderr)
        c1, c2, c3 = self.answer_cells(doc)
        self.assertEqual(self.pictures(c1), 2)
        inner = c1._tc.xpath(".//w:tbl")
        self.assertEqual(len(inner), 1)
        self.assertEqual(len(inner[0].xpath("./w:tr/w:tc")), 3)          # drawing, gutter, steps
        ext = [int(e.get("cx")) / 914400 for e in c1._tc.xpath(".//wp:extent")]
        self.assertLessEqual(ext[0], 2.4 + 1e-6)                          # drawing fits its column
        self.assertAlmostEqual(ext[1], 7.2 - 2.4 - 0.12, places=3)        # steps fill the rest
        for il in c1._tc.xpath(".//wp:inline"):
            self.assertEqual([il.get(k) for k in ("distT", "distB", "distL", "distR")], ["0"] * 4)
        self.assertEqual(self.pictures(c2), 1)                            # unchanged shapes
        self.assertEqual(self.pictures(c3), 1)
        self.assertEqual(c2._tc.xpath(".//w:tbl"), [])
        # the default (no keyLayout) keeps the stacked single picture
        r, doc = self.build(spec([both]))
        self.assertEqual(self.pictures(self.answer_cells(doc)[0]), 1)

    def test_side_layout_unmodelled_scene_falls_back_to_typed_solution(self):
        q = {"prompt": "Draw it.", "solution": "Typed fallback.", "steps": [{"say": "s"}],
             "keyImage": {"scene": "fbd", "panels": [{"forces": []}]}}
        s = spec([q]); s["keyLayout"] = "side"
        r, doc = self.build(s)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Typed fallback.", self.answer_cells(doc)[0].text)

    def test_steps_behave_as_before(self):
        r, doc = self.build(spec([{"prompt": "Solve.", "solution": "x",
                                   "steps": [{"answer": ["x ="], "value": "1"}]}]))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(self.pictures(self.answer_cells(doc)[0]), 1)

    def test_neither_keeps_typed_solution_and_answer_line(self):
        r, doc = self.build(spec([{"prompt": "Solve.", "solution": "Two steps.",
                                   "finalAnswer": "4 m"}]))
        self.assertEqual(r.returncode, 0, r.stderr)
        c = self.answer_cells(doc)[0]
        self.assertEqual(self.pictures(c), 0)
        self.assertIn("Two steps.", c.text)
        self.assertIn("ANSWER:  4 m", c.text)

    def test_key_image_without_solution_refused(self):
        r, _ = self.build(spec([{"prompt": "Draw it.", "keyImage": FBD}]))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("solution", r.stderr)

    def test_unmodelled_scene_falls_back_to_typed_solution(self):
        r, doc = self.build(spec([{"prompt": "Draw it.", "solution": "Typed fallback.",
                                   "keyImage": {"scene": "orbit"}}]))
        self.assertEqual(r.returncode, 0, r.stderr)
        c = self.answer_cells(doc)[0]
        self.assertEqual(self.pictures(c), 0)
        self.assertIn("Typed fallback.", c.text)
        self.assertIn("printing the typed solution instead", r.stderr)

    def test_motion_arrow_refuses_the_build(self):
        bad = {"scene": "fbd", "forces": FBD["forces"] + [{"label": "v", "dir": "right", "mag": 1}]}
        r, _ = self.build(spec([{"prompt": "Draw it.", "solution": "x", "keyImage": bad}]))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("motion", r.stderr)

    def test_existing_committed_spec_still_builds(self):
        out = os.path.join(self.tmp, "existing.docx")
        r = subprocess.run([sys.executable, BUILDER,
                            os.path.join(HERE, "specs", "phys_u01_s01.2_10q.json"), out],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(os.path.exists(out))


if __name__ == "__main__":
    unittest.main(verbosity=2)
