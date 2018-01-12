## Code for problem https://projecteuler.net/problem=27

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

max_n = 0
for a in range(-999, 1000):
    for b in range(0, 1001):
        n = 0
        while (n**2+a*n+b > 0 and utils.check_prime(n**2+a*n+b)):
            n += 1
        if n > max_n:
            a_b = a*b
            max_n = n

print 'The multiplications is {:d}'.format(a_b)
            
