"""
Requirement: Receives three instances of a class with details of the ancestor.
Graph that is a tree where the flow is upward towards the ancestor.
Implementation: We traverse the tree upward from the lowest descendant to the level where
the two descendants are at the same level.
We then move upward on both trees until we have a common node and that is the common ancestor.
Complexity: O(d) T where d is the depth of the descendant that is lower O(1) S
as we do not need to store any data.
"""
class AncestralTree:
    def __init__(self, value):
        self.value = value
        self.ancestor = None


def get_depth(descendant, top_ancestor):
    depth = 0
    while descendant.value != top_ancestor.value:
        depth += 1
        descendant = descendant.ancestor
    return depth


def first_common_ancestor(younger, older, diff):
    while diff > 0:
        younger = younger.ancestor
        diff -= 1
    while younger != older:
        younger = younger.ancestor
        older = older.ancestor
    return younger


def youngest_common_ancestor(descendant1, descendant2, top_ancestor):
    depth_descendant_1 = get_depth(descendant1, top_ancestor)
    depth_descendant_2 = get_depth(descendant2, top_ancestor)

    if depth_descendant_1 > depth_descendant_2:
        return first_common_ancestor(descendant1, descendant2, depth_descendant_1 - depth_descendant_2).value
    return first_common_ancestor(descendant2, descendant1, depth_descendant_2 - depth_descendant_1).value
