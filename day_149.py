# Given a list of numbers L, implement a method sum(i, j) 
# which returns the sum from the sublist L[i:j] (including i, excluding j).

# For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should 
# return sum([2, 3]), which is 5.

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class MyList:
    def __init__(self):
        self.head = Node(None)
    
    def add(self, value):
        tmp = self.head

        while tmp.next != None:
            tmp = tmp.next
        
        tmp.next = Node(value)

    def show(self):
        tmp = self.head

        while tmp.next != None:
            tmp = tmp.next
            print(tmp.value, end = ' ')

    def sumSubList(self, start, end):
        tmp = self.head
        sumValue = 0
        counter = -1
        while tmp.next != None and counter < end:
            if counter >= start:
                sumValue += tmp.value
            tmp = tmp.next
            counter += 1
        return sumValue


l = MyList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
print(l.sumSubList(1,3))
assert l.sumSubList(1,3) == 5