## Code for problem https://projecteuler.net/problem=14

def collatz(n):
    chain = []
    chain.append(n)
    while  True:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        chain.append(n)
        if n == 1:
            return chain

max_length = 0 
for i in range(2, int(1e6)):
    length = len(collatz(i))
    if length > max_length:
        max_length = length
        number = i

print '{:d} produces the longest chain'.format(number)