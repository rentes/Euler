"""
Project Euler - Problem 12
http://projecteuler.net/problem=12
"""

import time


def number_of_factors(n):
    """
    Returns the number of factors of number n
    Note: not the actual factors, just how many there are
    """
    number_of_factors = 0
    for x in range(1, n+1):
        if n % x == 0:
            number_of_factors += 1
    return number_of_factors


def elapsed_time(elapsed):
    """
    Computes the amount of time spent by the algorithm and outputs the time
    """
    hour = int(elapsed / 3600)  # hours
    min = int(elapsed / 60)  # minutes
    s = int(elapsed) % 60  # seconds
    ms = int((elapsed - int(elapsed)) * 1000)  # milliseconds
    print('time:', elapsed, 's ~', hour, 'hour,', min, 'min,',
          s, 's,', ms, 'ms')


# start the timing for this problem
start = time.time()
triangular_number = 1
n = 1

while (number_of_factors(int(triangular_number))) != 500:
    triangular_number = (n * (n + 1)) / 2
    n += 1

# compute the total time taken for this problem and show it to the user
elapsed_time(time.time() - start)
print(int(triangular_number))
