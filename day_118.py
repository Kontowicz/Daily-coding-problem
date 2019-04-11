# Given a sorted list of integers, square the elements and give the output in sorted order.

def computerSquare(array):
    K = 0
    
    for item in array:
        K += 1
        if item >= 0:
            break

    i = K - 1
    j = K

    ind = 0

    temp = [0] * len(array)

    while i>=0 and j < len(array):
        if array[i] * array[i] < array[j] * array[j]:
            temp[ind] = array[i] * array[i]
            i -= 1
        else:
            temp[ind] = array[j] * array[j]
            j += 1
        
        ind += 1

    while i >= 0:
        temp[ind] = array[i] * array[i]
        i -= 1
        ind += 1

    while j < len(array):
        temp[ind] = array[j] * array[j]
        j += 1
        ind += 1
    
    for i in range(0, len(array)):
        array[i] = temp[i]

    return array

print(computerSquare([-9, -2, 0, 2, 3]))

    