# Given a string, find the palindrome that can be made by inserting the fewest 
# number of characters as possible anywhere in the word. If there is more than 
# one palindrome of minimum length that can be made, return the lexicographically 
# earliest one (the first one alphabetically).

def findMinimum(string):
    return findMinimumR(string, 0, len(string)-1)

def findMinimumR(string, l, h):
    if l>h:
        return 
    if l == h:
        return 0
    if l == h - 1:
        if string[l] == string[h]:
            return 0
        return 1
    
    if string[l] == string[h]:
        return findMinimumR(string, l+1, h - 1)
    return min(findMinimumR(string, l, h - 1), findMinimumR(string, l+1, h))+1

print(findMinimum('race'))