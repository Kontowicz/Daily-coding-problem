# Given a 2-D matrix representing an image, a location of a pixel in the 
# screen and a color C, replace the color of the given pixel and all 
# adjacent same colored pixels with C.

# For example, given the following matrix, and 
# location pixel of (2, 2), and 'G' for green:

# B B W
# W W W
# W W W
# B B B
# Becomes

# B B G
# G G G
# G G G
# B B B

def floodFillUtil(array, x, y, prevC, newC):
    if x < 0 or x >= len(array) or y < 0 or y >= len(array[0]):
        return
    if array[x][y] != prevC:
        return
    
    array[x][y] = newC

    floodFillUtil(array, x + 1, y, prevC, newC)
    floodFillUtil(array, x - 1, y, prevC, newC)
    floodFillUtil(array, x, y + 1, prevC, newC)
    floodFillUtil(array, x, y-1, prevC, newC)

def floodFill(array, x, y, newC):
    prevC = array[x][y]
    floodFillUtil(array, x, y, prevC, newC)

    return array

a = [['B', 'B', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W'], ['B', 'B', 'B']]

data = floodFill(a, 2, 2, 'G')