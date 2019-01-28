# Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.
# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

def isPaindrom(string):
    return string == string[::-1]

def longestPalindromicSubstring(string):
    substring = []
    for i in range(0, len(string)+1):
        for j in range(i + 1, len(string) + 1):
            if isPaindrom(string[i:j]) == True:
                substring.append(string[i:j])
    return max(substring, key = len)

print(longestPalindromicSubstring('aabcdcb'))