# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.
# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
#     Right, then down
#     Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.


def numberOfPaths(left, right):  
    if(left == 1 or right == 1): 
        return 1
    return numberOfPaths(left-1, right) + numberOfPaths(left, right-1) 

numbers = [[2, 2], [5, 70]]

for i in range(0, len(numbers)):
    print('Matrix size: ', numbers[i][0])
    print('Ways: ', numberOfPaths(numbers[i][0], numbers[i][0]))
    assert numberOfPaths(numbers[i][0], numbers[i][0]) == numbers[i][1]