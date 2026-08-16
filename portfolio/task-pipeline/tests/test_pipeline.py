import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parents[1]))
from pipeline import run

class PipelineTests(unittest.TestCase):
    def test_order_is_preserved(self):
        self.assertEqual(run([-2, 0, 3, 5], workers=3), [4, 0, 9, 25])
    def test_empty_input(self):
        self.assertEqual(run([], workers=2), [])
    def test_invalid_configuration(self):
        with self.assertRaises(ValueError): run([1], workers=0)

if __name__ == "__main__": unittest.main()
