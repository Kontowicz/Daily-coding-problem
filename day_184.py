# Given n numbers, find the greatest common denominator between them.
#
# For example, given the numbers [42, 56, 14], return 14.

def denominator(x, y):
    while y:
        x, y = y, x % y

    return x

def solution(array):
    toReturn = denominator(array[0], array[1])
    for i in range(2, len(array)):
        toReturn = denominator(toReturn, array[i])

    return toReturn

assert solution([42, 56, 14]) == 14
