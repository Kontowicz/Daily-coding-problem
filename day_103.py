# Given a string and a set of characters, return the shortest substring containing all the characters in the set.

def isValid(string, characters):
    for item in characters:
        if item not in string:
            return False
    
    return True

def minWindowd(string, characters):
    if len(string) < len(characters):
        return None
    
    start = 0
    end = len(string)

    while True:
        if isValid(string[start:end], characters):
            start += 1
        else:
            break
    start -=1
    while True:

        if isValid(string[start:end], characters):
            end -= 1
        else:
            break
    end += 1
    return string[start:end]

print(minWindowd('figehaeci', {'a', 'e', 'i'}))
print(minWindowd('bacb', {'a', 'c'}))
print(minWindowd('teststring', {'t', 's'}))
    