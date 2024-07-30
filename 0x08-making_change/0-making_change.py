#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    total amount when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    remaining_amount = total
    coin_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)

    while remaining_amount > 0:
        if coin_index >= len(sorted_coins):
            return -1
        if remaining_amount >= sorted_coins[coin_index]:
            remaining_amount -= sorted_coins[coin_index]
            coin_count += 1
        else:
            coin_index += 1

    return coin_count
