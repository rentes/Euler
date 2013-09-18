"""
Project Euler - Problem 12
http://projecteuler.net/problem=12
"""

import time
import tools.timeutils as timeutils


def number_of_factors(n):
    """
    Returns the number of factors of number n
    Note: not the actual factors, just how many there are
    """
    number_of_factors = 0
    for x in range(1, n + 1):
        if n % x == 0:
            number_of_factors += 1
    return number_of_factors


# start the timing for this problem
start = time.time()
triangular_number = 1
n = 1

while (number_of_factors(triangular_number)) != 500:
    triangular_number = int((n * (n + 1)) / 2)
    n += 1

# compute the total time taken for this problem and show it to the user
timeutils.elapsed_time(time.time() - start)
# present the first triangular number to have 500 factors
print(triangular_number)
