## Code for problem https://projecteuler.net/problem=30

## The largest sum for 5 digits is 5*9**5.
## The number cannot have six digits as 5*9**6 < 100000
partial_sum = 0
for i in range(2, 5*9**5):
    if sum(map(lambda x: int(x)**5, str(i))) == i:
        partial_sum += i
        print 'Number found {:d}'.format(i)

print 'The sum of the numbers found is {:d}'.format(partial_sum)