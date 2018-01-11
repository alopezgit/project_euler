## Code for problem https://projecteuler.net/problem=5

## Code reused from problem 3
def check_prime(number):
    factor = 2
    while True:
        if factor == number:
            return True
        if number % factor == 0:
            return False
        factor += 1
        
def prime_factors(number):
    factor = 2
    list_factors = []
    while True:
        if number % factor == 0 and check_prime(factor):
            number /= factor
            list_factors.append(factor)
        else:
            factor += 1
        if number == 1:
            break 
    return list_factors


def check_factors(max_factor):
    ## We look for the least common multiple (l.c.m) of [1, max_factor] 
    ## and return the factors of that l.c.m.
    dict_fact = {}
    for factor in range(1, max_factor+1):
        counts = dict()
        for i in prime_factors(factor):
          counts[i] = counts.get(i, 0) + 1
        for key, value in counts.iteritems():
            if key not in dict_fact or value > dict_fact[key]:
                dict_fact[key] = value   
    return dict_fact

max_factor = 20
partial = map(lambda x: x[1]**x[0], [(v, k) for k, v in check_factors(max_factor).iteritems()])
print 'The smallest number found is {:d}'.format(reduce(lambda x, y: x*y, partial))