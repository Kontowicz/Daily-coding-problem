# Given an N by N matrix, rotate it by 90 degrees clockwise.


def solution(array):
    tuples = zip(*array[::-1])

    return [list(item) for item in tuples]

array = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

result = [[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

assert solution(array) == result
print('Test pass.')