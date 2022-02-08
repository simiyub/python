"""
Requirement: This function receives a number n and returns the value of the nth term in a
fibonacci sequence. The Fibonacci sequence is a sequence commonly denoted Fn where the next
number is found by adding the two numbers before it.
The sequence commonly starts from 0 and 1 and the next few values in the
sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.
Implementation: Since the value of the next number in the sequence is the sum of the
previous two values,
we need to track the values of the previous two terms to make this work efficiently.
So we start by initialising a temp array of first two numbers [0, 1] and then we iteratively
replace the values in the array with previous and current sum until we get to the nth term
or zero if the nth term is less than 1.
Complexity: O(n) T O(1) S as we traverse iteratively to the nth term.
"""


def get(term):
    previous_two = [0, 1]
    count = 3
    while count <= term:
        new_value = previous_two[0] + previous_two[1]
        previous_two[0] = previous_two[1]
        previous_two[1] = new_value
        count += 1
    return previous_two[1] if term > 1 else previous_two[0]
