# Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"
def reverseString(string):
    return ' '.join(string.split(' ')[::-1])

print(reverseString('hello world here'))
assert "here world hello" == reverseString('hello world here')