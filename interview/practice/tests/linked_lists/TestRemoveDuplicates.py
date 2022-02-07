import unittest

from interview.practice.code.Node import Node
from interview.practice.code.linked_lists.RemoveDuplicates import remove


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        three = Node(3)
        four = Node(4)
        four2 = Node(4)
        four3 = Node(4)
        five = Node(5)
        six = Node(6)
        six2 = Node(6)
        one = Node(1)
        one2 = Node(1)
        one.next = one2
        one2.next = three
        three.next = four
        four.next = four2
        four2.next = four3
        four3.next = five
        five.next = six
        six.next = six2

        count = 0
        unique = remove(one)
        while unique is not None:
            unique = unique.next
            count += 1

        self.assertEqual(5, count)  # add assertion here


if __name__ == '__main__':
    unittest.main()
