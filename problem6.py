# Project Euler - Problem 6
# http://projecteuler.net/problem=6
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

import time

start = time.time()

sumSquare = 0
squareSum = 0

# sum of the squares
for i in range(1, 101):
    sumSquare += i ** 2

# square of the sum
squareSum = ((100 * 101)/2) ** 2

elapsed = (time.time() - start)
print 'elapsed time is', elapsed, 'seconds ~ ', \
    int(elapsed)/60, 'minutes,', \
    int(elapsed)%60, 'seconds,', \
    int((elapsed-(int(elapsed)%60))*1000), 'milliseconds'

print squareSum - sumSquare
