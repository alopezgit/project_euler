## Code for problem https://projecteuler.net/problem=38

for i in range(1, 10000):
    ## If the number contains any repeated number or 0, skip it
    number_string = str(i)
    digits = set(number_string)
    if len(digits) != len(number_string) or '0' in digits:
        continue
    n = 2
    while True:
        number_string += str(i*n)
        if '0' in number_string or len(number_string) != len(set(number_string)):
            break
        if len(number_string) == 9: 
            ## The largest one has to be the last one found
            largest_pandigital = int(number_string)

print 'The largest pandigital is {:d}'.format(largest_pandigital)