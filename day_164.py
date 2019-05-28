# You are given an array of length n + 1 whose elements belong to the set
# {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate.
# Find it in linear time and space.

def solution(array, n):
    expectedSum = ((1 + (1*n))*n) / 2
    valueSum = sum(array)

    return abs(expectedSum - valueSum)