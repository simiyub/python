import unittest

from interview.medium.tests.Mixin import example_bst
from interview.medium.code.bst.BSTTraversal import traverse_in_order, traverse_pre_order, traverse_post_order


class TestBSTTraversal(unittest.TestCase):
    def test_traverse_in_order(self):
        expected_in_order = [1, 2, 5, 5, 10, 13, 14, 15, 22]
        self.assertEqual(expected_in_order, traverse_in_order(example_bst(), []))

    def test_traverse_pre_order(self):
        expected_pre_order = [10, 5, 2, 1, 5, 15, 13, 14, 22]
        self.assertEqual(expected_pre_order, traverse_pre_order(example_bst(), []))

    def test_traverse_post_order(self):
        expected_post_order = [1, 2, 5, 5, 14, 13, 22, 15, 10]
        self.assertEqual(expected_post_order, traverse_post_order(example_bst(), []))


if __name__ == '__main__':
    unittest.main()
