"""
Requirement: Given a node with an array of zero or more children,
this function will return an array containing the values of the nodes
and the children node values traversed in a depth-first search order.
Implementation: We add the value of the node onto the array to be returned.
Then we recursively do the same for each child in the array of children.
When all is done, we return the array of values.
Complexity: O(vertices+edges) T and O(vertices) S where the edges represent
the children that vertices have and the number of edges. It is the sum of the two
as we visit every node and it’s children. We then store the values of the vertices.
"""


def search(graph, values=None):
    if values is None:
        values = []
    if graph is not None:
        values.append(graph.value)
        for child in graph.children:
            search(child, values)

    return values
