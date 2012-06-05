# Project Euler - Problem 2
# http://projecteuler.net/problem=2
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

import time

# fibonacci dictionary used for memoization
fibs = {0:0, 1:1}
# counter that will hold the sum
count = 0
# counter for iterations
n = 1

# fibonacci definition
# based on Dijsktra's paper here: www.cs.utexas.edu/users/EWD/ewd06xx/EWD654.PDF
# love it
def fib(n):
    if n in fibs: return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * fib((n/2) - 1)) + fib(n/2)) * fib(n/2)
        return fibs[n]
    else:
        fibs[n] = (fib((n-1)/2) ** 2) + (fib((n+1)/2) ** 2)
        return fibs[n]

start = time.clock()
while count < 4000000:
    if fib(n) % 2 == 0: # we only want even fibonacci numbers
        count = count + fib(n) # add it to the sum
    n += 1 # increment iteration

elapsed = (time.clock() - start)
print count # print final result
print 'elapsed time is', elapsed, 'seconds ~ ', \
    int(elapsed)/60, 'minutes,', \
    int(elapsed)%60, 'seconds,', \
    int((elapsed-(int(elapsed)%60))*1000), 'milliseconds'
