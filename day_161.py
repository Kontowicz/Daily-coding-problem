# Given a 32-bit integer, return the number with its bits reversed.

def solution(number):
    reverse = 0

    while number > 0:
        reverse = reverse << 1

        if number & 1 == 1:
            reverse = reverse ^ 1

        number = number >> 1

    return  reverse

