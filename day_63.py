# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

def check(array, target):
    # find row 
    for i in range(0, len(array)):
        if target == ''.join(array[i]):
            return True
    
    for i in range(0, len(array)):
        tmp = ''
        for j in range(0, len(array[i])):
            tmp += array[j][i]
        if tmp == target:
            return True
    
    return False

arr = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

print(check(arr, 'MASS'))

print(check(arr, 'FOAM'))
