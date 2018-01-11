## Code for problem https://projecteuler.net/problem=2

def fibonacci(limit):
    ## Computes the fibonacci sequence until the last 
    ## value is higher than limit (value not included in output)
    value = 1
    list_values = []
    list_values.append(value)
    list_values.append(value)
    while True:
        value += list_values[-2]
        if value > limit:
            break
        list_values.append(value)
    list_values.pop(0)
    return list_values

print 'The sum is {:d}'.format(reduce(lambda x,y: x + (y if y % 2 == 0 else 0), [0] + fibonacci(4e6)))