"""
Max Sum of Non-Adjacent integers in an array
Requirement: This function takes an array of positive integers and
returns the maximum value that can be obtained from summing up
non-adjacent integers in an array.
Implementation: We traverse the array from the beginning tracking two values:
The current and previous sum.
We initialise the previous sum with the element at index 0 and current sum with
the greater of current element and element at index 0.
When we advance our pointer, we assign the current sum value to the previous sum.
We then compute a new current sum as the greater of the current sum value compared to
the previous value + current value where our pointer is.
We continue with this computation to the end of the array and
return the current sum which will be the greatest sum of non-adjacent values in the array.
Complexity: O(n) T as we have to traverse the whole array to determine the greatest sum.
O(1) S required to store the value of the maximum sum.
"""


def greatest_sum(array):

    if len(array) > 2:
        previous_sum = array[0]
        current_sum = max(array[1], previous_sum)
        for i in range(2, len(array)):
            new_sum = max(previous_sum + array[i], current_sum)
            previous_sum = current_sum
            current_sum = new_sum
        return current_sum

    return array[0] if len(array) == 1 else 0
