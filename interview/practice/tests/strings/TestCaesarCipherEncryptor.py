import unittest
from interview.practice.code.strings.CaesarCipherEncryptor import encrypt



class TestCaesarCipherEncryptor(unittest.TestCase):
    def test_encrypt2(self):
        expected = "pqr"
        shift_key = 3
        actual = encrypt("mno",shift_key )
        self.assertEqual(expected, actual)  # add assertion here



if __name__ == '__main__':
    unittest.main()
