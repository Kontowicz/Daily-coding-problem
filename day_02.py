#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].


input_arr_1 = [1, 2, 3, 4, 5]
input_arr_2 = [3, 2, 1]

def get_arr(arr):
    multi = 1
    new_arr = []
    for x in arr:
        multi = multi * x
    
    for x in arr:
        new_arr.append(int(multi/x))
    return new_arr

print(get_arr(input_arr_1))
print(get_arr(input_arr_2))