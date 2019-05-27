# Given an arithmetic expression in Reverse Polish Notation, write a
# program to evaluate it. The expression is given as a list of numbers and
# operands. For example: [5, 3, '+'] should return 5 + 3 = 8.
# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
# should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
# You can assume the given expression is always valid.

def calculate(mathValue):
    stack = []

    for item in mathValue:
        if str(item).isdigit():
            stack.append(item)
        else:
            a = stack.pop()
            b = stack.pop()
            if item == '+':
                stack.append(b + a)
            if item == '-':
                stack.append(b - a)
            if item == '*':
                stack.append(b * a)
            if item == '/':
                stack.append(b / a)

    return stack.pop()

assert calculate([5, 3, '+']) == 8
assert calculate([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']) == 5

