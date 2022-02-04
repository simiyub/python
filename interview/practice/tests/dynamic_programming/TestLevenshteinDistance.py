import unittest
from interview.practice.code.dynamic_programming.LevenshteinDistance import minimum_edits_to_match

class TestLevenshteinDistance(unittest.TestCase):
    def test_minimum_edits_to_match(self):
        self.assertEqual(2,minimum_edits_to_match("abc", "yabd"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
