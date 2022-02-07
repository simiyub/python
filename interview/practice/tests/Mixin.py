from interview.practice.code.Node import Node
from interview.practice.code.bst.BST import BST
from interview.practice.code.graphs.AncestralTree import AncestralTree


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

def example_node():
    ten = Node(10)

    one = Node(1)
    two = Node(2)
    two.children = [one]

    five2 = Node(5)
    five1 = Node(5)
    five1.children = [two, five2]



    fourteen = Node(14)
    thirteen = Node(13)
    thirteen.children = [fourteen]

    twenty_two = Node(22)
    fifteen = Node(15)
    fifteen.children   = [thirteen, twenty_two]

    ten.children = [five1, fifteen]

    return ten

def example_ancestral_tree():

    ten = AncestralTree(10)
    five1 = AncestralTree(5)
    five1.ancestor = ten
    fifteen = AncestralTree(15)
    fifteen.ancestor = ten
    thirteen = AncestralTree(13)
    thirteen.ancestor = fifteen
    fourteen = AncestralTree(14)
    fourteen.ancestor = fifteen
    twenty_two = AncestralTree(22)
    twenty_two.ancestor = fifteen
    two = AncestralTree(2)
    two.ancestor = five1
    five2 = AncestralTree(5)
    five2.ancestor = five1
    one = AncestralTree(1)
    one.ancestor = two
    return ten

