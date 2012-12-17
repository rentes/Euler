"""
Project Euler - Problem 1
http://projecteuler.net/problem=1
Add all the natural numbers below one thousand that are multiples of 3 or 5.
"""

import time


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
elapsed = (time.time() - start)
print('time for this problem to complete:')
print(elapsed, 'seconds ~')
print(int(elapsed / 60), 'minutes,')
print(int(elapsed) % 60, 'seconds,',)
print(int(elapsed * 1000) - ((int(elapsed) % 60) * 1000), 'milliseconds')
