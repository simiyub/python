import unittest

from interview.practice.code.bst import FindClosestValueInBST


class FindClosestValueInBSTTestCase(unittest.TestCase):
    def test_something(self):

        ten = FindClosestValueInBST.BST(10)

        one = FindClosestValueInBST.BST(1)
        two = FindClosestValueInBST.BST(2)
        two.left = one
        five2 = FindClosestValueInBST.BST(5)
        five1 = FindClosestValueInBST.BST(5)
        five1.left = two
        five1.right = five2



        ten.left = five1
        fourteen = FindClosestValueInBST.BST(14)
        thirteen = FindClosestValueInBST.BST(13)
        thirteen.right = fourteen
        twenty_two = FindClosestValueInBST.BST(22)
        fifteen = FindClosestValueInBST.BST(15)
        fifteen.left = thirteen
        fifteen.right = twenty_two
        ten.right = fifteen

        bst = ten

        expected = 13

        self.assertEqual(expected, FindClosestValueInBST.find_closest_value_in_bst(bst, 12))  # add assertion here


if __name__ == '__main__':
    unittest.main()
