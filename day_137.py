# Implement a bit array.

# A bit array is a space efficient array that holds a value of 1 or 0 at each index.

#     init(size): initialize the array with size
#     set(i, val): updates index at i with val where val is either 1 or 0.
#     get(i): gets the value at index i.


class BitArray:
    def __init__(self, size):
        self.size = size
        self.set_u = {}

    def set(self, i, value):
        if value and i not in self.set:
            self.set_u.add(i)
        elif not val and i in self.set_u:
            self.set_u.remove(i)

    def get(self, i):
        return int(i in self.set)