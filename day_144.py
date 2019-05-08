# Given an array of numbers and an index i, 
# return the index of the nearest larger number 
# of the number at index i, where distance is 
# measured in array indices.

# For example, given [4, 1, 3, 5, 6] 
# and index 0, you should return 3.

def solution(array, index):
    # Search left
    left = index - 1
    tmp = []
    for i in range(left, -1 , -1):
        if array[i] > array[index]:
            tmp.append(abs(index - i))

    # Search right 
    right = index + 1
    for i in range(right, len(array)):
        if array[i] > array[index]:
            tmp.append(abs(index - i))

    if tmp = []:
        return None
        
    return min(tmp)

print(solution([4, 1, 3, 5, 6], 0))