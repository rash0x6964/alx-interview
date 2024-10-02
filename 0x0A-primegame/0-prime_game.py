#!/usr/bin/python3
""" Prime Game """


def generate_primes(n):
    """Helper function to generate all primes
        and their multiples for numbers up to n.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False
    return primes


def calculate_winner(n):
    """Calculate the winner of a game round for a given n.
    """
    primes = generate_primes(n)
    # Maria always plays first
    moves = len(primes)
    if moves % 2 == 0:
        return "Ben"
    else:
        return "Maria"


def isWinner(x, nums):
    """Determine who the winner is after x rounds of the game.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            winner = calculate_winner(n)
            if winner == "Maria":
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
