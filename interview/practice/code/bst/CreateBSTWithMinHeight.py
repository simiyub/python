"""
This function creates a BST with the shortest depth which is the depth of the deepest node
in the BST from a sorted array of distinct integers. We want the tree to be as balanced as possible,
holding as close to equal as possible of the nodes in the left subtree as the right.
These still need to satisfy valid BST requirement: every node to the left of a node should
have a value less than the value of the current node and the node to the right must have a
value greater than or equal to the current node.
With a sorted array, the node in the middle of the array has roughly the same number of nodes
either way, making it the ideal candidate to be the root node.
We recursively select the element in the middle of the sub array on either side and make it
the root of the sub-branch and allocate the value to the left to left of the root and the
one to the right to the right of the root.
O(n) T O(n) S because we will need	to visit all the elements in the array and insert all
entries in the tree using recursion.
"""
from interview.practice.code.bst.BST import BST


def min_height_bst(array):
    return min_height_bst_helper(array, None, 0, len(array) - 1)


def min_height_bst_helper(array, bst, start_index, end_index):
    if end_index >= start_index:
        mid_index = (start_index + end_index) // 2
        new_bst = BST(array[mid_index])
        if bst is None:
            bst = new_bst
        else:
            if array[mid_index] < bst.value:
                bst.left = new_bst
                bst = bst.left
            else:
                bst.right = new_bst
                bst = bst.right

        min_height_bst_helper(array, bst, start_index, mid_index - 1)
        min_height_bst_helper(array, bst, mid_index + 1, end_index)
    return bst
