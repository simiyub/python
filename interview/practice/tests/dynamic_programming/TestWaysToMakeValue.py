import unittest
from interview.practice.code.dynamic_programming.WaysToMakeChange import ways_to_make_value


class TestWaysToMakeValue(unittest.TestCase):
    def test_ways_to_make_change(self):
        self.assertEqual(2, ways_to_make_value([1, 5], 6))  # add assertion here


if __name__ == '__main__':
    unittest.main()
