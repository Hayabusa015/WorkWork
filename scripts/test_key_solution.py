"""Checks for the key-image scenes in key_solution.py (SHULL-CHG-0071).

    python3 scripts/test_key_solution.py
"""
import os, sys, tempfile, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
import key_solution as ks
from key_ink import Page

FBD = {"scene": "fbd", "forces": [
    {"label": "F_{N}", "dir": "up", "mag": 1.0},
    {"label": "F_{g}", "dir": "down", "mag": 1.0},
    {"label": "F_{app}", "dir": "right", "mag": 0.6}]}


class FbdScene(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def test_one_arrow_and_one_label_per_force(self):
        P = Page(1080, 1200)
        ks.fbd_scene(P, 10, 8, 1060, FBD)
        self.assertEqual(P.arrows_drawn, 3)
        self.assertEqual(P.labels_drawn, ["F_{N}", "F_{g}", "F_{app}"])

    def test_panels_share_one_scale_and_count_every_force(self):
        sc = {"scene": "fbd", "panels": [
            {"caption": "Block", "forces": [{"label": "T", "dir": "right", "mag": 0.4},
                                            {"label": "F_{g}", "dir": "down", "mag": 1}]},
            {"caption": "Weight", "forces": [{"label": "T", "dir": "up", "mag": 0.4}]}]}
        P = Page(1080, 1200)
        ks.fbd_scene(P, 10, 8, 1060, sc)
        self.assertEqual(P.arrows_drawn, 3)
        self.assertEqual(P.labels_drawn, ["T", "F_{g}", "T"])

    def test_motion_arrow_refused(self):
        for bad in ({"label": "v", "dir": "right", "mag": 1},
                    {"label": "motion", "dir": "right", "mag": 1},
                    {"label": "F_{x}", "name": "velocity", "dir": "right", "mag": 1},
                    {"label": "a", "dir": "down", "mag": 1}):
            sc = {"scene": "fbd", "forces": FBD["forces"] + [bad]}
            with self.assertRaises(ks.MotionArrowError, msg=str(bad)):
                ks.solution_image({"prompt": "p", "keyImage": sc}, os.path.join(self.tmp, "m.png"))

    def test_force_names_that_are_not_motion_pass(self):
        sc = {"scene": "fbd", "forces": [{"label": "F_{app}", "dir": "right", "mag": 1},
                                         {"label": "drag", "dir": "up", "mag": 1},
                                         {"label": "f_{k}", "dir": "left", "mag": 1}]}
        ks.fbd_forces(sc)

    def test_scene_without_steps_renders(self):
        png, h = ks.solution_image({"prompt": "p", "keyImage": FBD}, os.path.join(self.tmp, "a.png"))
        self.assertTrue(os.path.exists(png))
        self.assertGreater(h, 1.0)
        self.assertLess(h, 3.5)
        im = Image.open(png).convert("L")
        self.assertLess(im.getextrema()[0], 200)       # something was drawn

    def test_unmodelled_items_raise_scene_unsupported(self):
        for sc in ({"scene": "orbit"},
                   {"scene": "fbd", "forces": []},
                   {"scene": "fbd", "forces": [{"label": "T", "dir": "sideways", "mag": 1}]},
                   {"scene": "fbd", "forces": [{"label": "T", "dir": "up", "mag": 0}]},
                   {"scene": "fbd", "object": "sphere", "forces": [{"label": "T", "dir": "up", "mag": 1}]}):
            with self.assertRaises(ks.SceneUnsupported, msg=str(sc)):
                ks.solution_image({"prompt": "p", "keyImage": sc}, os.path.join(self.tmp, "u.png"))

    def test_linear_sketch_with_steps_still_renders(self):
        q = {"prompt": "p", "sketch": {"scene": "linear", "find": "a",
                                       "lanes": [{"name": "cart", "v0": "0", "v": "6 m/s", "a": "?"}],
                                       "t": "3 s"},
             "steps": [{"row": ["a =", {"frac": ["v − v_{0}", "t"]}]}, {"answer": ["a ="], "value": "2 m/s^{2}"}]}
        png, h = ks.solution_image(q, os.path.join(self.tmp, "l.png"))
        self.assertTrue(os.path.exists(png))
        self.assertGreater(h, 1.0)

    def test_steps_only_still_renders(self):
        png, _ = ks.solution_image({"prompt": "p", "steps": [{"say": "Yes."}]},
                                   os.path.join(self.tmp, "s.png"))
        self.assertTrue(os.path.exists(png))


if __name__ == "__main__":
    unittest.main(verbosity=2)
