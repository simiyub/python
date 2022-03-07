"""
We iterate through the array maintaining an index of the element we are interested in finding
from the subsequence. Each time we find it, we advance our index until we get to the end of the
subsequence or end of the array and return true if we reached the end of the subsequence first
or false if we reached the end of the array without finding the full desired subsequence
Complexity: O(n) T O(1) S
"""


def is_subsequence(array, subsequence):
    index = 0
    for value in array:
        if value == subsequence[index]:
            index += 1

        if index == len(subsequence):
            return True
    return False
