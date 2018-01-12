## Code for problem https://projecteuler.net/problem=29

list_combinations = []
for a in range(2, 101):
    for b in range(2, 101):
        list_combinations.append(a**b)

print 'The number of distinct terms is {:d}'.format(len(set(list_combinations)))