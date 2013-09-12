"""
Project Euler - Problem 2
http://projecteuler.net/problem=2
"""

import time
import tools.timeutils as timeutils


def fib(n):
    """
    Fibonacci nth number definition based on Dijsktra's paper here:
    www.cs.utexas.edu/users/EWD/ewd06xx/EWD654.PDF
    (I love it)
    """
    fibs = {0: 0, 1: 1}  # fibonacci dictionary used for memoization

    if n in fibs:
        return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
        return fibs[n]
    else:
        fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n + 1) / 2) ** 2)
        return fibs[n]


def sum_fibonacci():
    """
    Find the sum of the even-valued terms of the Fibonacci sequence
    """
    count = 0  # counter that will hold the sum
    n = 1  # counter for iterations

    while count < 4000000:
        if fib(n) % 2 == 0:  # we only want even fibonacci numbers
            count = count + fib(n)
        n += 1
    print(count)


start = time.time()
sum_fibonacci()
timeutils.elapsed_time(time.time() - start)
