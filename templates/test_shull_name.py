"""Pins templates/_shull_name.py to the worked examples in standards/NAMING.md §2.
Run: python3 -m unittest templates/test_shull_name.py"""
import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _shull_name import document_name, reference_titles


class NamingExamples(unittest.TestCase):
    def test_section_and_unit_level(self):
        self.assertEqual(document_name("Guided_Notes", ["1.1", "1.2"], 1, unit_title="Matter & Atoms"),
                         "Unit 1 Guided Notes - Matter & Atoms.docx")
        self.assertEqual(document_name("Lab", ["1.3"], 1, topic="Motion Graphs", ext="pdf"),
                         "1.3 Lab - Motion Graphs.pdf")
        self.assertEqual(document_name("Lab", ["1.3"], 1, topic="Motion Graphs", key=True, ext="pdf"),
                         "1.3 Lab Key - Motion Graphs.pdf")
        self.assertEqual(document_name("Practice_Set", ["2.3"], 2, topic="Electron Configs",
                                       descriptor="Longhand"),
                         "2.3 Practice Set - Electron Configs Longhand.docx")
        self.assertEqual(document_name("Slides", ["1.4"], 1, topic="Isotopes", ext="pptx"),
                         "1.4 Slides - Isotopes.pptx")
        self.assertEqual(document_name("Test", ["1.1", "1.2"], 1, unit_title="Matter & Atoms", version="B"),
                         "Unit 1 Test B - Matter & Atoms.docx")
        self.assertEqual(document_name("Lab", ["1.3"], 1, ext="pdf"), "1.3 Lab.pdf")

    def test_course_level_reference(self):
        for topic in ("Polyatomic Ions", "Multi-Charge Metals", "Full Packet"):
            self.assertEqual(document_name("Reference", [], None, topic=topic, scope="course"),
                             f"Reference - {topic}.pdf")
        with self.assertRaisesRegex(ValueError, "Reference only"):
            document_name("Organizer", [], None, topic="Naming", scope="course")
        with self.assertRaisesRegex(ValueError, "always has a topic"):
            document_name("Reference", [], None, scope="course")
        with self.assertRaisesRegex(ValueError, "limit is 20"):
            document_name("Reference", [], None, topic="Metals with Multiple Charges", scope="course")

    def test_topic_limit(self):
        with self.assertRaisesRegex(ValueError, "limit is 20"):
            document_name("Lab", ["1.3"], 1, topic="Position-Velocity-Acceleration Graphing")

    def test_reference_titles_reads_ref_rows(self):
        self.assertIsInstance(reference_titles("chemistry"), list)
        self.assertEqual(reference_titles("no-such-course"), [])


if __name__ == "__main__":
    unittest.main()
