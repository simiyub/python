"""
Requirement: This function will receive an array of integers of which the value in each index
represents the number of steps from the current index to the next one.
Negative values represent a backward move. If we go out of bounds in either direction,
we wrap around the length and find our way back into the array.
This function will determine if the moves represented in the array represent a single
cycle from the beginning to the end.
Implementation: We iterate through the array to determine if we have a single cycle.
Soon as we find one we return true, otherwise we check to the end of the array and return False.
Complexity: O(n) T in worst case as we would traverse the whole graph to find the cycle
or to determine there is none. O(1) S as we don’t need to store values as we iterate through the array.
"""


def has_single_cycle(array):
    steps = 0
    starting_index = 0
    index = 0

    while steps < len(array):
        if steps > 0 and index == starting_index:
            return False
        steps += 1

        index = (index + array[index]) % len(array)
        if index < 0:
            index = index + len(array)
    return index == starting_index
