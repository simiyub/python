import unittest
from interview.practice.code.arrays.SumOfTwoNumbersWithSort import find_sum as find_sum_with_sort
from interview.practice.code.arrays.SumOfTwoNumbersWithStorage import find_sum as find_sum_with_storage


class TestSumOfTwoNumbers(unittest.TestCase):
    def test_find_sum_with_sort(self):
        self.assertEqual([-1, 11], find_sum_with_sort([3, 5, -4, 8, 11, 1, -1, 6], 10))

    def test_find_sum_with_storage(self):
        self.assertEqual([-1, 11], find_sum_with_storage([3, 5, -4, 8, 11, 1, -1, 6], 10))  #


if __name__ == '__main__':
    unittest.main()
