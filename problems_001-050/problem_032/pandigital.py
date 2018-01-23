## Code for problem https://projecteuler.net/problem=32
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

sum_pandigital = 0

for i in range(1, 10000):
    ## If the number contains any repeated number or 0, skip it
    numbers = set(str(i))
    if len(numbers) != len(str(i)) or '0' in numbers:
        continue
    factors = utils.factors_number(i)
    for multiplicand in factors:
        ## We check if the multiplicand has a 0 or any repeated number
        if '0' in str(multiplicand) or len(set(str(multiplicand))) != len(str(multiplicand)):
            continue
        ## If the numbers in the factor and i are different we do the same for the multiplier
        if not set(str(multiplicand)).intersection(numbers):
            multiplier = i / multiplicand
            ## We check if the multiplier has a 0 or any repeated number
            if '0' in str(multiplier) or len(set(str(multiplier))) != len(str(multiplier)):
                continue
            ## Check if multiplier repeats any number
            if not (set(str(multiplier)).intersection(set(str(multiplicand))) or set(str(multiplier)).intersection(numbers)):
                ## We check if contains all 1-9 digits
                if (len(str(multiplicand)) + len(str(multiplier)) + len(numbers) == 9):
                    print '{:d} x {:d} = {:d}'.format(multiplicand, multiplier, i)
                    sum_pandigital += i 
                    break
                    
print 'The sum is {:d}'.format(sum_pandigital)