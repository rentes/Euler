"""Project Euler - Problem 12 - http://projecteuler.net/problem=12"""
import sys
import time
import tools.timeutils as timeUtils


def number_of_factors(n):
    """
    Returns the number of factors of number n

    Using a list to keep the factors found of number n
    """
    quotient = 0
    max_limit = 0
    nr_factors = 2  # 1 and n are always factors

    for m in range(2, n):
        if n % m == 0:
            # found a new factor
            nr_factors += 1
            # I only have to divide n by m until m reaches the result of
            # the quotient of the first factor encountered
            # for example: consider number 28. the first factor is 2 and
            # the quotient gives 14, since 28 / 2 = 14. 14 is then the max
            # limit where m has to increase to, because we know for sure that
            # any m > 14 will not be a factor of 28, and we break the cycle
            # when this condition occurs. This way we only have to make less
            # divisions to find out all the factors of number n
            quotient = int(n / m)
            if max_limit < quotient:
                max_limit = quotient
        if m > max_limit:
            break
    return nr_factors


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
    """Testing the number of factors method [problem 12]"""
    assert number_of_factors(28) == 6
    assert number_of_factors(76576500) > 500


if __name__ == '__main__':
    sys.exit(main())
