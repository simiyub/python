"""
This function takes a binary search tree and an integer k and returns the value
of the kth-largest integer in the tree.
We could do an in order traversal of the tree and store the values in an array
which would result in a sorted array and then select the third-largest value in
the array. This would be O(n) T O(n) S
We could do this faster though. We could iterate through the tree from the root to the largest
node first and step back from the largest value to the kth value. This would be O(h+k) T and O(h) S
as we would have to go to the end of the tree to find the largest value which represents the height
of the tree and then walk back up to kth place. The space required is the number of stacks we have
on our way to the largest value.
"""


class TreeVisits:
    def __init__(self, count, last_visited_node):
        self.count = count
        self.last_visited_node_value = last_visited_node


def find_kth_largest_value(tree, value):
    visits = TreeVisits(0, -1)
    traverse_from_largest(tree, value, visits)
    return visits.last_visited_node_value


def find_kth_smallest_value(tree, value):
    visits = TreeVisits(0, -1)
    traverse_from_smallest(tree, value, visits)
    return visits.last_visited_node_value


def traverse_from_largest(tree, value, visits):
    if tree is None or visits.count >= value:
        return
    traverse_from_largest(tree.right, value, visits)
    if visits.count < value:
        visits.count += 1
        visits.last_visited_node_value = tree.value
        traverse_from_largest(tree.left, value, visits)


def traverse_from_smallest(tree, value, visits):
    if tree is None or visits.count >= value:
        return
    traverse_from_smallest(tree.left, value, visits)
    if visits.count < value:
        visits.count += 1
        visits.last_visited_node_value = tree.value
        traverse_from_smallest(tree.right, value, visits)
