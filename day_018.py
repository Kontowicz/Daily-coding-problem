# Given an array of integers and a number k, where 1 <= k <= length 
# of the array, compute 
# the maximum values of each subarray of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
# we should get: [10, 7, 8, 8]

from collections import deque

def getMax(arr, k):
    result = []
    Q = deque()
    for i in range(k):
        while Q and arr[i] >= arr[Q[-1]]:
            Q.pop()
        Q.append(i)

    for i in range(k, len(arr)):
        result.append(arr[Q[0]])
        while Q and Q[0] <= i - k:
            Q.popleft()

        while Q and arr[i] >= arr[Q[-1]]:
            Q.pop()
        Q.append(i)

    result.append(arr[Q[0]])
    return result

print(getMax([10, 5, 2, 7, 8, 7], 3))