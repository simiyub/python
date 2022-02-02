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

                #root node should not be removed
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
                    parent.right == current.left if current.left is not  None else current.right
                break
        return self

def get_minimum_value(self):
    current = self
    while current.left is not None:
        current = current.left
    return current.value