import unittest
from interview.easy.code.strings.PalindromeCheck import is_palindrome


class TestPalindromeCheck(unittest.TestCase):
    def test_is_palindrome1(self):
        string = "string"
        self.assertFalse(is_palindrome(string))  # a

    def test_is_palindrome2(self):
        string = "oooo"
        self.assertTrue(is_palindrome(string))  #
        # dd assertion here


if __name__ == '__main__':
    unittest.main()
