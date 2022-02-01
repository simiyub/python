import unittest

from interview.medium.code.bst.BST import BST
from interview.medium.code.bst.KthLargestValueInBST import find_kth_largest_value


class TestKthLargestValueInBST(unittest.TestCase):
    def test_find_kth_largest_value(self):
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
        self.assertEqual(17, find_kth_largest_value(tree, 3))  # add assertion here


if __name__ == '__main__':
    unittest.main()
