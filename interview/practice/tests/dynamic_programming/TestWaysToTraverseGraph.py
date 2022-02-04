import unittest
from interview.practice.code.dynamic_programming.WaysToTraverseGraph import ways_to_traverse_graph


class TestWaysToTraverseGraph(unittest.TestCase):
    def test_ways_traverse_graph(self):
        expected = 10
        width = 4
        height = 3
        self.assertEqual(expected, ways_to_traverse_graph(width, height))  # add assertion here


if __name__ == '__main__':
    unittest.main()
