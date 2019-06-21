# You are given an array of nonnegative integers. Let's say you start at
# the beginning of the array and are trying to advance to the end. You
# can advance at most, the number of steps that you're currently on.
# Determine whether you can get to the end of the array.

def solution(array):
    if len(array) < 2:
        return True

    for i in range(2, len(array)):
        if array[len(array) - 1] >= i - 1:
            return solution(array[:len(array) - i - 1])

assert solution([1, 3, 1, 2, 0, 1])
assert not solution([1, 2, 1, 0, 0])
print('Test pass.')