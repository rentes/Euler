"""Project Euler - Problem 1 - http://projecteuler.net/problem=1"""
import sys
import time
import tools.timeutils as timeUtils


def sum_numbers():
    """
    Sums all natural numbers below 1000 that are multiples of 3 or 5
    Returns: int
    """
    a, b = 1, 0
    while a < 1000:
        if ((a % 3 == 0) or (a % 5 == 0)):
            b += a
        a += 1
    return b


def main():
    """Main entry point for the script"""
    start = time.time()
    print(sum_numbers())
    timeUtils.elapsed_time(time.time() - start)


if __name__ == '__main__':
    sys.exit(main())
