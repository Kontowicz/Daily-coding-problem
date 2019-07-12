# Given a column number, return its alphabetical column id.
# For example, given 1, return "A". Given 27, return "AA".

def solution(number):
    to_return = ''

    while number > 0:
        reminder = number % 26

        if reminder == 0:
            to_return += 'Z'
            number = (number // 26) - 1
        else:
            to_return += chr((reminder - 1) + ord('A'))
            number = number // 26

    print(to_return)
    return to_return

assert solution(1) == 'A'
assert  solution(27) == 'AA'