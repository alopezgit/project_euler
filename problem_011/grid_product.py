## Code for problem https://projecteuler.net/problem=9
import numpy as np
## Define global variable of adjacent numbers to find
n_adj = 4

## Helper functions
def check_array(array):
    largest = 0
    pos = 0
    while True:
        temp = reduce(lambda x, y: x*y, map(int, list(array[pos:pos+n_adj])))
        if temp > largest:
            largest = temp
        pos += 1
        if pos + n_adj >= len(array):
            return largest

def check_horizontal(grid):
    largest = 0
    for x in range(bounds[0]):
        temp = check_array(grid[x])
        if temp > largest:
            largest = temp
    return largest

def check_vertical(grid):
    largest = 0
    for y in range(bounds[1]):
        temp = check_array(grid[:, y])
        if temp > largest:
            largest = temp
    return largest

def check_diagonal(grid):
    largest = 0
    offset = 0
    while True:
        diagonal = grid.diagonal(offset)
        if len(diagonal) < n_adj:
            break
        temp = check_array(diagonal)
        if temp > largest:
            largest = temp
        diagonal = grid.diagonal(-offset)
        temp = check_array(diagonal)
        if temp > largest:
            largest = temp
        offset+= 1
    return largest

## We form a 20x20 matrix of numbers
with open('input.txt') as file:
    grid = []
    for x, line in enumerate(file):
        y = 0
        grid.append([])
        for number in line.split(' '):
            grid[x].append(int(number.strip('\n')))
            y += 1
    bounds = [x+1, y]

grid =  np.array(grid)

largest = 0

temp = check_horizontal(grid)
if temp > largest:
    largest = temp
temp = check_vertical(grid)
if temp > largest:
    largest = temp
temp = check_diagonal(grid)
if temp > largest:
    largest = temp
## We need to check right to left diagonals too, so we flip the grid
temp = check_diagonal(grid[:,::-1])
if temp > largest:
    largest = temp

print 'The largest value is {:d}'.format(largest)