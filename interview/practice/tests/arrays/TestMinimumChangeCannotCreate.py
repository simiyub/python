import unittest
from interview.practice.code.arrays.MinimumChangeCannotCreate import minimum_change_cannot_create


class TestMinimumChangeCannotCreate(unittest.TestCase):
    def test_minimum_change_cannot_create(self):
        self.assertEqual(20, minimum_change_cannot_create([5, 7, 1, 1, 2, 3, 22]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
