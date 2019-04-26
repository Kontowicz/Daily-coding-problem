# Use a more space-efficient data structure, SparseArray, that implements the same interface:

#     init(arr, size): initialize with the original large array and size.
#     set(i, val): updates index at i with val.
#     get(i): gets the value at index i.



class sparseArray:
    def __init__(self, array):
        self.storage = {}
        for i, num in enumerate(array):
            if num:
                self.storage[i] = num

    def set(self, i, val):
        self.storage[i] = val
    
    def get(self, i):
        return self.storage[i]

array = [1, 0, 0, 0, 3, 0, 2]

sa = sparseArray(array)
assert sa.storage == {0: 1, 4: 3, 6: 2}