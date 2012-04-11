# sum all multiples of 3 or 5 below 1000
a, b = 1, 0
while a < 1000:
    if ((a % 3 == 0) or (a % 5 == 0)): # if a is multiple or 3 or 5
        b += a # add a to integer responsible for the sum (b)
    a += 1 # let us check next integer
print b # after the while loop, print the sum stored on b
