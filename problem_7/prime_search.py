## Code for problem https://projecteuler.net/problem=7

## Code reused from problem 3
def check_prime(number):
    factor = 2
    while True:
        if factor == number:
            return True
        if number % factor == 0:
            return False
        factor += 1
        
def prime_factors(number_primes):
    ## Quite slow
    guess = 2
    list_primes = []
    while True:
        if check_prime(guess):
            list_primes.append(guess)
        guess += 1
        if len(list_primes) == number_primes:
            break 
    return list_primes

print 'The 10001 prime number is {:d}'.format(prime_factors(10001)[-1])
