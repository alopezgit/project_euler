## Code for problem https://projecteuler.net/problem=37

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

def truncatable_prime(n):
    n = str(n)
    prime = True
    for i in range(len(n)):
        prime *= utils.check_prime(int(n[i:])) * utils.check_prime(int(n[:i+1])) 
        if not prime:
            break
    return prime

n_primes = 0
n = 10
sum_primes = 0
## The problem says that there are only 11 truncatable primes
while n_primes < 11:
    if truncatable_prime(n):
        n_primes += 1
        print 'New truncatable prime found: {:d}'.format(n)
        sum_primes += n
    n += 1

print 'The sum of primes is {:d}'.format(sum_primes)