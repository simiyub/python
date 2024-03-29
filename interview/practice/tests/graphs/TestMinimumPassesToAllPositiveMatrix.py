import unittest
from interview.practice.code.graphs.MinimumPassesToAllPositiveMatrix import minimum_passes


class MyTestCase(unittest.TestCase):
    def test_minimum_passes1(self):
        matrix = [[0, -2, -1], [-5, 2, 0], [-6, -2, 0]]
        self.assertEqual(3, minimum_passes(matrix))

    def test_minimum_passes2(self):
        matrix = [
    [-1, 0, 3],
    [0, -5, -6]
  ]
        self.assertEqual(-1, minimum_passes(matrix))


if __name__ == '__main__':
    unittest.main()
