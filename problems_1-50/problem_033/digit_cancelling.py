## Code for problem https://projecteuler.net/problem=33
from fractions import Fraction

product_fractions = 1
for num in range(10, 100):
    for den in range(num+1, 100):
        intersection = set(str(num)).intersection(set(str(den)))
        ## The number of common digits has to be one (if 2, then the naive simplication is 1, not correct)
        if len(intersection) != 1:
            continue
        intersection = intersection.pop()
        ## Trivial fractions out
        if intersection == '0':
            continue
        ## We find the numerator and denominator "simplifying" the common digits
        num_2 = (str(num).replace(intersection, ''))
        den_2 = (str(den).replace(intersection, ''))
        ## Check some necessary conditions (existance and zero division)
        if len(num_2) and len(den_2) and den_2 != '0':
            den_2 = int(den_2)
            num_2 = int(num_2)
            ## Check if same value
            if 1.0*num_2/den_2 == 1.0*num/den:
                product_fractions*= 1.0*num_2/den_2
                print 'Fraction {:d}/{:d} is equal to {:d}/{:d}'.format(num, den, num_2, den_2)

print 'The denominator is {:d}'.format(Fraction(product_fractions).limit_denominator().denominator)