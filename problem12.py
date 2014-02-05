"""Project Euler - Problem 12 - http://projecteuler.net/problem=12"""
import sys
import time
import tools.timeutils as timeUtils


def number_of_factors(n):
    """
    Returns the number of factors of number n
    Note: not the actual factors, just how many there are
    """
    factors = 0
    for x in range(1, n + 1):
        if n % x == 0:
            factors += 1
    return factors


def main():
    """Main entry point for the script"""
    start = time.time()
    triangular_number = 1
    n = 1

    while (number_of_factors(triangular_number)) != 500:
        triangular_number = int((n * (n + 1)) / 2)
        n += 1

    timeUtils.elapsed_time(time.time() - start)
    print(triangular_number)


if __name__ == '__main__':
    sys.exit(main())
