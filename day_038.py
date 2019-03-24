# You have an N by N board. Write a function that, given N, 
# returns the number of possible arrangements of the board 
# where N queens can be placed on the board without threatening 
# each other, i.e. no two queens share the same row, column, or diagonal.

def countQuenns(array):
    counter = 0
    for row in array:
        for element in row:
            if element == 1:
                counter += 1

    return counter

def isSave(array, row, collumn):
    for i in range(collumn):
        if array[row][i] == 1:
            return False

    for i,j in zip(range(row,-1,-1), range(collumn,-1,-1)):
        if array[i][j] == 1:
            return False

    for i,j in zip(range(row,len(array),1), range(collumn,-1,-1)): 
        if array[i][j] == 1:
            return False
    return True

def solve(array, column, size):
    if column >= size:
        return True

    for i in range(size):
        if isSave(array, i, column):
            array[i][column] = 1

            if solve(array, column + 1, size):
                return True
            
            array[i][column] = 0
    return False

def trigger(size):
    array = []
    for i in range(size):
        array.append([0]*size)
    if solve(array, 0, len(array)) == False:
        return False
    
    for i in array:
        print(i)
    return countQuenns(array)
print(trigger(7))