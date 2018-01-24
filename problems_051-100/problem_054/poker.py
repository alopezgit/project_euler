import collections
import operator

def replace_letters_to_value(string):
    ## Replaces the ten, jack, queen, king and ace symbols to numbers
    ## and also converts strings to values
    ## when given a card in the form "QD" returns [12, "D"]
    mapping = {'T':'10', 'J':'11', 'Q':'12', 'K':'13', 'A':'14'}
    string = list(string)
    for k, v in mapping.iteritems():
        string[0] = string[0].replace(k, v)
    string[0] = int(string[0])

    return string

with open('p054_poker.txt') as file:
    ## Read data
    hands = map(lambda x: map(lambda y: replace_letters_to_value(y), x.strip().split(' ')), file.readlines())


def check_hand(hand):
    ## This function returns the value of the hand, and the sorted values
    ## value_hand is in the form of X.Y, where X is defined as follows:
    ## 1 high card, 2 pair, 3 two pairs, 4 three of a kind, 5 straight
    ## 6 flush, 7 full house, 8 four of a kind, 9 straight flush
    ## and Y depends on the value of the cards that form the pairs/three/fours of a kind
    ## So the hand [2, 2, 10, 10, 4], will have value 3.1002, as it is formed by two pairs
    ## where the larger pair is formed by 10s and the lowest by 2s
    hand = sorted(hand)
    values = map(lambda x: x[0], hand)
    suits = map(lambda x: x[1], hand)
    flush = True if len(set(suits)) == 1 else False
    counts = collections.Counter(values).most_common()
    straight = sorted(values) == range(min(values), max(values)+1)
    if flush and straight:
        value_hand = 9
    elif counts[0][1] == 4:
        value_hand = float('8.'+str(counts[0][0]).zfill(2) )
    elif counts[0][1] == 3 and counts[1][1] == 2:
        value_hand = float('7.'+str(counts[0][0]).zfill(2) )
    elif flush:
        value_hand = 6
    elif straight:
        value_hand = 5
    elif counts[0][1] == 3:
        value_hand = float('4.'+str(counts[0][0]).zfill(2) )
    elif counts[0][1] == 2 and counts[1][1] == 2:
        pair_1 = max(counts[0][0], counts[1][0])
        pair_2 = min(counts[0][0], counts[1][0])
        value_hand = float('3.'+str(pair_1).zfill(2) +str(pair_2).zfill(2) )
    elif counts[0][1] == 2:
        value_hand = float('2.'+str(counts[0][0]).zfill(2) )
    elif len(counts) == 5:
        value_hand = 1
    return value_hand, values

wins = [0, 0]
for pair_hand in hands:
    ## Check hand by hand
    value_hand_p1, values_p1 = check_hand(pair_hand[:5])
    value_hand_p2, values_p2 = check_hand(pair_hand[5:])
    if value_hand_p1 > value_hand_p2:
        wins[0] += 1
    elif value_hand_p1 < value_hand_p2:
        wins[1] += 1
    else:
        ## In the case of same value, check highest card not repeated
        for i in range(1, 6):
            if values_p1[-i] > values_p2[-i]:
                wins[0] += 1
                break
            elif values_p1[-i] < values_p2[-i]:
                wins[1] += 1
                break



print 'Player one wins {:d} hands'.format(wins[0])