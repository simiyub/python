"""
These functions return the values of the nodes in order, pre-order and post order.
The order is in respect to the root.
In order, we traverse first the left node, then visit current node and last visit the right.
This will give us the value of the nodes in order of their value.
Pre-order traverses the current node first, then traverses the left branch followed by
the right branch.
We also pass in an array to store the values.
O(n) T O(n) S because we have to visit all the nodes in the tree, and we store
the values in an array which trumps the cost of adding the entries on a call stack.
If we only printed out the values, then the O(d) s where d represents the depth of the queue.
This is the cost of calls on the stack.

"""


def traverse_in_order(tree, array):
    if tree is not None:
        traverse_in_order(tree.left, array)
        array.append(tree.value)
        traverse_in_order(tree.right, array)
    return array


def traverse_pre_order(tree, array):
    if tree is not None:
        array.append(tree.value)
        traverse_pre_order(tree.left, array)
        traverse_pre_order(tree.right, array)
    return array


def traverse_post_order(tree, array):
    if tree is not None:
        traverse_post_order(tree.left, array)
        traverse_post_order(tree.right, array)
        array.append(tree.value)
    return array
