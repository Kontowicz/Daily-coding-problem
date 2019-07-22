# Given a sorted array, find the smallest positive integer
# that is not the sum of a subset of the array.

def solution(array):
    to_return = 1
    for number in array:
        if number > to_return:
            break
        to_return += number

    return to_return