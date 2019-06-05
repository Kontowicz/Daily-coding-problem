# Given a string s and a list of words words, where each
# word is the same length, find all starting indices of
# substrings in s that is a concatenation of every word in words exactly once.

from itertools import permutations

def solution(string, words):
    wordsPermutation = list(permutations(words))
    wordsPermutation = [ x + y for (x, y) in wordsPermutation]

    positions = [string.find(x) for x in wordsPermutation]
    positions = [x for x in positions if x >= 0]
    return sorted(positions)

print(solution("dogcatcatcodecatdog", ["cat", "dog"]))