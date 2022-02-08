import unittest
from interview.practice.code.linked_lists.ReverseLinkedList import reverse

from interview.practice.tests.Mixin import example_linked_list


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(6, reverse(example_linked_list()).value)


if __name__ == '__main__':
    unittest.main()
