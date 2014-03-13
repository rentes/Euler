"""Project Euler - Problem 12 - http://projecteuler.net/problem=12"""
import sys
import time
import tools.timeutils as timeUtils


def number_of_factors(n):
    """
    Returns the number of factors of number n

    Using a list to keep the factors found of number n
    """
    factor_found = 0
    max_limit = 0
    list = []
    list.append(1)  # 1 is always a factor

    for m in range(2, n):
        if n % m == 0:
            # found a new factor
            factor_found = int(n / m)
            # I only have to divide n by m until m reaches the result of
            # the quotient of the first factor encountered
            # for example: consider number 28. the first factor is 2 and
            # the quotient gives 14, since 28 / 2 = 14. 14 is then the max
            # limit where m has to increase to, because we know for sure that
            # any m > 14 will not be a factor of 28, and we break the cycle
            # when this condition occurs. This way we only have to make less
            # divisions to find out all the factors of number n
            if max_limit < factor_found:
                max_limit = factor_found
            list.append(factor_found)
        if m > max_limit:
            break
    list.append(n)  # number n is also always a factor
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
    """Testing the number of factors method on problem12.py"""
    assert number_of_factors(28) == 6
    assert number_of_factors(76576500) > 500


if __name__ == '__main__':
    sys.exit(main())
