import unittest
from interview.practice.code.strings.ReverseWordsInString import reverse1, reverse2


class TestReverseWordsInString(unittest.TestCase):
    def test_reverse1(self):
        expected = 'boy every'
        string = 'every boy'
        self.assertEqual(expected, reverse1(string))

    def test_reverse2(self):
        expected = 'for accounted are  children   all'
        string = 'all   children  are accounted for'
        self.assertEqual(expected, reverse2(string))


if __name__ == '__main__':
    unittest.main()
