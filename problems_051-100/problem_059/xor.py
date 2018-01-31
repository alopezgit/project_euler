## Code for problem https://projecteuler.net/problem=59
import itertools
import enchant
## The dict is used to check if the text contains english words
d = enchant.Dict("en_US")
def decipher_text(cipher, key):
    text = ''
    for i in range(len(cipher)):
        dec_char = cipher[i] ^ key[i%3]
        ## Under 32 and above 126 the ascii characters are not english characters
        if dec_char < 32 or dec_char > 126:
            return False
        text += chr(dec_char)
    return text

with open('p059_cipher.txt') as file:
    cipher = map(int, file.read().strip().split(','))

max_real_words = 0 
## We form all combinations of 3 lowercase characters (ascii from 97 to 122)
for k, key_comb in enumerate(itertools.combinations(range(97,123), 3)):
    ## We form all permutations of the combinations
    for key in itertools.permutations(key_comb):
        text = decipher_text(cipher, key)
        if text:
            ## We check the ratio of actual english words according to the dictionary
            text_list = filter(lambda x: x is not '', text.split(' '))
            real_words = sum([d.check(word) for word in text_list])/(1.0*len(text_list))
            if real_words > max_real_words:
                real_text = text
                max_real_words = real_words
                real_key = key
                ascii_value = sum([ord(c) for c in text])

print real_text
print 'The key was {:d}, {:d}, {:d}'.format(*real_key)
print 'The sum of values is {:d}'.format(ascii_value)
