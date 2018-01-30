## Code for problem https://projecteuler.net/problem=58
import math
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )
from utils import utils

## We form a 1001 grid
## 5 4 3 In this 3x3 matrix, the center (1) is at (0,0)
## 6 1 2 the number 2 is at (1,0), and 9 is at (1,-1) 
## 7 8 9

## It takes a while, around 4 min in i7 3.4GHz


x = y = 0
dx, dy = 0, -1

n_element = 1
i = 0

n_checked = 1
n_prime = 0
list_diagonals = []
while True:
    if abs(x) == abs(y):
        list_diagonals.append(n_element)
        if i != 0 and math.sqrt(i+1) % 2 == 1 and math.sqrt(i+1) == int(math.sqrt(i+1)):
            k = int((math.sqrt(i+1)-1)/2)
            for k in range(4):
                if utils.check_prime(list_diagonals.pop()):
                    n_prime += 1
            n_checked += 4
            print n_prime/(1.0*n_checked)
            if n_prime/(1.0*n_checked) < 0.1:
                print 'The side length of the square spiral is {:d}'.format(int(math.sqrt(i+1)))
                break
    n_element += 1
    if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
        dx, dy = -dy, dx
    x, y = x+dx, y+dy

    i+= 1
