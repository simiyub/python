import unittest
from interview.practice.code.recursion.Permutations import permutations


class TestPermutations(unittest.TestCase):
    def test_something(self):
        self.assertEqual(6, len(permutations([1, 2, 3])))


if __name__ == '__main__':
    unittest.main()
