# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

import random

def getElement(stream):
    element = None

    for i, elem in enumerate(stream):
        if  i == 0: 
            element = 0
        elif random.randint(1, i + 1) == 1:
            element = elem

    return element