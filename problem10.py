"""
Project Euler - Problem 10
http://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import time


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


def elapsed_time(elapsed):
    """
    Computes the amount of time spent by the algorithm and outputs the time
    """
    min = int(elapsed / 60)  # minutes
    s = int(elapsed) % 60  # seconds
    ms = int((elapsed - int(elapsed)) * 1000)  # milliseconds
    print('time:', elapsed, 's ~', min, 'min,', s, 's,', ms, 'ms')

start = time.time()
sum_of_primes()
elapsed_time(time.time() - start)
