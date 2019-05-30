# Implement a 2D iterator class. It will be initialized with an array
# of arrays, and should implement the following methods:
#
# next(): returns the next element in the array of arrays.
# If there are no more elements, raise an exception.
# has_next(): returns whether or not the iterator still has elements left.

class iterator:
    def __init__(self, matrix):
        self.matrix = matrix
        self.flat = self.generator()
        self.next_value = next(self.flat)

    def generator(self):
        for row in self.matrix:
            for number in row:
                yield number

    def has_next(self):
        return self.next_value != None

    def next(self):
        value = self.next_value
        try:
            self.next_value = next(self.flat )
        except Exception:
            self.next_value = None

        return value