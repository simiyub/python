
class AncestralTree:
    def __init__(self, value):
        self.value = value
        self.ancestor = None


def get_depth(descendant, topAncestor):
    depth = 0
    while descendant.value != topAncestor.value:
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



def youngest_common_ancestor(descendant1, descendant2, topAncestor):
    depth_descendant_1 = get_depth(descendant1, topAncestor)
    depth_descendant_2 = get_depth(descendant2, topAncestor)

    if depth_descendant_1>depth_descendant_2:
        return first_common_ancestor(descendant1, descendant2, depth_descendant_1 - depth_descendant_2).value
    return first_common_ancestor(descendant2, descendant1, depth_descendant_2 - depth_descendant_1).value



