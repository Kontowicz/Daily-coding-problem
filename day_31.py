# The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions 
# required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three:
# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

def distance(string1, string2):
    s = dict()

    for element in string1:
        if element in s:
            s.update({element: s[element]+1})
        else:
            s.update({element: 1})
    
    toReturn = 0
    for element in string2:
        if element in s:
            s.update({element: s[element]-1})
        else:
            toReturn += 1

    for _, val in s.items():
        if val < 0:
            toReturn += abs(val)
    return toReturn

print(distance('kitten', 'sitting'))
assert distance('kitten', 'sitting') == 3