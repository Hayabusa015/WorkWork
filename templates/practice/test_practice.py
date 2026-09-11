"""Regression checks for the course-specific worksheet boundaries."""
import copy
import json
from pathlib import Path
import unittest
from build_practice import validate_spec

ROOT = Path(__file__).parent

class PracticeBoundaries(unittest.TestCase):
    def spec(self, course):
        return json.loads((ROOT / 'specs' / (course + '.json')).read_text(encoding='utf-8'))

    def test_supplied_specs_valid(self):
        for course in ('chemistry', 'physics', 'geology'):
            validate_spec(self.spec(course))

    def test_nonexistent_section_refused(self):
        spec = self.spec('physics'); spec['section'] = '4.9'
        with self.assertRaisesRegex(ValueError, 'section'):
            validate_spec(spec)

    def test_physics_answer_space_refused(self):
        spec = self.spec('physics'); spec['questions'][0]['work_height'] = 1
        with self.assertRaisesRegex(ValueError, 'notebook'):
            validate_spec(spec)

    def test_chemistry_math_without_box_refused(self):
        spec = self.spec('chemistry')
        next(q for q in spec['questions'] if q.get('calculation'))['work_height'] = 0
        with self.assertRaisesRegex(ValueError, 'work box'):
            validate_spec(spec)

    def test_geology_math_refused(self):
        spec = self.spec('geology'); spec['equations'] = [{'plain': 'x = 1'}]
        with self.assertRaisesRegex(ValueError, 'math'):
            validate_spec(spec)

    def test_missing_key_refused(self):
        spec = self.spec('physics'); spec['questions'][0]['answer'] = ''
        with self.assertRaisesRegex(ValueError, 'answer'):
            validate_spec(spec)

    def test_unknown_component_refused(self):
        spec = self.spec('chemistry'); spec['questions'][0]['figure'] = 'unknown'
        with self.assertRaisesRegex(ValueError, 'figure'):
            validate_spec(spec)

if __name__ == '__main__':
    unittest.main()
