# You are given an N by M matrix of 0s and 1s. 
# Starting from the top left corner, how many ways are there to reach the bottom right corner?

# You can only move right and down. 0 represents an 
# empty space while 1 represents a wall you cannot walk through.

def solution(array):

    result = []

    for row in array:
        tmp = []
        for item in row:
            if item == 1:
                tmp.append(0)
            else:
                tmp.append(1)
        result.append(tmp)

    for i in range(1, len(result)):
        for j in range(1, len(result[i])):
            if result[i][j] == 0:
                continue
            else:
                result[i][j] = result[i - 1][j] + result[i][j - 1]


    return result[-1][-1]

