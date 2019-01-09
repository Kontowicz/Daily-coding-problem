# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

def isBalanced(string):
    if len(string) % 2 != 0:
        return False
    
    stack = []
    for element in string:
        if element == '(' or element == '[' or element == '{':
            stack.append(element);
        else:
            if element == ')':
                x = stack.pop()
                if x != '(':
                    return False
            elif element == '}':
                x = stack.pop()
                if x != '{':
                    return False
            elif element == ']':
                x = stack.pop()
                if x != '[':
                    return False
    if len(stack) != 0:
        return False
    return True

print(isBalanced('([])[]({})'))
print(isBalanced('([)]'))
print(isBalanced('((()'))