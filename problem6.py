"""Project Euler - Problem 6 - http://projecteuler.net/problem=6"""
import sys
import time
import tools.timeutils as timeutils


def sum_square_less_square_sum():
    """
    Finds the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    """
    sum_square = 0

    # sum of the squares
    for i in range(1, 101):
        sum_square += i ** 2

    # square of the sum
    square_sum = ((100 * 101) / 2) ** 2

    print(int(square_sum - sum_square))


def main():
    """Main entry point for the script"""
    start = time.time()
    sum_square_less_square_sum()
    timeutils.elapsed_time(time.time() - start)

if __name__ == '__main__':
    sys.exit(main())
