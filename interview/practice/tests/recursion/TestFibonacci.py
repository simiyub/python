import unittest
from interview.practice.code.recursion.Fibonacci import get


class TestFibonacci(unittest.TestCase):
    def test_get(self):
        self.assertEqual(13, get(8))


if __name__ == '__main__':
    unittest.main()
