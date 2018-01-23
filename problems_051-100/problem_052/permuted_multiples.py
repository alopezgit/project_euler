## Code for problem https://projecteuler.net/problem=52
import collections

check_number = 2
while True:
	found = 1
	for i in range(2, 7):
		if collections.Counter(str(i*check_number)) != collections.Counter(str(check_number)):			
			found = 0
			break
	if found == 1:
		break
	check_number +=1
print 'The answer is {:d}'.format(check_number)