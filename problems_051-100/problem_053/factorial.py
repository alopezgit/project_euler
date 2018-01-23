## Code for problem https://projecteuler.net/problem=53
import math
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = math.factorial(r)
    return numer//denom

greater_million = 0
for n in range(1, 101):
	for r in range(1, n+1):
		if ncr(n,r) > 1000000:
			greater_million += 1

print 'The number of nCr greater than 1 million is {:d}'.format(greater_million)