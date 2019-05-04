# Given an array of integers in which two elements appear exactly once and all
# other elements appear exactly twice, find the two elements that appear only once.

# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. 
# The order does not matter.


def solution(array):
    xor = 0
    x = 0
    y = 0
    
    for item in array:
        xor ^= item

    bit = (xor & ~(xor - 1))

    for item in array:
        if item & bit:
            x ^= item
        else:
            y ^= item
    
    return [x, y]

assert solution([2, 4, 6, 8, 10, 2, 6, 10]).sort() == [8, 4].sort()

print('Test pass.')