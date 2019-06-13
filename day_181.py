# Given a string, split it into as few strings as possible such that each string is a palindrome.

def is_palindrome(string):
    return string == string[::-1] and string != ''

def solution(string):
    toReturn = []
    pos = []
    while len(string) > 0:
        for i in range(0, len(string) + 1):
            candidate = string[0:i]
            if is_palindrome(candidate):
                pos.append([0, i])

        toReturn.append(string[pos[-1][0]:pos[-1][1]])
        string = string[pos[-1][1]::]

        pos = []

    return toReturn

assert solution("racecarannakayak") == ["racecar", "anna", "kayak"]
assert solution("abc") == ["a", "b", "c"]