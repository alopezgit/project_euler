## Code for problem https://projecteuler.net/problem=50
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils


## We know that 953 contains 21 terms, so the largest prime < 1e6/21
list_primes = []
for i in range(2, 50000):
	if utils.check_prime(i):	
		list_primes.append(i)

n_max = 1
for pos in range(len(list_primes)):
	n_pos = n_max + 1
	## When this is true, we already found the answer as 
	## we iterate in increasing order of primes
	if sum(list_primes[pos:pos+n_max]) > 1000000:
		break
	while True:
		a = sum(list_primes[pos:pos+n_pos])
		## The number we are looking for has to be < 1000000
		if a > 1000000:
			break
		## We check if it is a prime number
		if utils.check_prime(a):
			n_max = n_pos
			prime_found = a
		n_pos += 1

print 'The prime found is {:d}'.format(prime_found)


