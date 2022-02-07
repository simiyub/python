import unittest
from interview.practice.code.graphs.RiverSizes import sizes


class TestRiverSizes(unittest.TestCase):
    def test_sizes(self):
        array = [[1, 0, 0, 1, 0],
                 [1, 0, 1, 0, 0],
                 [0, 0, 1, 0, 1],
                 [1, 0, 1, 0, 1],
                 [1, 0, 1, 1, 0]]
        self.assertTrue(sizes(array).count(2) == 3)  # add assertion here


if __name__ == '__main__':
    unittest.main()
