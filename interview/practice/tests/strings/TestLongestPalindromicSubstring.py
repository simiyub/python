import unittest
from interview.practice.code.strings.LongestPalindromicSubstring import longest_palindromic_substring


class TestLongestPalindromicString(unittest.TestCase):
    def test_longest_palindromic_string(self):
        self.assertEqual('everreve', longest_palindromic_substring('barabbaeverrevebarbara'))  # add assertion here


if __name__ == '__main__':
    unittest.main()
