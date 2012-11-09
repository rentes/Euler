# Project Euler - Problem 1
# http://projecteuler.net/problem=1
# Add all the natural numbers below one thousand that are multiples of 3 or 5.

import time

start = time.time()
# sum all multiples of 3 or 5 below 1000
a, b = 1, 0
while a < 1000:
    if ((a % 3 == 0) or (a % 5 == 0)): # if a is multiple or 3 or 5
        b += a # add a to integer responsible for the sum (b)
    a += 1 # let us check next integer

elapsed = (time.time() - start)
print b # after the while loop, print the sum stored on b
print 'elapsed time is', elapsed, 'seconds ~ ', \
    int(elapsed)/60, 'minutes,', \
    int(elapsed)%60, 'seconds,', \
    int((elapsed-(int(elapsed)%60))*1000), 'milliseconds'
