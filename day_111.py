# Given a word W and a string S, find all starting indices in S which are anagrams of W.
  
def compare(data, data2): 
    for i in range(127): 
        if data[i] != data2[i]: 
            return False
    return True

def find(pattern, text): 
    toReturn = []
    patternSize = len(pattern) 
    textSize = len(text) 

    countPattern = [0]*127
    countTextWindow = [0]*127
  
    for i in range(patternSize): 
        (countPattern[ord(pattern[i]) ]) += 1
        (countTextWindow[ord(text[i]) ]) += 1

    for i in range(patternSize,textSize): 
        if compare(countPattern, countTextWindow): 
            toReturn.append(i-patternSize)

        (countTextWindow[ord(text[i]) ]) += 1
        (countTextWindow[ord(text[i-patternSize]) ]) -= 1

    if compare(countPattern, countTextWindow): 
        toReturn.append(textSize-patternSize)
    
    return toReturn
          
text = "abxaba"
pattern = "ab"       
print(find(pattern, text))