## Code for problem https://projecteuler.net/problem=6

partial_sum = 0
partial_squared_sum = 0 
max_number = 100
for i in range(max_number + 1):
    partial_sum += i
    partial_squared_sum += i**2

result = partial_sum**2 - partial_squared_sum

print 'The result is {:d}'.format(result)