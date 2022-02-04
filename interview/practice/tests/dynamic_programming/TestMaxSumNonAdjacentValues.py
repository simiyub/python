import unittest
from interview.practice.code.dynamic_programming.MaxSumNonAdjacentValues import greatest_sum


class TestMaxSumNonAdjacentValues(unittest.TestCase):
    def test_sum1(self):
        array = [75, 105, 120, 75, 90, 135]
        self.assertEqual(330, greatest_sum(array))

    def test_sum2(self):
        array = [1]
        self.assertEqual(1, greatest_sum(array))  #


if __name__ == '__main__':
    unittest.main()
