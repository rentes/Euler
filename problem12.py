"""Project Euler - Problem 12 - http://projecteuler.net/problem=12"""
import sys
import time
import tools.timeutils as timeUtils

solution = 0

def number_of_factors(n):
    """
    Returns the number of factors of number n
    Note: not the actual factors, just how many there are
    """
    factors = 0
    factor_found = 0
    max_limit = 0
    list = []
    list.append(1)

    for m in range(2, n):
        if n % m == 0:
            factor_found = int(n / m)
            if max_limit < factor_found:
                max_limit = factor_found
            list.append(factor_found)
        if m > max_limit:
            break
    list.append(n)
    return len(list)


def main():
    """Main entry point for the script"""
    start = time.time()
    triangular_number = 1
    n = 2

    while number_of_factors(triangular_number) <= 500:
        triangular_number += n
        n += 1

    timeUtils.elapsed_time(time.time() - start)
    print(triangular_number)


def test_number_of_factors():
    """Testing the number of factors method"""
    assert number_of_factors(28) == 6
    assert number_of_factors(76576500) > 500


if __name__ == '__main__':
    sys.exit(main())
