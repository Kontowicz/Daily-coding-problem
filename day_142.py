# You're given a string consisting solely of (, ), and *. * can 
# represent either a (, ), or an empty string. Determine whether 
# the parentheses are balanced.

# For example, (()* and (*) are balanced. )*( is not balanced.

def solution(string):
    start = 0
    end = len(string) - 1 
    while start < end:
        if (string[start] == '(' and string[end] == '(') or (string[start] == ')' and string[end] == '('):
            return False

        start += 1
        end -= 1

    return True

solution('(()*') == True
solution('(*)') == True
solution(')*(') == False
print('All tests pass')