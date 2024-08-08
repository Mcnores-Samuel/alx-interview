#!/usr/bin/python3
"""Prime Game module. This module contains a function that determines the winner
of a prime game.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game. The game is played by two players,
    Maria and Ben. They play a game of prime numbers. The players take turns
    picking a prime number from the list of numbers. The player who picks the
    last prime number wins the game.

    Args:
        x (int): The number of rounds.
        nums (list of int): A list of n integers.

    Returns:
        str: The name of the player who wins the game. If the game ends in a tie,
        return None.
    """
    def is_prime(num):
        """Determines if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [i for i in range(1, n + 1) if is_prime(i)]
        turns = 0
        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            turns += 1
        
        if turns % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
