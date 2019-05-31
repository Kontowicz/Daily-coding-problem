# Given a list of words, find all pairs of unique indices such
# that the concatenation of the two words is a palindrome.
#
# For example, given the list ["code", "edoc", "da", "d"],
# return [(0, 1), (1, 0), (2, 3)].

def isPalindrome(word):
    return word == word[::-1]

def solution(words):
    toReturn = []

    for i, word_i in enumerate(words):
        for j, word_j in enumerate(words):
            if i != j:
                newWord = word_i + word_j
                if isPalindrome(newWord):
                    toReturn.append((i, j))

    return toReturn

assert solution(["code", "edoc", "da", "d"]) == [(0, 1), (1, 0), (2, 3)]
print('Test pass.')