import unittest
from interview.practice.code.strings.MinimumCharactersToFormWords import minimum_characters

class TestMinimumCharactersToFormWords(unittest.TestCase):
    def test_minimum_characters(self):
        words = ['words', 'have', 'meaning?']
        expected = 'w o r d s h a a v e e m n n i g'
        self.assertEqual(expected,minimum_characters(words))


if __name__ == '__main__':
    unittest.main()
