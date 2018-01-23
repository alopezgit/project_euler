## Code for problem https://projecteuler.net/problem=35

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

n_circular = 0
for i in range(2, 1000000):
    prime = 1
    number = str(i)
    ## Check all rotations
    for pos in range(len(number)):
        prime *= utils.check_prime(int(''.join(number[pos:] + number[:pos])))
        ## If any not prime, break loop
        if not prime:
            break
    if prime:
        n_circular+= 1

print 'The number of circular primes below one million is {:d}'.format(n_circular)
