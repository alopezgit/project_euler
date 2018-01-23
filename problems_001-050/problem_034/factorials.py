## Code for problem https://projecteuler.net/problem=34
import math
## As 7*9! contains 7 digits, we put the upper limit there 
factorial_sum = 0
for i in range(3, math.factorial(9)*7):
    if sum(map(lambda x: math.factorial(int(x)), str(i))) == i:
        factorial_sum += i

print 'The sum is {:d}'.format(factorial_sum)
