"""Project Euler - Problem 10 - http://projecteuler.net/problem=10"""
import sys
import time
import tools.timeutils as timeutils


def sum_of_primes():
    """
    Finds the sum of all the primes below two million
    """
    n, prime_sum, limit = 2, 0, 2000000
    while limit > 0:
        if is_prime(n):
            prime_sum += n
        n += 1
        limit -= 1
    print(prime_sum)


def is_prime(n):
    """
    Checks if n is a prime number
    Returns: boolean (True if n is prime, False otherwise)
    """
    if n < 2:
        return False
    # the first prime number
    if n == 2:
        return True
    # all even numbers, except 2, are not prime numbers
    if n % 2 == 0:
        return False
    # primality test
    for x in range(3, int(n ** 0.5) + 1, 2):
        # dividing n for all numbers in range [3, sqrt(n) + 1]
        if n % x == 0:
            # n is divisible by x, so n is not a prime
            return False
    # if we get here, then n is a prime
    return True


def main():
    """Main entry point for the script"""
    start = time.time()
    sum_of_primes()
    timeutils.elapsed_time(time.time() - start)


if __name__ == '__main__':
    sys.exit(main())
