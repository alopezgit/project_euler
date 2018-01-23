## Code for problem https://projecteuler.net/problem=25

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

generator = utils.fibonacci()

for fibonacci, index in generator:
    if len(str(fibonacci)) == 1000:
        break

print 'The index is {:d}'.format(index)
