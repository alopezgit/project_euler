## Code for problem https://projecteuler.net/problem=46
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

## We compute some primes first
list_primes = []
for i in range(100000):
	if utils.check_prime(i):
		list_primes.append(i)

conjecture = True
number = 1
while True:
	number += 2
	## Check if the number is odd composite
	if not utils.check_prime(number):
		conjecture = False
		## We search for a composition of prime + k*n**2
		for prime in list_primes:
			if prime > number:
				break
			if pow((number - prime)/2, 0.5).is_integer():
				conjecture = True
	## Break when the conjecture does not hold
	if conjecture == False:
		break
print 'The conjecture fails at {:d}'.format(number)
