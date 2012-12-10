'''
Project Euler - Problem 3
http://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import time

def multiplyFactors(l):
    '''
    Multiplies discovered prime factors of n
    Returns: int
    '''
    v = 1
    for x in l:
        v *= x
    return v

def factors(n):
    '''
    This function does the following to solve this problem:
    1 - discover all prime factors of n
    2 - as we discover new factors, multiply them all to see if they equal n
    3 - if they equal n, we found all factors and only need to obtain the max
    4 - if not equal to n, continue search for factors until reaching n
    '''
    # list with prime factors of number n
    l = []
    # first number to divide n
    m = 2
    # while all factors multiplied don't equal n and m is not n yet
    while n != multiplyFactors(l) and m < n:
        if n % m == 0:
            # variable to control if a factor is a multiple of the already
            # discovered ones on the list, e.g., is a prime or not
            divisors = 0
            if len(l) != 0:
                for x in l:
                    if m % x == 0:
                        divisors += 1
                        break
                # factor has no multiples yet, hence is prime!
                if divisors == 0:
                    # prime factor found. let's add it to the list
                    l.append(m)
                    # sort the list for easy retrieval of last element
                    l.sort()
            else:
                l.append(m)
        # continue factor search
        m += 1
    # comment next line if you don't want to see list of discovered factors
    print (l)
    return l

start = time.time()
# print the last value of list of factors (we sorted the list)
print (factors(600851475143)[-1])
elapsed = (time.time() - start)
print ('elapsed time is', elapsed, 'seconds ~', \
    int(elapsed/60), 'minutes,', \
    int(elapsed)%60, 'seconds,', \
    int(elapsed*1000)-((int(elapsed)%60)*1000), 'milliseconds')
