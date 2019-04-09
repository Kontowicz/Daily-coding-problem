# Given a string and a set of delimiters, reverse the words in the string while maintaining the 
# relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

def reverseString(string, delimiters):
    toReturn = ''
    tmp = ''
    delimInOrder = []
    for item in string:
        if item in delimiters:
            delimInOrder.append(item)
    delimInOrder = delimInOrder[::-1]
    for i in range(len(string)-1, -1,-1):
        sign = string[i]
        if sign in delimiters or i == 0:
            if i == 0:
                toReturn += sign + tmp[::-1]
            else:
                toReturn += tmp[::-1] + delimInOrder.pop()
            tmp = ''
            continue
        tmp += sign
        
    return toReturn

print(reverseString('hello/world:here', [':', '/']))

assert reverseString('hello/world:here', {':', '/'}) == 'here/world:hello'
