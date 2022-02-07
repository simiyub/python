import unittest
from interview.practice.code.linked_lists.RemoveKthFromEndNode import remove

from interview.practice.tests.Mixin import example_linked_list


class TestRemoveKthFromEndNode(unittest.TestCase):
    def test_remove(self):

        self.assertEqual(4, remove(example_linked_list(), 3))


if __name__ == '__main__':
    unittest.main()
