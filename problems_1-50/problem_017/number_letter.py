## Code for problem https://projecteuler.net/problem=17

## For number < 20, the names are quite irregular
## Code quite ugly
int_to_letters = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

int_to_letters[0] = ''
int_to_letters[10] = 'ten'
int_to_letters[11] = 'eleven'
int_to_letters[12] = 'twelve'
int_to_letters[13] = 'thirteen'
int_to_letters[14] = 'fourteen'
int_to_letters[15] = 'fifteen'
int_to_letters[16] = 'sixteen'
int_to_letters[17] = 'seventeen'
int_to_letters[18] = 'eighteen'
int_to_letters[19] = 'nineteen'
int_to_letters[20] = 'twenty'
int_to_letters[30] = 'thirty'
int_to_letters[40] = 'forty'
int_to_letters[50] = 'fifty'
int_to_letters[60] = 'sixty'
int_to_letters[70] = 'seventy'
int_to_letters[80] = 'eighty'
int_to_letters[90] = 'ninety'
int_to_letters[100] = 'hundred'
int_to_letters[1000] = 'one thousand'

sum_lenght = 0
for i in range(1, 1000):
    name = ''
    and_var = ''
    ## Check if we have to put the x-hundred
    if i / 100 > 0:
        name = int_to_letters[i / 100] + ' ' + int_to_letters[100]
        ## We put 'and' for extra numbers (e.g. nine hundred and two)
        and_var = ' and '
    ## For values below 20 (but not 0) take from dictionary directly
    if (i % 100) < 20 and (i % 100) > 0:
        name += and_var + int_to_letters[(i % 100)]
    elif (i % 100) != 0:
        name += and_var + int_to_letters[10*((i % 100)/10)]+int_to_letters[int(str(i)[-1])]

    sum_lenght += len(str(name.replace(' ', '')))
    print name
sum_lenght += len(int_to_letters[1000].replace(' ', ''))

print 'The sum of letters is {:d}'.format(sum_lenght)