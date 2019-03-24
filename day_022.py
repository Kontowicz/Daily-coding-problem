# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
# If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

# recursive, didn't work wery fine. Because it's not tekes into account subwords.

def breakWords(dictionary, str):
    
    if len(str) == 0:
        return
    for i in range(0, len(str)+1):
        if str[0:i] in dictionary:
            print(str[0:i])
            breakWords(dictionary ,str[i::])

# breakWords(['quick', 'brown', 'the', 'fox'], 'thequickbrownfox')
# print()
# breakWords(['bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond')

# Works fine but i'm sure it can be done more efficiently.
def ownApproach(dictionary, str):
    str2 = str
    test = sorted(dictionary, key=len, reverse=True)
    result = []
    for word in test:
        if word in str:
            str = str.replace(word, '')
            result.append(word)
    for final in result:
        str2 = str2.replace(final, ' ' + final + ' ')
    return [x for x in str2.split(' ') if x != '']

print(ownApproach(['bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond'))
print(ownApproach(['quick', 'brown', 'the', 'fox'], 'thequickbrownfox'))