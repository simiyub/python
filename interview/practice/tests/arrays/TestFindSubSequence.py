import unittest
from interview.practice.code.arrays.FindSubSequence import is_subsequence


class TestValidateSubSequence(unittest.TestCase):

    def test_validate_subsequence1(self):
        self.assertTrue(is_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))

    def test_validate_subsequence2(self):
        self.assertTrue(is_subsequence([1, 1, 1, 1, 1], [1, 1, 1]))

    def test_validate_subsequence3(self):
        self.assertTrue(is_subsequence([1, 2, 3, 4, 5, 3, 4, 5, 6], [3, 4, 5, 6]))


if __name__ == '__main__':
    unittest.main()

