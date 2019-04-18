# You are given a 2-d matrix where each cell represents number of coins in that cell. 
# Assuming we start at matrix[0][0], and can only move right or down, find the maximum 
# number of coins you can collect by the bottom right corner.
def getMax(array, row, col, rows, columns):
    cval = array[row][col]

    if row == rows - 1 and col == columns - 1:
        return cval

    down, right = cval, cval

    if row < rows - 1:
        down += getMax(array, row + 1, col, rows, columns)

    if col < columns -1:
        right += getMax(array, row, col + 1, rows, columns)

    return max(down, right)

def getMaxRun(array):
    return getMax(array, 0, 0, len(array), len(array[0]))

data = [[0, 3, 1, 1],
         [2, 0, 0, 4],
         [1, 5, 3, 1]]
print(getMaxRun(data))