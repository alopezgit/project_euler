## Code for problem https://projecteuler.net/problem=4

def check_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    return False

def largest_palindrome():
    ## Tries two different 3-digit numbers and finds largest palindrome
    ## Tries all values of factor_1 and factor_2 (100, 999), not optimal
    factor_1 = factor_2 = 999
    largest_value = (0, 0, 0)
    while True:
        if factor_1 * factor_2 > largest_value[0] and check_palindrome(factor_1 * factor_2):
            largest_value = (factor_1 * factor_2, factor_1, factor_2)
        factor_1 -= 1
        if factor_1 == 100:
            factor_2 -= 1
            factor_1 = 999
        if factor_2 == 100:
            return largest_value

print largest_palindrome()
