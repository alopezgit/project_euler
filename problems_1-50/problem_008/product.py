## Code for problem https://projecteuler.net/problem=8

with open('input.txt', 'r') as file:
    digits = file.read().replace('\n','')
    
pos = 0
n_adj = 13
largest = 0
while True:
    temp = reduce(lambda x, y: x*y, map(int, list(digits[pos:pos+n_adj])))
    if temp > largest:
        largest = temp
    pos += 1
    if pos + n_adj == len(digits):
        break

print 'The largest number is {:d}'.format(largest)