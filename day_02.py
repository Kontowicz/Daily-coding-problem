
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