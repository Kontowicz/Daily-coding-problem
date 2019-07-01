# Write a program that checks whether an integer is a palindrome.
# For example, 121 is a palindrome, as well as 888. 678 is not a
# palindrome. Do not convert the integer into a string.

def solution(value):
    div = 1

    while value / div >= 10:
        div = div * 10

    while value != 0:
        first = value // div
        last = value % 10

        if first != last:
            return False

        value = (value % div) // 10
        div = div / 100

    return True

assert solution(1001) == True
assert solution(201) == False
print('Test pass.')