# Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less.
# You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.
# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: 
# ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

def div(string, k):
    wordArr = string.split(' ')
    for item in wordArr:
        if len(item)>k:
            return None
    
    toReturn = []    
    
    tmp = wordArr[0]
    i = 1
    while i < len(wordArr):
        if len(tmp) + len(wordArr[i]) + 1 <=k:
            tmp += ' '
            tmp += wordArr[i]
        else:
            toReturn.append(tmp)
            tmp = wordArr[i]
        i+=1
    toReturn.append(tmp)
    return toReturn

print(div( "the quick brown fox jumps over the lazy dog", 10))