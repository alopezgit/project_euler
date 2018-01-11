## Code for problem https://projecteuler.net/problem=15
import math
## I will leave the function here, it is really slow, so I could not use it for 20x20
## But it works I think, it needs to be optimized.
def recursive_path(x, y, n_finish = 0, grid_size = 2):
    if x < grid_size:
        n_finish = recursive_path(x+1, y, n_finish, grid_size)
    if y < grid_size:
        n_finish = recursive_path(x, y+1, n_finish, grid_size)
    if x == grid_size and y == grid_size:
        return n_finish + 1
    else:
        return n_finish

## The number of paths is the permutation with repetition of two sets with n elements
## where n is the length of one side. We have to perform 2n turns to reach the end
## where n of those turns will be right and the other n will be down.
grid_size = 20
turns = math.factorial(2*grid_size)/(math.factorial(grid_size)**2)
print 'The number of paths is {:d}'.format(turns)