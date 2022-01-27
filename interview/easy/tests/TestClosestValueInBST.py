import unittest

from interview.easy.code import ClosestValueInBST


class ClosestValueInBSTTestCase(unittest.TestCase):
    def test_something(self):

        ten = ClosestValueInBST.BST(10)

        one = ClosestValueInBST.BST(1)
        two = ClosestValueInBST.BST(2)
        two.left = one
        five2 = ClosestValueInBST.BST(5)
        five1 = ClosestValueInBST.BST(5)
        five1.left = two
        five1.right = five2



        ten.left = five1
        fourteen = ClosestValueInBST.BST(14)
        thirteen = ClosestValueInBST.BST(13)
        thirteen.right = fourteen
        twenty_two = ClosestValueInBST.BST(22)
        fifteen = ClosestValueInBST.BST(15)
        fifteen.left = thirteen
        fifteen.right = twenty_two
        ten.right = fifteen

        bst = ten

        expected = 13

        self.assertEqual(expected, ClosestValueInBST.find_closest_value_in_bst(bst, 12))  # add assertion here


if __name__ == '__main__':
    unittest.main()
