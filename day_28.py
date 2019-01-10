# Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
# More specifically, you should have as many words as possible in each line. There should be at least one space between each word. 
# Pad extra spaces when necessary so that each line has exactly length k.
# Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
# Each word is guaranteed not to be longer than k.
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

import re
def justify(array, k):
    toReturn = []
    tmp = ''
    for element in array:
        if len(tmp) + len(element) + 1 <= k:
            tmp += (element+' ')
        else:
            toReturn.append(tmp[0:-1])
            tmp = ''
            tmp += element + ' '
    toReturn.append(tmp[0:-1])
    final = []
    for element in toReturn:
        diff = k - len(element)
        mod = diff % element.count(' ')
        num = (int)(diff / element.count(' '))
        t = re.sub(r' ', ' '*(num+1), element)
        element = t
        if mod > 0:
            for i in range(0, len(element)):
                if element[i] == ' ':
                    element = element[0:i] + ' ' + element[i:]
                    mod -= 1
                if mod == 0:
                    break
        final.append(element)
    return final
print(justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16))