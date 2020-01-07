def _coin_change(coins, amount, count):
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    index = amount - 1
    if count[index] != 0:
        return count[index]
    mini = float("inf")
    for coin in coins:
        res = _coin_change(coins, amount - coin, count)
        if res >= 0 and res < mini:
            mini = 1 + res
    if mini == float("inf"):
        count[index] = -1
    else:
        count[index] = mini
    return count[index]


def coin_change(coins, amount):
    """Function for generating coin change."""
    if amount < 1:
        return 0
    return _coin_change(coins, amount, [0] * amount)


print(coin_change(coins=[2, 3], amount=5))
print(coin_change(coins=[2], amount=3))
