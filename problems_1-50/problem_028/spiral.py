## Code for problem https://projecteuler.net/problem=28

## We form a 1001 grid
## 7 8 9 In this 3x3 matrix, the center (1) is at (0,0)
## 6 1 2 the number 2 is at (1,0), and 9 is at (1,-1) 
## 5 4 3

X = Y = 1001
x = y = 0
dx = 0
dy = -1
dict_grid = {}
n_element = 1
for i in range(max(X, Y)**2):
    if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
        dict_grid[str(x)+','+str(y)] = n_element
        n_element += 1
    if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
        dx, dy = -dy, dx
    x, y = x+dx, y+dy
partial_sum = 0
for i in range(-500, 501):
    partial_sum += dict_grid['{:d},{:d}'.format(i,i)]
    partial_sum += dict_grid['{:d},{:d}'.format(i,-i)]

## The center is summed twice, so we subtract it
partial_sum -= 1

print 'The sum is {:d}'.format(partial_sum)