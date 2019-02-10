# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, 
# write a function that shuffles a deck of cards represented as an array using only swaps

import random

def shuffle(array):
    for i in range(0, len(array)):
        pos = random.randint(0, len(array))%len(array)
        array[i], array[pos] = array[pos], array[i]
    return array

test_arr = []
for i in range(0, 20):
    test_arr.append(i)
print(shuffle(test_arr))