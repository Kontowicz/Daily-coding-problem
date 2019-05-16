# Find an efficient algorithm to find the smallest distance 
# (measured in number of words) between any two given words in a string.

# For example, given words "hello", and "world" and a text content of 
# "dog cat hello cat dog dog hello cat world", return 1 
# because there's only one word "cat" in between the two words.

def solution(sentence, firstWords, secondWord):
    if firstWords == secondWord:
        return 0

    words = sentence.split(' ')

    minDistance = len(words) + 1

    for i in range(len(words)):
        if words[i] == firstWords or words[i] == secondWord:
            prev = i
            break

    while i < len(words):
        if words[i] == firstWords or words[i] == secondWord:
            if words[prev] != words[i] and (i - prev) < minDistance:
                minDistance = i - prev - 1
                prev = i
            else:
                prev = i
        i += 1

    return minDistance

assert solution("dog cat hello cat dog dog hello cat world", "hello", "world") == 1
print('Test pass.')