# Given an array of numbers, find the length of the longest increasing subsequence in the array.
# The subsequence does not necessarily have to be contiguous.
# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
# the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

def longest(array):
    values = [1] * len(array)

    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j]:
                values[i] = max(values[i], values[j] + 1)
    return max(values)

print(longest([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
        