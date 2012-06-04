# Project Euler - Problem 5
# http://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

import time

nr = 2

def divideEvenly(n):
    divide = False
    if n % 20 == 0 and n % 19 == 0 and n % 18 == 0 and n % 17 == 0 and n % 16 == 0 and n % 15 == 0 and n % 14 == 0 and n % 13 == 0 and n % 11 == 0:
        divide = True
    return divide

start = time.clock()
while nr > 0:
    if divideEvenly(nr):
        break
    else:
        if nr == 2:
            nr += 8
        else:
            nr += 10 
elapsed = (time.clock() - start)
print nr
print 'elapsed time is', elapsed, 'seconds ~ ', int(elapsed)/60, 'minutes,', int(elapsed)%60, 'seconds,', int((elapsed-(int(elapsed)%60))*1000), 'milliseconds'
