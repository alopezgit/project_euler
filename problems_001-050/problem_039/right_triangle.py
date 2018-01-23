## Code for problem https://projecteuler.net/problem=39

def check_possible_sides(p):
    ## Checks all integers a,b,c, where c>=b>=a
    ## so that a+b+c = p and a**2+b**2=c**2
    n_solutions = 0
    for a in range(1, p):
        for b in range(a, p-2*a):
            c = p - (a + b)
            if c < b:
                break
            if a**2 + b**2 == c**2:
                n_solutions += 1
    return n_solutions

largest_n_sol = 0
for p in range(3, 1001):
    tmp_sol = check_possible_sides(p)
    if tmp_sol > largest_n_sol:
        optimal_p = p
        largest_n_sol = tmp_sol
print 'The p with more possible solutions is {:d}'.format(optimal_p)