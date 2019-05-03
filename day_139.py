# Given an iterator with methods next() and hasNext(), 
# create a wrapper iterator, PeekableInterface, which 
# also implements peek(). peek shows the next element 
# that would be returned on next().

# Here is the interface:

# class PeekableInterface(object):
#     def __init__(self, iterator):
#         pass

#     def peek(self):
#         pass

#     def next(self):
#         pass

#     def hasNext(self):
#         pass


class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_value = next(iterator)
        self.has_next = True

    def peek(self):
        return self.next_value

    def next(self):
        next_value = self.next_value
        try:
            self.next_value = next(iterator)
        except:
            self.has_next = False
            self.next_value = None
        return next_value

    def hasNext(self):
        return self.has_next