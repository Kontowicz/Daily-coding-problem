# Given an array of integers, return a new array
# where each element in the new array is the number of
# smaller elements to the right of that element in the original input array.

def solution(array):
    result = []

    for i in range(0, len(array)):
        counter = 0
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                counter += 1
        result.append(counter)

    return result

assert solution([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
print('Test pass.')