# Given two strings A and B, return whether or not A can be shifted some number of times to get B.

def isRotated(first, second):
    return len(first) == len(second) and first in second * 2

print('Target: {} Input string: {}'.format('abcde', 'cdeab'))
print('Result: {}'.format(isRotated('abcde', 'cdeab')))
assert isRotated('abcde', 'cdeab')

print('Target: {} Input string: {}'.format('abc', 'acb'))
print('Result: {}'.format(isRotated('abc', 'acb')))
assert not isRotated('abc', 'acb')