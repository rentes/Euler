# Project Euler - Problem 4
# http://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math
import time

# to record last found largest palindrome
largestPalindrome = 0
# numbers for product
number1, number2 = 1, 1

def numberOfDigits(n):
    return 1 + int(math.log10(n))

def isPalindrome(n):
    nrDigits = numberOfDigits(n)
    if nrDigits == 1:
        return True
    elif nrDigits == 2:
        if n / 10 == n % 10:
            return True
        else:
            return False
    elif nrDigits == 3:
        if n / 100 == (n % 100) % 10:
            return True
        else:
            return False
    elif nrDigits == 4:
        if n / 1000 == ((n % 1000) % 100) % 10 and (n % 1000) / 100 == ((n % 1000) % 100) / 10:
            return True
        else:
            return False
    elif nrDigits == 5:
        if n / 10000 == (((n % 10000) % 1000) % 100) % 10 and (n % 10000) / 1000 == (((n % 10000) % 1000) % 100) / 10:
            return True
        else:
            return False
    elif nrDigits == 6:
        if n / 100000 == ((((n % 100000) % 10000) % 1000) % 100) % 10 and (n % 100000) / 10000 == ((((n % 100000) % 10000) % 1000) % 100) / 10 and ((n % 100000) % 10000) / 1000 == (((n % 100000) % 10000) % 1000) / 100:
            return True
        else:
            return False
    else:
        print 'Number of digits higher than 6. Pass.'
        return False

start = time.clock()
while number1 < 1000:
    while number2 < 1000:
        product = number1 * number2
        if isPalindrome(product):
            if product > largestPalindrome:
                largestPalindrome = product # update largest palindrome
        number2 += 1
    number2 = 1 # reset number2
    number1 += 1

print 'largest is', largestPalindrome
elapsed = (time.clock() - start)
print 'elapsed time is', elapsed, 'seconds ~ ', int(elapsed)/60, 'minutes,', int(elapsed)%60, 'seconds,', int((elapsed-(int(elapsed)%60))*1000), 'milliseconds'
