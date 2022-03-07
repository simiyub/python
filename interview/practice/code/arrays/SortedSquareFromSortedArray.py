"""
Given an array of sorted integers, this function returns a sorted array of the square of the numbers
"""


def sorted_square_array(array):
    return [value **2 for value in array]