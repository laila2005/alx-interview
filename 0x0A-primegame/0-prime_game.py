#!/usr/bin/python3
"""
Prime Game module
Determines the winner of multiple rounds of a prime number game
"""


def is_prime(n):
    """
    Check if a number is prime
    Args:
        n (int): Number to check
    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_game(n):
    """
    Simulate one round of the prime game
    Args:
        n (int): Upper bound of the number set (1 to n)
    Returns:
        bool: True if Maria wins, False if Ben wins
    """
    if n == 1:
        return False

    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False

    moves = 0
    for i in range(2, n + 1):
        if numbers[i] and is_prime(i):
            for j in range(i, n + 1, i):
                numbers[j] = False
            moves += 1

    return moves % 2 == 1


def isWinner(x, nums):
    """
    Determine the overall winner of x rounds of the prime game
    Args:
        x (int): Number of rounds
        nums (list): List of n values for each round
    Returns:
        str or None: Name of player with most wins or None if tied
    """
    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
