## Code for problem https://projecteuler.net/problem=13

with open('input.txt') as file:
    numbers = map(long, file.readlines())
print 'First 10 digits are {:s}'.format(str(reduce(lambda x, y: x + y, numbers))[:10])
