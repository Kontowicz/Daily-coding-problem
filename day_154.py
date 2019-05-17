# Implement a stack API using only a heap. A stack implements the following methods:
#
# push(item), which adds an element to the stack
# pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
# Recall that a heap has the following operations:
#
# push(item), which adds a new key to the heap
# pop(), which removes and returns the max value of the heap

import sys
from heapq import heappush, heappop

class solution:
    def __init__(self):
        self.counter = sys.maxsize
        self.stack = []

    def push(self, item):
        heappush(self.stack, (self.counter, item))
        self.counter -= 1

    def pop(self):
        if not self.stack:
            return None

        x, item = heappop(self.stack)
        return  item