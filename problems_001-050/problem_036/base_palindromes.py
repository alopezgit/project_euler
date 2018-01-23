## Code for problem https://projecteuler.net/problem=36

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

sum_palindromes = 0
for i in range(1, 1000000):

    if utils.check_palindrome(i) and utils.check_palindrome("{0:b}".format(i)):
        sum_palindromes += i

print 'The sum of double base palindromes is {:d}'.format(sum_palindromes)