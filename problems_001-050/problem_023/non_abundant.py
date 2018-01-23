## Code for problem https://projecteuler.net/problem=23
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils
import itertools

a = 28
list_abundant = []
for a in range(1, 28123):
    if sum(filter(lambda x: x!=a, utils.factors_number(a))) > a:
        list_abundant.append(a)

## We compute the cartesian product of the abundant set (https://en.wikipedia.org/wiki/Cartesian_product)
## And keep track of the possible numbers that their sum can generate
dict_sum = {}
for subset in itertools.product(list_abundant, repeat=2):
    if sum(subset) not in dict_sum:
        dict_sum[sum(subset)] = 1
partial_sum = 0
for i in range(28123):
    if i not in dict_sum:
        partial_sum += i
print 'The sum is {:d}'.format(partial_sum)
