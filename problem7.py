"""
Project Euler - Problem 7
http://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13. What is the 10 001st prime number?
"""

import time

def is_prime(n):
    """
    Checks if n is a prime number
    Returns: boolean (True if n is prime, False otherwise)
    """
    if n < 2:
        return False
    if n == 2: # the first prime number
        return True
    if n % 2 == 0: # all even numbers, except 2, are not prime numbers
        return False
    for x in range(3, int(n**0.5)+1, 2): # primality test
       if n % x == 0: # dividing n for all numbers in range [3, sqrt(n) + 1]
            return False # n is disible by x, so n is not a prime
    return True # if we get here, than n is a prime

def ten_thousand_first_prime():
    """
    Finds the 10 001st prime number
    """
    n = 2 # natural numbers, starting with 2
    count = 0 # prime number counter
    largest = 0 # the newest prime number found
    while count < 10001:
        if is_prime(n) == True:
            count += 1
            largest = n
        n += 1
    print(largest)

start = time.time()
ten_thousand_first_prime()
elapsed = (time.time() - start)
print('time:', elapsed, 'seconds ~', \
    int(elapsed/60), 'minutes,', \
    int(elapsed)%60, 'seconds,', \
    int(elapsed*1000)-((int(elapsed)%60)*1000), 'milliseconds')
