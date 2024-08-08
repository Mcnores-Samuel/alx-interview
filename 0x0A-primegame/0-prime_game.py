#!/usr/bin/python3
"""Prime Game module. This module contains a
function that determines the winner of a prime game.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game.
    The game is played by two players, Maria and Ben.
    They play a game of prime numbers. The players take turns
    picking a prime number from the list of numbers.
    The player who picks the last prime number wins the game.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of n integers.

    Returns:
        str: The name of the player who wins the game. If the game ends in a tie,
        return None.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'

