## Code for problem https://projecteuler.net/problem=47
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

## Really slow (2 min in a i7). Have to optimize
n = 4
n_consecutive = 0
for n in range(1, 1000000):
	## The function also returns 1 as a prime factor :/ So we need to put 5
	if (not utils.check_prime(n)) and len(utils.prime_factors(n)) == 5:
		n_consecutive += 1
	else:
		n_consecutive = 0
	if n_consecutive == 4:
		break
	if n % 1000 == 0:
		print n
print 'The number is {:d}'.format(n-3)
