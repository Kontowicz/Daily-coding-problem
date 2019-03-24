# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
def maxSum(array):
    max_so_far = 0
    max_end = 0

    for item in array:
        max_end += item
        if max_end < 0:
            max_end = 0
        if max_so_far < max_end:
            max_so_far = max_end
    
    return max_so_far

print(maxSum([34, -50, 42, 14, -5, 86]))
assert maxSum([34, -50, 42, 14, -5, 86]) == 137
print(maxSum([-5, -1, -8, -9]))
assert maxSum([-5, -1, -8, -9]) == 0