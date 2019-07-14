# Given a string, return whether it represents a number.
# Here are the different kinds of numbers:

def solution(number):
    import re
    pattern = '[+\-]?\d+[e|\.?\d+]?'
    return re.match(pattern, number)

assert solution("10")
assert solution("-10")
assert solution("10.1")
assert solution("-10.1")
assert solution("1e5")
assert solution("-5")
assert solution("1e-5")
assert solution("1e-5.2")
assert not solution("a")
assert not solution("x 1")
assert not solution("a -2")
assert not solution("-")
print('Test pass')