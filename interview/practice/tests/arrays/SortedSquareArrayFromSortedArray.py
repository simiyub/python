import unittest
from interview.practice.code.arrays.SortedSquareFromSortedArray import sorted_square_array

class SortedSquareArrayFromSortedArray(unittest.TestCase):
    def test_sorted_square_array(self):
        self.assertEqual([1, 4, 9], sorted_square_array([1, 2, 3]) )
    def test_sorted_square_array(self):
        self.assertEqual([9, 25, 81], sorted_square_array([3, 5, 9]) )

if __name__ == '__main__':
    unittest.main()
