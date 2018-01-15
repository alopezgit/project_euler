## Code for problem https://projecteuler.net/problem=43
## It takes a little bit (~20 seconds laptop with i7)
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils
import itertools

def substring_division(number):
	## Checks if follows the property in problem 43
	primes = [2, 3, 5, 7, 11, 13, 17]
	initial = 1 if len(str(number)) == 10 else 0

	for pos in range(initial, 9 - initial):
		if int(str(number)[pos:pos+3]) % primes.pop(0):
			return False

	return True

## We generate all 0 to 9 pandigitals
permutations = sorted(list(itertools.permutations([i for i in range(0, 9 + 1)])))
sum_pandigital = 0
while True:
    if len(permutations) == 0:
    	break
    ## We take a permutation from the list and join it in an integer
    i = int(''.join(map(str, permutations.pop())))
    if substring_division(i):
    	sum_pandigital += i

print 'The sum is {:d}'.format(sum_pandigital)
