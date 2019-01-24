# Implement a stack that has the following methods:
#     push(val), which pushes an element onto the stack
#     pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
#     max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

class myStack(object):
    def __init__(self):
        self.value = []
        self.max_value = None
    
    def push(self, val):
        if self.max_value == None:
            self.max_value = val
            self.value.append(val)
        else:
            self.max_value = max(val, self.max_value)
            self.value.append(val)

    def pop(self):
        v = None 
        if len(self.value) != 0:
            self.max_value = max(self.value)
        else:
            self.max_value = None
        return v

    def max(self):
        return self.max_value

my = myStack()
print(my.max())
my.push(10)
print(my.pop())
print(my.pop())

    