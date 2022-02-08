import unittest
from interview.practice.code.recursion.ProductSum import product_sum


class TestProductSum(unittest.TestCase):
    def test_product_sum(self):
        self.assertEqual(96, product_sum([2, 4, [4, 5, 3, [6, 5] ] ]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
