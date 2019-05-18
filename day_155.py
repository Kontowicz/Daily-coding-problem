# Given a list of elements, find the majority element,
# which appears more than half the time (> floor(len(lst) / 2.0)).
# 
# You can assume that such element exists.
# 
# For example, given [1, 2, 1, 1, 3, 4, 0], return 1.

from math import floor

def solution(array):
    x = floor(len(array) / 2.0)
    
    hist = {}

    for item in array:
        if item not in hist:
            hist[item] = 1
        else:
            hist[item] += 1

    for key, value in hist.items():
        if value >= x:
            return key

arr = [1, 2, 1, 1, 3, 4, 0]
print('Test: {}'.format(arr))
res = solution(arr)
print('Result: {}'.format(res))
assert res == 1
print('Test pass.')