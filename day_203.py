# Suppose an array sorted in ascending order is rotated at some
# pivot unknown to you beforehand. Find the minimum element in
# O(log N) time. You may assume the array does not contain duplicates.

def solution_helper(array, start, stop):
    pivot = start + ((stop - start) // 2)

    if array[start] <= array[pivot]:
        if array[stop] < array[pivot]:
            return solution_helper(array, pivot + 1, stop)
        else:
            return array[start]
    elif array[start] >= array[pivot]:
        if array[stop] > array[pivot]:
            return solution_helper(array, start, stop)
        else:
            return array[stop]


def solution(array):
    return solution_helper(array, 0, len(array) - 1)

assert solution([5, 7, 10, 3, 4]) == 3
print('Test pass.')