"""
This example uses iteration to find the closest value to a target value
in a BST with Worst and Average case O(n) T and O(1) S
"""
import copy


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_closest_value_in_bst(tree, target):
    return __closest(copy.deepcopy(tree), target, tree.value)


def __closest(tree, target, current_closest):
    while tree is not None:
        if abs(target - current_closest) > abs(target - tree.value):
            current_closest = tree.value

        if target < tree.value and tree.left is not None:
            tree = tree.left
        elif target > tree.value and tree.right is not None:
            tree = tree.right
        else:
            break
    return current_closest
