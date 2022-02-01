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
