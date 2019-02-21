# Given the head of a singly linked list, reverse it in-place.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:

    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.value, end='')
            tmp = tmp.next
        

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_element = curr.next
            curr.next = prev
            prev = curr
            curr = next_element
        self.head = prev

lis = List()
lis.push(1) 
lis.push(2) 
lis.push(3) 
lis.push(4) 
lis.print()
print()
lis.reverse()
lis.print()
