"""
Project Euler - Problem 6
http://projecteuler.net/problem=6
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

import time


def sum_square_less_square_sum():
    """
    Finds the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    """
    sumSquare = 0
    squareSum = 0

    # sum of the squares
    for i in range(1, 101):
        sumSquare += i ** 2

    # square of the sum
    squareSum = ((100 * 101) / 2) ** 2

    print(int(squareSum - sumSquare))


def elapsed_time(elapsed):
    """
    Computes the amount of time the algorithm ran and outputs the time
    """
    min = int(elapsed / 60)  # minutes
    s = int(elapsed) % 60  # seconds
    ms = int(elapsed * 1000) - ((int(elapsed) % 60) * 1000)  # milliseconds
    print('time:', elapsed, 's ~', min, 'min,', s, 's,', ms, 'ms')

start = time.time()
sum_square_less_square_sum()
elapsed_time(time.time() - start)
