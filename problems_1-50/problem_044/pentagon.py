## Code for problem https://projecteuler.net/problem=44

## We generate the triangle numbers up to 10e7 (arbitrary)
largest_value = 100000000
pentagon_values = []
while True:
	pentagon_values.append((len(pentagon_values)+1)*(3*(len(pentagon_values)+1)-1)/2)
	if pentagon_values[-1] > largest_value:
		break

## For large lists constructing a set is faster if 
## we want to check if an element is in the list
pentagon_values_set = set(pentagon_values)
min_val = 1e10
## Double loop :( to check differences
for k, element in enumerate(pentagon_values):
	for j in xrange(k+1, len(pentagon_values)):
		element_2 = pentagon_values[j]
		D = (element_2-element)
		if D > min_val:
			break
		## Check that sum and differences in the set
		if element+element_2 in pentagon_values_set and D in pentagon_values_set:
			min_val = D
			triangle_j = element 
			triangle_k = element_2

## Quite arbitrary the triangle numbers checked, but it is correct
print 'The minimum distance found is {:d} for triangle numbers {:d} and {:d}'.format(min_val, triangle_j, triangle_k)