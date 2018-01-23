## Code for problem https://projecteuler.net/problem=45

triangle_values = []
pentagon_values = []
hexagon_values = []

while True:
	triangle_values.append((len(triangle_values)+1)*(len(triangle_values)+2)/2)
	pentagon_values.append((len(pentagon_values)+1)*(3*(len(pentagon_values)+1)-1)/2)
	hexagon_values.append((len(hexagon_values)+1)*(2*(len(hexagon_values)+1)-1))
	## Yep, arbitrary
	if len(triangle_values) > 100000:
		break

## For faster checking if it is in the list
pentagon_values_set = set(pentagon_values)
hexagon_values_set = set(hexagon_values)

for triangular in triangle_values:
	if triangular > 40755 and triangular in pentagon_values_set and triangular in hexagon_values_set:
		break
print 'The next value that is a triangular, pentagonal and hexagonal number is {:d}'.format(triangular)