## Code for problem https://projecteuler.net/problem=21

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

amicable_sum = 0
for a in range(2, 10000):
    b = sum(filter(lambda x: x!=a, utils.factors_number(a)))
    res = sum(filter(lambda x: x!=b, utils.factors_number(b)))
    if res == a and a != b:
        amicable_sum += a

print 'The sum of amicable numbers under 10000 is {:d}'.format(amicable_sum)