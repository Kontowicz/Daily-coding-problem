# Given an array and a number k that's smaller than the length of
# the array, rotate the array to the right k elements in-place.

def solution(array, k):
    tmp = array[len(array)-k:len(array)]
    return tmp + array[0:k+1]

arr = [1, 2, 3, 4, 5]
assert solution(arr, 2) ==  [4, 5, 1, 2, 3]