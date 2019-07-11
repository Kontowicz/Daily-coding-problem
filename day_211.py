# Given a string and a pattern, find the starting indices
# of all occurrences of the pattern in the string.

def solution(string, pattern):
    string_len = len(string)
    pattern_len = len(pattern)

    to_return = []

    for i in range(0, string_len - pattern_len + 1):
        if string[i:i+pattern_len] == pattern:
            to_return.append(i)
    
    return to_return