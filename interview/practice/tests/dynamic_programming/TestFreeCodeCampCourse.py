from interview.practice.code.dynamic_programming.FreeCodeCampCourse import *
import unittest


class TestFreeCodeCampCourse (unittest.TestCase):

    def test_fib_recursive(self):
        self.assertEqual(13, fib_recursive(7))  # add assertion here

    def test_fib_memoization(self):
        self.assertEqual(12586269025, fib_memoization(50))  #

    def test_grid_traversal(self):
        self.assertEqual(1, traverse_grid(1, 1))
        self.assertEqual(3, traverse_grid(2, 3))
        self.assertEqual(3, traverse_grid(3, 2))
        self.assertEqual(6, traverse_grid(3, 3))
        self.assertEqual(2333606220, traverse_grid(18, 18))

    def test_can_sum(self):
        self.assertTrue(can_sum(7, [2, 3, 4, 7]))
        self.assertTrue(can_sum(7, [2, 3]))
        self.assertFalse(can_sum(7, [2, 4]))
        self.assertTrue(can_sum(8, [2, 3, 5]))
        self.assertFalse(can_sum(300, [7, 14]))

    def test_how_sum(self):
        self.assertIn(how_sum(7, [2, 3, 4, 7]), [[7], [3, 4], [3, 2, 2]])
        self.assertIsNone(how_sum(7, [2, 4]))
        self.assertIsNone(how_sum(300, [7, 14]))
        self.assertIsNotNone(how_sum(700, [7, 14]))
        self.assertEqual([70, 70], how_sum(140, [70, 2]))

    def test_best_sum(self):
        self.assertEqual([7], best_sum(7, [5, 3, 4, 7]))
        self.assertIsNotNone(best_sum(8, [2, 3, 5]))
        self.assertEqual([4, 4], best_sum(8, [1, 4, 5]))
        self.assertEqual([25, 25, 25, 25], best_sum(100, [1, 2, 5, 25]))

    def test_can_construct(self):
        self.assertTrue(can_construct('abcdef', ['ab', 'abc', 'cd', 'def',  'abcd']))
        self.assertFalse(can_construct('skateboard', ['bo, rd', 'ate', 't', 'ska', 'sk', 'boar']))
        self.assertTrue(can_construct('', ['cat', 'dog', 'mouse']))
        self.assertFalse(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                                       ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee']))

    def test_count_construct(self):
        self.assertEqual(2, count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
        self.assertEqual(4, count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
        self.assertEqual(0, count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                                       ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee']))

    def test_all_construct(self):
        self.assertEqual(len([['purp', 'le'], ['p', 'ur', 'p', 'le']]),
                         len(all_constructs('purple', ['purp', 'p', 'ur', 'le', 'purpl'])))
        self.assertEqual( len([['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]),
                          len(all_constructs('abcdef', ['ab', 'abc', 'cd', 'def',  'abcd', 'ef', 'c'])))

        self.assertEqual(0, len(all_constructs('aaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'])))
if __name__ == '__main__':
    unittest.main()
