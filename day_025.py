# Implement regular expression matching with the following special characters:
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
# For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
# Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

def isValid(string, expression):
    if len(string) == 0:
        return False
    if string[0] == expression[0]:
        return isValid(string[1:], expression[1:])
    if expression[0] == '.':
        return isValid(string[1:], expression[1:])
    if expression[0] == '*' and expression[1:] != string[1:]:
        return isValid(string[1:], expression)
    if expression[0] == '*' and expression[1:] == string[1:]:
        return True
    if expression == string:
        return True
    if expression != string:
        return False

print(isValid("chat", ".*at"))
print(isValid("chats", ".*at"))