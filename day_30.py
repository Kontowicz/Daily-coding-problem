# You are given an array of non-negative integers that represents a two-dimensional elevation
# map where each element is unit-width wall and the integer is the height. 
# Suppose it will rain and all spots between two walls get filled up.
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

def water(array):
    left = [0]*len(array)
    right = [0]*len(array)
    water = 0

    left[0] = array[0]
    for i in range(1, len(array)):
        left[i] = max(left[i-1], array[i])
    
    right[len(array) - 1] = array[len(array) - 1]
    for i in range(len(array) - 2, -1, -1):
        right[i] = max(right[i+1], array[i])
    
    for i in range(0, len(array)):
        water += min(left[i], right[i] - array[i])
    return water

print(water([2, 1, 2]))
print(water([3, 0, 1, 3, 0, 5]))