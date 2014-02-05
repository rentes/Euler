"""Project Euler - Problem 2 - http://projecteuler.net/problem=2"""
import sys
import time
import tools.timeutils as timeutils


def fib(n):
    """
    Fibonacci nth number definition based on Dijsktra's paper here:
    www.cs.utexas.edu/users/EWD/ewd06xx/EWD654.pdf
    """
    # fibonacci dictionary used for memoization
    fibs = {0: 0, 1: 1}

    if n in fibs:
        return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
        return fibs[n]
    else:
        fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n + 1) / 2) ** 2)
        return fibs[n]


def sum_fibonacci():
    """
    Find the sum of the even-valued terms of the Fibonacci sequence
    """
    sum = 0
    n = 1

    while sum < 4000000:
        if fib(n) % 2 == 0:
            sum = sum + fib(n)
        n += 1
    print(sum)


def main():
    """Main entry point for the script"""
    start = time.time()
    sum_fibonacci()
    timeutils.elapsed_time(time.time() - start)


if __name__ == '__main__':
    sys.exit(main())
