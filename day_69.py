# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

import sys
def maxProduct(array):
    if len(array) < 3:
        return None
    
    leftMin = [-1] * (len(array))
    rightMin = [-1] * (len(array) )
    leftMax = [-1] * (len(array) )
    rightMax = [-1] * (len(array) )

    maxValue = -sys.maxsize - 1

    max_sum = array[0]
    min_sum = array[0]

    for i in range(1, len(array)):
        leftMax[i] = max_sum
        if array[i] > max_sum:
            max_sum = array[i]

        leftMin[i] = min_sum
        if array[i] < min_sum:
            min_sum = array[i]

    max_sum = array[-1]
    min_sum = array[-1]

    for i in range(len(array)-2, -1, -1):
        rightMax[i] = max_sum
        if array[i] > max_sum:
            max_sum = array[i]
        
        rightMin[i] = min_sum
        if array[i] < min_sum:
            min_sum = array[i]

    for i in range(1, len(array) - 1):
        max1 = max(array[i] * leftMax[i] * rightMax[i], array[i] * leftMin[i] * rightMin[i])

        max2 = max(array[i] * leftMax[i] * rightMin[i], array[i] * leftMin[i] * rightMin[i])

        maxValue = max(maxValue, max(max1, max2))
    return maxValue

print(maxProduct([-10, -10, 5, 2]))
