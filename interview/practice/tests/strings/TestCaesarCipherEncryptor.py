import unittest
from interview.practice.code.strings.CaesarCipherEncryptor import encrypt



class TestCaesarCipherEncryptor(unittest.TestCase):
    def test_encrypt1(self):
        expected = "pqr"
        shift_key = 3
        actual = encrypt("mno",shift_key )
        self.assertEqual(expected, actual)  # add assertion here

    def test_encrypt2(self):
        expected = "abc"
        shift_key = 3
        actual = encrypt("xyz",shift_key )
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
