# Given a string of parentheses, write a function to compute the minimum number of 
# parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

# For example, given the string "()())()", you should return 1. Given the string ")
# (", you should return 2, since we must remove all of them.

def count_parentheses(string):
    opens = 0
    count = 0

    for char in string:
        if char == '(':
            opens += 1
        elif char == ')':
            if opens == 0:
                count += 1
            else:
                opens -= 1

    return count + opens

assert count_parentheses('()())()') == 1
assert count_parentheses(')(') == 2
print('Test pass')