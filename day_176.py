# Determine whether there exists a one-to-one character mapping
# from one string s1 to another s2.
#
# For example, given s1 = abc and s2 = bcd, return true
# since we can map a to b, b to c, and c to d.
#
# Given s1 = foo and s2 = bar, return false since
# the o cannot map to two characters.

def solution(s1, s2):
    if len(s1) != len(s2):
        return False

    map = {}
    for character1, character2 in zip(s1, s2):
        if character1 not in map:
            map[character1] = character2
        elif map[character1] != character2:
            return False

    return True

assert solution("abc", "bcd")
assert not solution("foo", "bar")
print('Test pass.')