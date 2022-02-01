from interview.medium.code.bst.BST import BST


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
