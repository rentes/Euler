"""Project Euler - Problem 15 - http://projecteuler.net/problem=15"""
import sys
import time
import math
import tools.timeutils as timeutils


def combinations_n_k(n, k):
    """Returns the number of combinations n choose k"""
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


def main():
    """Main entry point for the script"""
    start = time.time()

    # please see http://copingwithcomputers.com/2013/07/06/lattice-paths/
    # for an explanation on the relation of lattice paths with Pascal numbers
    print(combinations_n_k(40, 20))

    timeutils.elapsed_time(time.time() - start)

if __name__ == '__main__':
    sys.exit(main())
