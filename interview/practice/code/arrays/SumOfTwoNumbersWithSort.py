"""
/**
 * We sort the array then iterate through it comparing the sum of the largest and smallest element
 * until we find a sum that is equal to the target sum and return or return an empty array.
 * Time Complexity: O(nlogn) T O(1) S storage
 * */
"""


def find_sum(array, target):
    array.sort()
    start = 0
    end = len(array)-1
    for i in range(len(array)-1):
        current_sum = array[start] + array[end]
        if current_sum == target:
            return [array[start], array[end]]
        if current_sum > target:
            end -= 1
        if current_sum < target:
            start += 1

    return []
