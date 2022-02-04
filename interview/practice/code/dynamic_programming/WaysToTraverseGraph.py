"""
Requirement: This function receives two positive integers representing the width
and the height of a grid that is the representation of a graph. With this,
the function will return the total number of ways to get to the bottom right of the graph.
The function assumes that the only directions we can take are down and right.
The width * height will always be more than 2 to give us a valid graph.
Implementation:
Using dynamic programming. The approach is walking down from beginning to end while
storing the number of ways to the next cell as we go down.
Complexity: O(wh) T as we traverse through the two-dimensional array
represented by the width and the height. O(wh) S as we store the count of ways
to each grid as we go from beginning to end.
"""
def ways_to_traverse_graph(width, height):
    ways = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    for width_index in range(1, width + 1):
        for height_index in range(1, height + 1):
            if width_index == 1 or height_index == 1:
                ways[height_index][width_index] = 1
            else:
                ways_left = ways[height_index][width_index - 1]
                ways_top = ways[height_index - 1][width_index]
                ways[height_index][width_index] = ways_left + ways_top
    return ways[height][width]
