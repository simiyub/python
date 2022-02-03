"""
Requirement: This function will receive an array of integers and a target value
and will determine the number of ways in which we can obtain the given value using
the values in the array. This is similar to the scenario where you have various denominations
of a currency and a target amount.
Implementation: We first create an array in which we store the number of ways we
can create the value required from each denomination.
This array is the size of the target value. Each index in the array represents the
values that can be formed from the denominations between 0 and the target value.
We initialise the first element in the array to 1 which effectively means
there is only one way to form 0 and that is use none of the denominations in the array.
We then iterate through the denominations and for each, we determine the number of ways
we can form the values represented in the index of ways from 0 to the target value.
The number of ways will be the value in the index of the target amount plus
the value of the element in the index of amount less the denomination.
When we have iterated through all the denominations, the number of ways to make that
value is the value in the index = target value in the array of ways.
Complexity: O(denominations * target value) T as we go through each denomination and
for each update the ways array. O(target value) as we maintain an array the size of the target value.
"""


def ways_to_make_value(denominations, target_value):
    ways = [0 for _ in range(target_value+1)]
    ways[0] = 1
    for denom in denominations:
        for value in range(1, len(ways)):
            if denom <= value:
                ways[value] += ways[value - denom]
    return ways[target_value]
