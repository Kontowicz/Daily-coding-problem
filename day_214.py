# Given an integer n, return the length of the longest
# consecutive run of 1s in its binary representation.

def solution(number):
    counter = 0

    while number > 0:
        number = (number & (number << 1))

        counter += 1

    return counter