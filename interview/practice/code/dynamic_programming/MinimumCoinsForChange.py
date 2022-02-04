"""
Requirement:Given a target value, this function will take an array representing coin denominations
and return the least number of coins required to make that value.
Implementation: We maintain an array whose indices are equivalent to values from 0 to the desired
amount.In the array, we store a value of the minimum number of coins required to raise the
amount(value of the index). We replace the value each time we find a coin count lower than
the value we have in the array.
Complexity: O(denominations * target value) T as we go through each denomination and for
each update the arrays of minimum coins. O(target value) S as we maintain an array the size
of the target value.
"""

def coins_for_change(target_amount, denominations):
    coin_count = [float("inf") for _ in range(target_amount + 1)]
    coin_count[0] = 0

    for denom in denominations:
        for i in range(1, len(coin_count)):
            if denom <= i:
                new_count = coin_count[i-denom] + 1
                coin_count[i] = min(coin_count[i], new_count)

    minimum_coins = coin_count[target_amount]
    if coin_count[target_amount] == float("inf"):
            minimum_coins = -1

    return minimum_coins
