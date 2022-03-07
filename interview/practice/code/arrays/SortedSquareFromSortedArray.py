"""
Given an array of sorted integers, this function returns a sorted array of the square of the numbers
"""


def sorted_square_array(array):
    result = [0 for _ in array]
    smaller_value_index = 0
    larger_value_index = len(array) - 1

    for index in reversed(range(len(array))):
        smaller_value = array[smaller_value_index]
        larger_value = array[larger_value_index]

        if (abs(smaller_value) > abs(larger_value)):
            result[index] = smaller_value ** 2
            smaller_value_index += 1
        else:
            result[index] = larger_value ** 2
            larger_value_index += 1
    return result
