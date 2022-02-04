import unittest
from interview.practice.code.graphs.BreadthFirstSearch import search
from interview.practice.tests.Mixin import example_node


class TestBreadthFirstSearch(unittest.TestCase):
    def test_search(self):
        expected = [10, 5, 15, 2, 5, 13, 22, 1, 14]
        self.assertEqual(expected, search(example_node(), []))  # add assertion here


if __name__ == '__main__':
    unittest.main()
