# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

import math

def powetSet(array):
    total = (int)(math.pow(2, len(array)))
    cnt = 0
    j = 0
    toReturn = []
    for cnt in range(0, total):
        tmp = []
        for j in range(0, len(array)):
            if (cnt & (1 << j)) > 0:
                tmp.append(array[j])
        toReturn.append(tmp)
    return toReturn
    
print(powetSet([1, 2, 3]))