# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.


def max_subse(arr):
    exclu = 0
    inclu = arr[0]

    for i in range(1, len(arr)):
        tmp = inclu
        inclu = max(exclu + arr[i], inclu)
        exclu = tmp
    return inclu

assert max_subse([2, 4, 6, 2, 5]) == 13
assert max_subse([5, 1, 1, 5]) == 10