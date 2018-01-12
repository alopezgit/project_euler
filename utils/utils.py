import math

def check_prime(number):
    if (number > 2 and number % 2 == 0) or number < 2:
        return False
    sqrt_number = math.sqrt(number)
    factor = 3
    while True:
        if factor > sqrt_number:
            break
        if number % factor == 0:
            return False
        factor += 2
    return True

def prime_factors(number):
    ## Returns the prime factors of the number
    factor = 2
    list_factors = []
    list_factors.append(1)
    while True:
        if number % factor == 0 and check_prime(factor):
            number /= factor
            list_factors.append(factor)
        else:
            factor += 1
        if number == 1:
            break
    counts = dict()
    for i in list_factors:
      counts[i] = counts.get(i, 0) + 1 
    return counts

def factors_number(n):
    ## Step checks parity (odd numbers do not have even factors)
    step = 2 if n%2 else 1
    ## We check factors up to sqrt(n) using a generator
    return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(pow(n, 0.5))+1, step) if n % i == 0)))

def fibonacci():
    ## A generator for the fibonacci sequence
    last_number = 1
    current_number = 1
    index = 1
    while index < 3:
        yield 1, index
        index += 1
    while True:
        current_number, last_number = current_number + last_number, current_number
        yield current_number, index
        index += 1

def check_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    return False
