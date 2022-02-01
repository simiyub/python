"""
This function takes a data structure that is a BST. The nodes in the tree have a value
and a node to the left or right or None. The left node must be less that the node’s value
and the node to the right must be greater than or equal to the value of the BST.
The children of each node must also be a BST.
Each node has a maximum abd a minimum value. We validate that each node is valid and if
we get to the end.
O(n) T as we are traversing every node. (O)We use space on the call stack
"""

import copy


def __is_valid(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value < min_value or tree.value >= max_value:
        return False
    elif tree.right is not None and not __is_valid(tree.right, tree.value, max_value):
        return False
    return __is_valid(tree.left, min_value, tree.value)


def validate_bst(tree):
    return __is_valid(copy.deepcopy(tree), float("-inf"), float("inf"))
