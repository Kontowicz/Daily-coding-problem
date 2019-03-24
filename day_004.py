# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def first_approach(array):
    max_value = max(array)
    
    if max_value < 1:
        return 1
    elif array[0] == 1:
        return 2
    
    new_arr = [0] * max_value
    
    for i in array:
        if i > 0:
            if new_arr[i-1] != 1:
                new_arr[i-1] = 1
    for i in range(0, len(new_arr)):
        if new_arr[i] == 0:
            return i + 1
    
    # This mean all value between 1 and m are in new_arr
    return -1

assert first_approach([3, 4, -1, 1]) == 2
assert first_approach([1, 2, 0]) == 2