## Code for problem https://projecteuler.net/problem=55

def check_lychrel(number):
    for iteration in range(50):
        number = number + int(str(number)[::-1])
        if str(number) == str(number)[::-1]:
            return False

    return True

n_lychrel = 0
for n in range(1, 10000):
    n_lychrel += check_lychrel(n)

print 'The number of lychrel numbers is {:d}'.format(n_lychrel)