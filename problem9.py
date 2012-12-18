"""
Project Euler - Problem 9
http://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time


def pythagorean_triplet():
    """
    Finds the product of the terms of the pythagorean triplet a, b and c,
    for which a^2 + b^2 = c^2 and a + b + c = 1000
    """
    a, b, c = 1, 1, 1
    triplet_found = False

    while a < 1000 and triplet_found is False:
        while b < 1000 and triplet_found is False:
            while c < 1000 and triplet_found is False:
                if (a ** 2 + b ** 2 == c ** 2) and (a + b + c == 1000):
                    print("triplet is:", a, b, c)
                    print("product is:", a * b * c)
                    triplet_found = True
                else:
                    c += 1
            b += 1
            c = 1
        a += 1
        b = 1


def elapsed_time(elapsed):
    """
    Computes the amount of time spent by the algorithm and outputs the time
    """
    min = int(elapsed / 60)  # minutes
    s = int(elapsed) % 60  # seconds
    ms = int((elapsed - int(elapsed)) * 1000)  # milliseconds
    print('time:', elapsed, 's ~', min, 'min,', s, 's,', ms, 'ms')

start = time.time()
pythagorean_triplet()
elapsed_time(time.time() - start)
