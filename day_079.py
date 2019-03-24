# Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

def nondecreasing(array):
    counter = 0

    for i in range(0, len(array) - 1):
        if array[i] > array[i+1]:
            counter += 1 

    return counter <= 1

assert nondecreasing([10, 5, 7]) == True
assert nondecreasing([10, 5, 1]) == False
print('Test ok')