# You are given n numbers as well as n probabilities that sum up to 1. 
# Write a function to generate one of the numbers with its corresponding probability.

# For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], 
# your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

from random import random
import bisect

class probGen:
    def __init__(self, num, prob):
        self.num = num
        self.cummulativeProb = []

        currentCummulativeProb = 0

        for p in prob:
            currentCummulativeProb += p
            self.cummulativeProb.append(currentCummulativeProb)

    def getNumber(self):
        return self.num[bisect.bisect_left(self.cummulativeProb, random())]