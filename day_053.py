# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) 
# data structure with the following methods: enqueue, which inserts an element into the queue, 
# and dequeue, which removes it.

class queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, value):
        while len(self.s1)!=0:
            self.s2.append(self.s1.pop())
        
        self.s1.append(value)

        while len(self.s2)!=0:
            self.s1.append(self.s2.pop())
    
    def dequeue(self):
        return self.s1.pop()

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
