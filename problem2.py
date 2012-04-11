# fibonacci dictionary used for memoization
fibs = {0:0, 1:1}
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
# counter that will hold the sum
count = 0
# counter for iterations
n = 1
while count < 4000000:
    if fib(n) % 2 == 0: # we only want even fibonacci numbers
        count = count + fib(n) # add it to the sum
    n = n + 1 # increment iteration
print count # print final result
