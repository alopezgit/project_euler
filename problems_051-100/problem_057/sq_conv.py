## Code for problem https://projecteuler.net/problem=57
import numpy as np
from fractions import Fraction

## If we do it with floats and then convert to fractions, the precision
## is not enough to find the correct fraction
## So we do it recursively but we do not simplify numerator/denominator
def recursive_exp(n_iter):
    numerator = 5
    denominator = 2
    for i in range(n_iter-1):
        numerator, denominator = numerator * 2 + denominator, numerator
    numerator, denominator = denominator + numerator, numerator
    return numerator, denominator

n_found = 0
for i in range(1000):
    if i == 0:
        exp = 1.5
    elif i > 0:
        numerator, denominator = recursive_exp(i)
        if len(str(numerator)) > len(str(denominator)):
            n_found += 1


print 'The n. of expansions of sqrt(2) where the numerator has more digits than the denominator is {:d}'.format(n_found)