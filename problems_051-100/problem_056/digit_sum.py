## Code for problem https://projecteuler.net/problem=56
max_val = 0
for a in range(100):
    for b in range(100):
        val = reduce(lambda x, y: x+y, map(int, list(str(a**b))))
        if val > max_val:
            max_val = val
            a_large = a
            b_large = b

print 'The largest digit sum is {:d}, with a: {:d} and b: {:d}'.format(max_val, a_large, b_large)
