## Code for problem https://projecteuler.net/problem=1

multiples = reduce(lambda x, y: x + (y if ((y % 3 == 0) or (y % 5 == 0)) else 0), range(1000))

print 'The sum of multiples of 3 and 5 below 1000 is {:d}'.format(multiples)