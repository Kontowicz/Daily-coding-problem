# Given a list of possibly overlapping intervals, return a new list of 
# intervals where all overlapping intervals have been merged.

def mergeOverlap(array):
    array.sort(key = lambda x : x[0])
    
    tmp = []
    tmp.append(array[0])
    for i in range(1, len(array)):
        top = tmp[-1]

        if top[1] < array[i][0]:
            tmp.append(array[i])
        elif top[1] < array[i][1]:
            top[1] = array[i][1]
            tmp.pop()
            tmp.append(top)

    return tmp

print('Data: [[1, 3], [5, 8], [4, 10], [20, 25]]')
print(mergeOverlap([[1, 3], [5, 8], [4, 10], [20, 25]]))
assert mergeOverlap([[1, 3], [5, 8], [4, 10], [20, 25]]) == [[1, 3], [4, 10], [20, 25]]
print('Test ok')