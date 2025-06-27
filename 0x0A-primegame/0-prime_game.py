#!/usr/bin/python3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def play_game(n):
    # If n is 1, no prime numbers, second player wins
    if n == 1:
        return False
    
    # Create array of numbers from 1 to n
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False
    
    # Count moves to determine winner
    moves = 0
    for i in range(2, n + 1):
        if numbers[i] and is_prime(i):
            # Mark prime and its multiples as removed
            for j in range(i, n + 1, i):
                numbers[j] = False
            moves += 1
    
    # If odd number of moves, Maria wins (True)
    # If even number of moves, Ben wins (False)
    return moves % 2 == 1

def isWinner(x, nums):
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
    else:
        return None
