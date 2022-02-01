import unittest

from interview.medium.code.bst.BST import BST
from interview.medium.code.bst.KthValueInBST import find_kth_largest_value, find_kth_smallest_value


class TestKthLargestValueInBST(unittest.TestCase):

    def setUp(self):
        two = BST(2)
        two.left = BST(1)
        two.right = BST(3)
        five = BST(5)
        five.left =two
        five.right = BST(5)
        twenty = BST(20)
        twenty.left = BST(17)
        twenty.right = BST(22)
        tree = BST(15)
        tree.left = five
        tree.right = twenty
        self.tree = tree
    def test_find_kth_largest_value(self):

        self.assertEqual(17, find_kth_largest_value(self.tree, 3))

    def test_find_kth_smallest_value(self):
        self.assertEqual(15, find_kth_smallest_value(self.tree, 6))
            # add assertion here


if __name__ == '__main__':
    unittest.main()
