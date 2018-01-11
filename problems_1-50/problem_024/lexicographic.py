## Code for problem https://projecteuler.net/problem=24
import itertools

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation = ''.join(map(str, sorted(list(itertools.permutations(elements)))[999999]))
print 'The permutation is {:s}'.format(permutation)

