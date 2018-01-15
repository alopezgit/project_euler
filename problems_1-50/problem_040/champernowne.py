## Code for problem https://projecteuler.net/problem=40
## Initialize variables: refers to d_n, n_digits keeps track 
## of the number of fractional digits, i is the current number
multiplication_digits = 1
next_digit = 10
i = n_digits = 0
while True:
	i+= 1
	## We check if the number contains any of the d_n we are looking for
	if (n_digits + len(str(i))) > next_digit:
		multiplication_digits *= int(str(i)[next_digit - n_digits - 1])
		## d_n are 10, 100, 1000... powers of 10.
		next_digit *= 10
	if next_digit > 1000000:
		break
	n_digits += len(str(i))

print 'The multiplication is {:d}'.format(multiplication_digits)