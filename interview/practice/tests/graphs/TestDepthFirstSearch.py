import unittest

from interview.practice.tests.Mixin import example_node
from interview.practice.code.graphs.DepthFirstSearch import search


class TestDepthFirstSearch(unittest.TestCase):
    def test_search(self):

        expected = [10, 5, 2, 1, 5, 15, 13, 14, 22]
        graph = example_node()
        self.assertEqual(expected, search(graph))  # add assertion here


if __name__ == '__main__':
    unittest.main()
