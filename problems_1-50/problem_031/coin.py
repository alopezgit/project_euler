## Code for problem https://projecteuler.net/problem=31

## Idea from https://www.vitoshacademy.com/python-algorithms-maximum-combinations-of-coins/

target = 200
coin_values = [1,2,5,10,20,50,100,200]
values_comb = [0]*(target+1)
 
for coin in coin_values:
    for i in range(coin, target+1):
        if coin == i:
            values_comb[i]+=1
        else:
            values_comb[i]=(values_comb[i]+values_comb[i-coin])
 
print 'The number of possible combinations is {:d}'.format(values_comb[target])