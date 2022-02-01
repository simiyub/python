import unittest
from interview.medium.code.bst import CreateBST

"""
unit test for CreateBST
"""


class TestCreateBST(unittest.TestCase):
    def test_create_bst(self):
        five = 5
        bst = CreateBST.CreateBST(1)
        self.assertTrue(bst.insert(five).contains(five))  # add assertion here


if __name__ == '__main__':
    unittest.main()
