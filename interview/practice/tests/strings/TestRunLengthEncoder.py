import unittest
from interview.practice.code.strings.RunLengthEncoder import encode


class TestRunLengthEncoder(unittest.TestCase):
    def test_encode(self):
        expected = '9Z6Z4C3M'
        string = 'ZZZZZZZZZZZZZZZCCCCMMM'
        actual = encode(string)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
