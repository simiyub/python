import unittest
from interview.practice.code.dynamic_programming.MinimumCoinsForChange import coins_for_change


class TestMinimumCoinsForChange(unittest.TestCase):
    def test_coins_for_change(self):
        self.assertEqual(3,coins_for_change(7, [1, 5, 10]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
