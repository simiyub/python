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
