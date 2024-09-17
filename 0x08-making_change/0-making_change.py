#!/usr/bin/python3
"""A module contain function solves the coin change problem
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed
        to meet a given amount total
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for t in range(coin, total + 1):
            dp[t] = min(dp[t], dp[t - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
