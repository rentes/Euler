"""
Project Euler - Problem 10
http://projecteuler.net/problem=10
"""

import time
import tools.timeutils as timeutils


def sum_of_primes():
    """
    Finds the sum of all the primes below two million
    """
    n, sum, limit = 2, 0, 2000000
    while limit > 0:
        if is_prime(n):
            sum += n
        n += 1
        limit -= 1
    print(sum)


def is_prime(n):
    """
    Checks if n is a prime number
    Returns: boolean (True if n is prime, False otherwise)
    """
    if n < 2:
        return False
    if n == 2:  # the first prime number
        return True
    if n % 2 == 0:  # all even numbers, except 2, are not prime numbers
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):  # primality test
        if n % x == 0:  # dividing n for all numbers in range [3, sqrt(n) + 1]
            return False  # n is disible by x, so n is not a prime
    return True  # if we get here, than n is a prime


start = time.time()
sum_of_primes()
timeutils.elapsed_time(time.time() - start)
