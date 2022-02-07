"""
Requirement: This function takes a two dimensional matrix and returns an array of the size of rivers
 in the array. A river is represented by 1 in the array.
 1 without any other 1s adjacent to it is a river of size 1.bAdjacency can be vertical,
 horizontal or both. For example:
 [
  [1,0,0,1,0]
  [1,0,1,0,0]
  [0,0,1,0,1]
  [1,0,1,0,1]
  [1,0,1,1,0]
  ]
will return [1,2,2,2,5]
Implementation: We iterate through the multidimensional array and whenever we find a 1,
we follow through, identifying any adjacent 1s - parts of the river and adding to the size.
Once we determine that no more consecutive 1s exist, we add the size to the array that is returned.

Complexity: O(wh) T O(wh) S as we traverse the multidimensional matrix once from top to bottom,
left to right and track the elements we have reviewed and store the count in the array to be returned.
"""
def sizes(matrix):
    rivers = []
    visited = [[False for value in row] for row in matrix]  # we initialise every entry as not visited.

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not visited[i][j]:
                traverse_node(i, j, matrix, visited, rivers)
    return rivers


def traverse_node(i, j, matrix, visited, rivers):
    current_river_size = 0
    nodes_to_explore = [[i, j]]
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if not visited[i][j]:
            visited[i][j] = True
            if matrix[i][j] != 0:
                current_river_size += 1
                unvisited_neighbours = get_unvisited_neighbours(i, j, matrix, visited)
                for neighbour in unvisited_neighbours:
                    nodes_to_explore.append(neighbour)
    if current_river_size > 0:
        rivers.append(current_river_size)


def get_unvisited_neighbours(i, j, matrix, visited):
    unvisited_neighbours = []
    if i > 0 and not visited[i - 1][j]:
        unvisited_neighbours.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_neighbours.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisited_neighbours.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited_neighbours.append([i, j + 1])
    return unvisited_neighbours