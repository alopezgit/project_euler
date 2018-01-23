## Code for problem https://projecteuler.net/problem=12

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

natural_number = 1
triangle = 0
while True:
    triangle += natural_number
    natural_number += 1
    factors = utils.factors_number(triangle)
    if len(factors) > 500:
        print 'The number is {:d}'.format(triangle)
        break
