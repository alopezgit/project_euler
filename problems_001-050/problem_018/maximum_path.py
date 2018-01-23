## Code for problem https://projecteuler.net/problem=18

with open('input.txt') as file:
    triangle = map(lambda x: map(int, x.strip('\n').split(' ')), file.readlines())

## We start at the bottom and sum the largest value of the two children to the root node
## So if we have
##    3
##   4 6
##  3 5 7
## we do
##  3
## 9 13


while len(triangle) > 1:
    last = triangle.pop()
    pos = 0
    while True:
        triangle[-1][pos] += last[pos] if last[pos] > last[pos+1] else last[pos+1]
        pos += 1
        if pos == len(triangle[-1]):
            break
print 'The maximum path is {:d}'.format(triangle[0][0])