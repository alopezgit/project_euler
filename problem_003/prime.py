## Code for problem https://projecteuler.net/problem=3

def check_prime(number):
    factor = 2
    while True:
        if factor == number:
            return True

        if number % factor == 0:
            return False
        factor += 1
        
def largest_prime_factor(number):
    factor = 2
    while True:
        if number % factor == 0 and check_prime(factor):
            number /= factor
        if number == 1:
            break 
        factor += 1
    return factor

number_check = 600851475143
print 'The largest prime number in {:d} is {:d}'.format(number_check, largest_prime_factor(number_check)) 