import unittest
from interview.practice.code.graphs.SingleCycleCheck import has_single_cycle

class TestSingleCycleCheck(unittest.TestCase):
    def test_something(self):
        self.assertTrue(has_single_cycle([2, 3, 1, -4, -4, 2]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
