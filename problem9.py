"""
Project Euler - Problem 9
http://projecteuler.net/problem=9
"""

import time
import tools.timeutils as timeutils


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


start = time.time()
pythagorean_triplet()
timeutils.elapsed_time(time.time() - start)
