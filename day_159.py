# Given a string, return the first recurring
# character in it, or null if there is
# no recurring character.

def solution(sentence):
    occurence = {}

    for char in sentence:
        if char not in occurence:
            occurence[char] = 1
        else:
            return char

    return None

assert solution('acbbac') == 'b'
assert solution('abcdef') == None
