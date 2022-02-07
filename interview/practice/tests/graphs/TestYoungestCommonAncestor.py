import unittest
from interview.practice.code.graphs.AncestralTree import youngest_common_ancestor, AncestralTree
from interview.practice.tests.Mixin import example_ancestral_tree


class TestYoungestCommonAncestor(unittest.TestCase):
    def test_youngest_common_ancestor(self):
        ten = AncestralTree(10)
        five1 = AncestralTree(5)
        five1.ancestor = ten
        fifteen = AncestralTree(15)
        fifteen.ancestor = ten
        fourteen = AncestralTree(14)
        fourteen.ancestor = fifteen
        thirteen = AncestralTree(13)
        thirteen.ancestor = fifteen
        twenty_two = AncestralTree(22)
        twenty_two.ancestor = fifteen
        two = AncestralTree(2)
        two.ancestor = five1
        five2 = AncestralTree(5)
        five2.ancestor = five1
        one = AncestralTree(1)
        one.ancestor = two
        self.assertEqual(10, youngest_common_ancestor(one, fourteen, ten))
        self.assertEqual(5, youngest_common_ancestor(one, five2, ten))


if __name__ == '__main__':
    unittest.main()
