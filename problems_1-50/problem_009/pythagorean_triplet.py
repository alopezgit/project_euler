## Code for problem https://projecteuler.net/problem=9


def triplet():
    ## I do not like the nested while/for 
    a = 1
    b = 2
    c = 3
    while True:
        for a in range(1, c-1):
            for b in range(a, c):
                if a**2 + b**2 == c**2 and a + b + c == 1000:
                    return a * b * c
        c += 1

print 'The product of the triplet is {:d}'.format(triplet())