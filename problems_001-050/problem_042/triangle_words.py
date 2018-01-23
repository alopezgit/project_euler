## Code for problem https://projecteuler.net/problem=42

def word_to_value(word):
	return sum(map(lambda x: ord(x) - 96, word))

with open('p042_words.txt') as file:
	words = file.read().lower().replace('"','').split(',')
word_values = map(lambda x: word_to_value(x), words)
largest_value = max(word_values)
triangle_values = []
while True:
	triangle_values.append((len(triangle_values)+1)*(len(triangle_values)+2)/2)
	if triangle_values[-1] > largest_value:
		break
n_triangles = 0
for value in word_values:
	if value in triangle_values:
		n_triangles += 1

print 'The number of coded triangle numbers is {:d}'.format(n_triangles)