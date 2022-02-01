from interview.medium.code.BST import BST


def example_bst():
    ten = BST(10)

    one = BST(1)
    two = BST(2)
    two.left = one
    five2 = BST(5)
    five1 = BST(5)
    five1.left = two
    five1.right = five2

    ten.left = five1
    fourteen = BST(14)
    thirteen = BST(13)
    thirteen.right = fourteen
    twenty_two = BST(22)
    fifteen = BST(15)
    fifteen.left = thirteen
    fifteen.right = twenty_two
    ten.right = fifteen

    return ten