# Given a string, determine whether any permutation of it is a palindrome.

# For example, carrace should return true, since it can be rearranged 
# to form racecar, which is a palindrome. daily should return false, 
# since there's no rearrangement that can form a palindrome.

from collections import Counter

def solution(word):
    cnt = Counter(word)
    
    oddCounter = 0

    for key, value in cnt.items():
        if value % 2 == 1:
            oddCounter += 1

    return oddCounter <= 1

print(solution('carrace'))
print(solution('daily'))