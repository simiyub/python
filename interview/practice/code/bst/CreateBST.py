"""
 This is a BST implementation with O(n) T and O(n) S in worst case
 This class supports inserting,removing and checking if a value is in the tree.
 The tree will always have at least one node which cannot be removed.
 Each tree has an integer value and potentially a left and right node.
 The value of a node is strictly greater than the value of the nodes to the left,
 and it is greater than or equal to the values of the nodes to the right.
 """


class CreateBST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        We compare the value of the current node with the value we want to insert.
        We continue with the search to the left if the value we want to insert is less than
        the current node or right if the value we want to insert is greater than the current
        node value. We do this recursively until we find an empty slot suitable for our
        value and insert it into the tree.
        """
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = CreateBST(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = CreateBST(value)
                    break
                else:
                    current = current.right
        return self

    def contains(self, value):
        """
        In searching for a given value, we start with the current node in the tree provided
        and check if it is the value we are interested in.
        If it is greater than the value we want,
        we search the tree to the left and to the right if the current node is less.
        We do this iteratively until we find the node of interest or return -1 if it doesn’t exist.
        """
        current = self
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def remove(self, value, parent):
        """
        Simplest case, we search for a node and find it as a leaf.
        In this case, we just remove it by setting the parent pointer to point to null.
        If the node only has one child node, we set the parent of the node to point to the single child
        and the deletion is complete.
        If the node has more than one child, then we go down the right of the tree from the node
        we want to delete and move the smallest value node to the current node.
        This is because we know it’s greater than all the values to the node’s left and
        it is smaller than all the ones to the right.

        """
        current = self
        while current is not None:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                if current.left is not None and current.right is not None:
                    current.value = current.right.get_minimum_value()
                    current.right.remove(current.value, current)

                # root node should not be removed
                elif parent is None:
                    if current.left is not None:
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left

                    elif current.right is not None:
                        current.value = current.right.get_minimum_value
                        current.left = current.right.left
                        current.right = current.right.right
                    else:
                        current.value = None

                elif parent.left == current:
                    parent.left = current.left if current.left is not None else current.right
                elif parent.right == current:
                    parent.right = current.left if current.left is not None else current.right
                break
        return self


def get_minimum_value(self):
    current = self
    while current.left is not None:
        current = current.left
    return current.value
