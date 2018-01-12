## Code for problem https://projecteuler.net/problem=26
import numpy as np

def check_cycle(d):
    ## The function checks the cycle length
    ## We check the length of unique n when doing
    ## n = 10*n%d where n starts as 1
    ## When n is a number already seen, the cycle starts again
    ## E.g. we start with n = 1 -> 10 % 7 = 3, 30 % 7 = 2, 20 % 7 = 6, 
    ## 60 % 7 = 4, 40 % 7 = 5, 50 % 7 = 1. As we started with 1, the 
    ## number of unique n was 6 ([1,3,2,6,4,5])
    ## The cycle length has to be lower than d
    initial = 1
    list_rems = []
    while True:
        initial *= 10
        dec = initial/d
        initial = initial % d
        if initial in list_rems:
            break
        list_rems.append(initial)
    if list_rems[-1] != 0:
        return len(list_rems)
    else:
        return 0

max_length = 0
for i in range(1, 1000):
    lenght = check_cycle(i)
    if lenght > max_length:
        max_length = lenght
        d = i
print 'The number is {:d}, with a cycle lenght of {:d}'.format(d, max_length)