import unittest
from interview.practice.code.arrays.SortedSquareFromSortedArray import sorted_square_array

class TestSortedSquareArrayFromSortedArray(unittest.TestCase):
    def test_sorted_square_array1(self):
        self.assertEqual([1, 4, 9], sorted_square_array([1, 2, 3]) )
    def test_sorted_square_array2(self):
        self.assertEqual([9, 25, 81], sorted_square_array([3, 5, 9]) )

    def test_sorted_square_array3(self):
        self.assertEqual([1, 4], sorted_square_array([-2, -1]) )

if __name__ == '__main__':
    unittest.main()
