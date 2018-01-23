## Code for problem https://projecteuler.net/problem=41
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils
import itertools

## We generate all pandigital numbers using permutations
## First we start with 9-pandigitals
permutations = []
n_pandigital = 9
while True:
    ## If no permutations left, we generate more pandigital numbers
    if len(permutations) == 0:
        permutations = sorted(list(itertools.permutations([i for i in range(1, n_pandigital + 1)])))
        ## Next iterations of permutations will have a digit less (e.g. from 1 to 9, then 1 to 8, etc)
        n_pandigital -= 1
    ## We take a permutation from the list and join it in an integer
    i = int(''.join(map(str, permutations.pop())))
    ## If the number is a prime, we finish as the numbers are in a decreasing order,
    ## so the first found is the largest one
    if utils.check_prime(i):
        prime_pandigital = i
        print 'The largest pandigital prime is {:d}'.format(i)
        break