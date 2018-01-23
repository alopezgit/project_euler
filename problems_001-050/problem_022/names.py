## Code for problem https://projecteuler.net/problem=22

with open('p022_names.txt') as file:
    names = file.read().replace('"','').lower().split(',')
total_score = 0
for pos, name in enumerate(sorted(names)):
    total_score+= (pos+1)*sum(map(lambda x: ord(x) - 96, name))

print 'The total name score is {:d}'.format(total_score)