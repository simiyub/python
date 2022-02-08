"""
Requirement: this function receives an array that could be an array of values or array of integers
and returns the product sum. The product sum is the sum of elements in array multiplied
by the depth of the array.
As an example: The sum of [2, 4, [4, 5, 3, [6, 5] ] ]
will be 2 +4 +2(4 + 5 + 3 + 3(6 + 5)) = 6 + 2*(12 + (3*11)) = 6 + (2 *45) = 96
Implementation: Using a helper function, we provide a multiplier to pass in the level
with which we multiply the sum. Then we sum up the values in the array if they are integers
and multiply with the multiplier or call the function recursively if the value is an array.
Complexity: O(n) T and O(d) S as we traverse through the array to the end.
We require the space for the stack when we run the helper function recursively
for arrays within the array.
"""


def __product_sum(unknown, multiplier=1):
    value_sum = 0
    for value in unknown:
        if type(value) is list:
            value_sum += __product_sum(value, multiplier + 1)
        else:
            value_sum += value
    return value_sum * multiplier


def product_sum(array):
    return __product_sum(array, 1)
