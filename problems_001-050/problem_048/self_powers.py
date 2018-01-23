## Code for problem https://projecteuler.net/problem=48
sum_powers = 0
for i in range(1, 1001):
	sum_powers += pow(i, i)

print 'The last 10 digits of the sum are {:s}'.format(str(sum_powers)[-10:])