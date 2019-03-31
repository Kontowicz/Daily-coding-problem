# Given an integer list where each number represents the number of hops you can make,
# determine whether you can reach to the last index starting at index 0.

def isPossible(arr, begin, end):
    if begin == end:
        return True

    jump = arr[begin]
    if not jump or (begin + jump > end):
        return False

    return isPossible(arr, begin + jump, end)


def reach(arr):
    return isPossible(arr, 0, len(arr) - 1)
