## Code for problem https://projecteuler.net/problem=49
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils
import itertools
import math
n = 1001
found = False
while True:
	if utils.check_prime(n):
		permutations = set(sorted(list(itertools.permutations(map(int, str(n))))))
		for permutation in permutations:
			## n_2 comes from a permutation of the digits of n
			n_2 = int(''.join(map(str, permutation)))
			## We compute n_3 doing n_3 = n + 2 * k, where k = n_2 - n
			n_3 = int(2*math.fabs(n_2-n)+n)
			## We check if n_3 is a permutation, that n_3>n_2>n and that it is not the given example
			if set(str(n_3)) == set(str(n)) and n_3 > n_2 and n_2 > n and n_3 < 10000 and n != 1487:
				## We also check that they are prime
				if utils.check_prime(n_2) and utils.check_prime(n_3):
					found = True
	n += 2
	if found:
		break
print 'The 12 digit resulting of the concatenation of numbers is {:s}'.format(str(n)+str(n_2)+str(n_3))