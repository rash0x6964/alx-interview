#!/usr/bin/python3
"""A module contain function solves the coin change problem
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed
        to meet a given amount total
    """
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        num_coins += total // coin
        total %= coin

    if total == 0:
        return num_coins
    else:
        return -1
