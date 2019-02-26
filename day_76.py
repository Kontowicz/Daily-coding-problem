# You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can 
# be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter 
# at each column is lexicographically later as you go down each row. It does not matter whether each row 
# itself is ordered lexicographically.

def cnt(array):
    toRerturn = 0
    for i in range(len(array[0])):
        for k in range(1, len(array)):
            if array[k][i] < array[k-1][i]:
                toRerturn += 1
                break

    return toRerturn

print(cnt(['cba', 'daf', 'ghi']))