"""
Requirement:This function will receive an array of integers and
create an array of unique permutations or ordering of integers
that can be created from the integers in the array.
Implementation: We build all permutations for the array within the array in place using pointers.
We select the first element in the array and use it as a starting element of all the combinations
of permutations that can be formed from the rest of the elements in the array.
We swap the first element in the remaining array of elements with the current anchor index.
Then we iteratively call the helper method a second time with the next element in the array of
remaining elements, the array and the array of permutations.
When we are done with this call, we swap back the elements to how they were before
and move on to the next index after the anchor index. When the index is the last one in the array,
we copy the array into the array of permutations.
Complexity: O(n*n!) T and O(n.n!) S For each element in the array,
we make calls to the helper  equivalent to the position of the element in the array
which means the last one will have n.n! calls.
"""


def __swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def __permutations_helper(anchor_index, array, all_permutations):
    if anchor_index == len(array) - 1:
        all_permutations.append(array[:])
    else:
        for j in range(anchor_index, len(array)):
            __swap(array, anchor_index, j)
            __permutations_helper(anchor_index + 1, array, all_permutations)
            __swap(array, anchor_index, j)


def permutations(array):
    permutations_found = []
    __permutations_helper(0, array, permutations_found)
    return permutations_found
