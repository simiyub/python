from interview.practice.code.dynamic_programming.FreeCodeCampCourse import *
import unittest



class TestFreeCodeCampCourse (unittest.TestCase):

    def test_fib_recursive(self):
        self.assertEqual(13, fib_recursive(7))  # add assertion here

    def test_fib_memoization(self):
        self.assertEqual(12586269025, fib_memoization(50))  #

    def test_grid_traversal(self):
        self.assertEqual(1, traverse_grid(1,1))
        self.assertEqual(3, traverse_grid(2,3))
        self.assertEqual(3, traverse_grid(3,2))
        self.assertEqual(6, traverse_grid(3,3))
        self.assertEqual(2333606220, traverse_grid(18,18))

    def test_can_sum(self):
        self.assertTrue(can_sum(7,[2, 3, 4, 7]))
        self.assertTrue(can_sum(7, [2, 3]))
        self.assertFalse(can_sum(7, [2, 4]))
        self.assertTrue(can_sum(8, [2, 3, 5]))
        self.assertFalse(can_sum(300,[7, 14]))

if __name__ == '__main__':
    unittest.main()
