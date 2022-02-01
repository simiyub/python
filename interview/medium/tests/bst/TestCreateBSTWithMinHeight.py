import unittest

from interview.medium.code.bst.CreateBSTWithMinHeight import min_height_bst


class TestCreateBSTWithMinHeight(unittest.TestCase):
    def test_min_height_bst(self):
        bst = min_height_bst([1, 2, 5, 7, 10, 13, 14, 15, 22])
        self.assertEqual(2, bst.left.value)
        self.assertEqual(14, bst.right.value)


if __name__ == '__main__':
    unittest.main()
