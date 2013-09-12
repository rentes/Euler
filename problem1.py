"""
Project Euler - Problem 1
http://projecteuler.net/problem=1
"""

import time
import tools.timeutils as timeutils


def sum_numbers():
    """
    Sums all natural numbers below 1000 that are multiples of 3 or 5
    Returns: int
    """
    a, b = 1, 0
    while a < 1000:
        if ((a % 3 == 0) or (a % 5 == 0)):  # if a is multiple or 3 or 5
            b += a  # add a to the sum
        a += 1  # let us check next integer
    return b


start = time.time()
print(sum_numbers())
timeutils.elapsed_time(time.time() - start)
