"""
Requirement: This function will receive a node class that has a value and a list of children.
Given an empty array, the function will return the array populated with values of all the nodes
populated after a breadth-first search traversal.
Implementation: This function populates the value of the node into a queue and
then populated the values of the children into the queue too.
We then remove the values in order from the queue and populate the array to be returned.
We do this iteratively to the end of the graph and return the array.
Complexity:O(v+e) T  O(v) as we traverse the nodes and their children that are represented
by the number of edges and store the values of the edges in the array.
"""


def search(node, array):
    queue = [node]
    while len(queue) > 0:
        current = queue.pop(0)
        array.append(current.value)
        for child in current.children:
            queue.append(child)
    return array
