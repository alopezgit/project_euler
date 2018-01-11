## Code for problem https://projecteuler.net/problem=10
import math
## Code reused from problem 3/7
def check_prime(number, list_primes = []):
    if len(list_primes) == 0:
        list_primes = [2]
    sqrt_number = math.sqrt(number)
    pos = 0
    while True:
        factor = list_primes[pos]
        pos += 1
        if factor > sqrt_number or pos == len(list_primes):
            break
        if number % factor == 0:
            return False
    return True
        
        
def prime_factors(max_value):
    ## Quite slow
    guess = 2
    list_primes = []
    while True:
        if check_prime(guess, list_primes):
            list_primes.append(guess)
        guess += 1
        if guess > max_value:
            break 
    return list_primes

print 'The sum is {:d}'.format(sum(prime_factors(2e6)))