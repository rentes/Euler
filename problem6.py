"""
Project Euler - Problem 6
http://projecteuler.net/problem=6
"""

import time
import tools.timeutils as timeutils


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


start = time.time()
sum_square_less_square_sum()
timeutils.elapsed_time(time.time() - start)
