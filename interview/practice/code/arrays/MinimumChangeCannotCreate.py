"""
Requirement: Given an array of integers that represent a set of coins,
write a function that returns the minimum amount of change that cannot be created with the set of coins.
Given no coins [ ], the minimum change that you cannot create would be 1 and given [1, 2, 5],
you cannot create 4.

Implementation: We sort the array in place. We then set a variable to track the change we can create,
starting with 1. If we have a value less than or equal to the current change we can create,
we add the value of the coin to what we can create until we reach a point
where the value of the coin is greater than the current change we can create.
At this point we return the value of what we can create plus 1 which is the least amount of change
beyond what we have that we cannot create.
Complexity:  O(nlogn) T and O(1) S as we sorted the array and then iterated through it in n time,
but the sort of nlogn is greater. We sorted the array in place, so no extra space is required.
"""
def minimum_change_cannot_create(coins):
    coins.sort()
    can_create = 0

    for coin in coins:
        if coin > can_create + 1:
            return can_create + 1
        can_create += coin
    return can_create + 1
