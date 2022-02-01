def traverse_in_order(tree, array):
    if tree is not None:
        traverse_in_order(tree.left, array)
        array.append(tree.value)
        traverse_in_order(tree.right, array)
    return array


def traverse_pre_order(tree, array):
    if tree is not None:
        array.append(tree.value)
        traverse_pre_order(tree.left,array)
        traverse_pre_order(tree.right,array)
    return array


def traverse_post_order(tree, array):
    if tree is not None:
        traverse_post_order(tree.left,array)
        traverse_post_order(tree.right,array)
        array.append(tree.value)
    return array