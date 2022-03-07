"""
 * We iterate through the array, maintaining a map of numbers we have viewed as potential matches.
 * We check in each iteration if the number we are currently looking at would give us the target
 * sum with any of the numbers in our map. If so, we return the two numbers otherwise,
 * we add it to the map.
 * O(n) T O(n) S storage
"""


def find_sum(array, target):
    viewed = {}
    for value in array:
        complement = target-value
        if viewed.get(complement):
            return [value, complement]
        else:
            viewed.update({value: True})
    return []
