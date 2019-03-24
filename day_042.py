# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
# Integers can appear more than once in the list. You may assume all numbers in the list are positive.
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

def isSubset(array, size, sum_val, sub):
    if sum_val == 0:
        return sub
    if size == 0 and sum_val != 0: 
        return False
    
    if array[size - 1] > sum_val:
        return isSubset(array, size - 1, sum_val, sub)
    
    return isSubset(array, size - 1, sum_val, sub) or isSubset(array, size - 1, sum_val - array[size - 1], sub + [array[size - 1]])

def find(array, targetValue):
    return isSubset(array, len(array), targetValue, [])
print('Test')
print('Array: [12, 1, 61, 5, 9, 2]')
print('Value: 24')
print('Expected subset: [12, 9, 2, 1]')
print('Outupt', find([12, 1, 61, 5, 9, 2] , 24))
assert sorted(find([12, 1, 61, 5, 9, 2] , 24)) == sorted([12, 9, 2, 1])
print('Test ok')

