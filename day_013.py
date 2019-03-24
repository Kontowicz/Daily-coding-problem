# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def isValid(string, k):
    return len(''.join(set(string))) <= k

def find(string, k):
    left = 0
    right = 1
    distance = []
    while right < len(string):
        if isValid(string[left:right], k) == True:
            distance.append([right - left, string[left:right]])
            right += 1
        else :
            distance.append([right - left, string[left:right]])
            left += 1
            right += 1
            

    return max(distance)

print(find('abcba', 2))
        
