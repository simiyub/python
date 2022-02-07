"""
Requirement: This function takes a matrix of integers and returns the minimum number of passes
to convert all negative integers to positive.
To convert a negative integer to positive, we need at least one neighbouring positive integer.
A neighbouring integer is one to the left, right, top or bottom.
Zero is considered non-negative/positive and will be ignored.
Implementation: We create a count of passes, a queue of all positive elements in the matrix
and record a count of them separately. We then go through the queue converting all negative
integers neighbouring the positive integers to positive. We add the newly converted integers
to the queue and record a new count. We then use the new integers in the queue and the count
in the next pass. We continue with this process until the queue is empty and return the
value of pass count less one as the last pass is for validating that there are no more negative values.
 If we run through the matrix to the end and there are still negative values ,
 we return -1 as it means the matrix cannot be converted to an all positive integer matrix.
Complexity: O(w*h) T for the width and height of the matrix / array sizes because we
process the matrices at the beginning. O(w*h) S as we store the values to the end.
"""
import copy


def contains_negatives(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False


def indices_of_positive_values(matrix):
    indices = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value > 0:
                indices.append([row, col])
    return indices


def adjacent_positions(row, col, matrix):
    positions = []

    if row > 0 :
        positions.append([row - 1, col])
    if row < len(matrix) - 1:
        positions.append([row + 1, col])
    if col > 0:
        positions.append([row, col - 1])
    if col < len(matrix[0]) - 1 :
        positions.append([row, col + 1])
    return positions


def convert_negatives(matrix):
    queue = indices_of_positive_values(matrix)
    passes = 0
    while len(queue) > 0:
        size = len(queue)
        while size > 0:
            row, col = queue.pop(0)
            positions = adjacent_positions(row, col, matrix)
            for position in positions:
                row, col = position
                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] *= -1
                    queue.append([row, col])
            size -= 1
        passes += 1
    return passes


def minimum_passes(mat):
    matrix = copy.deepcopy(mat)
    passes = convert_negatives(matrix)
    return -1 if contains_negatives(matrix) else passes - 1
