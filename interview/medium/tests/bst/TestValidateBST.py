import unittest

from interview.medium.code.bst.ValidateBST import validate_bst
from interview.medium.tests.Mixin import example_bst


class TestValidateBST(unittest.TestCase):
    def test_validate_bst(self):

        self.assertTrue(validate_bst(example_bst()))  # add assertion here


if __name__ == '__main__':
    unittest.main()
