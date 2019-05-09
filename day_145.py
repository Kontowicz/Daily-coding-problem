# Given the head of a singly linked list, 
# swap every two nodes and return its head.

# For example, given 1 -> 2 -> 3 -> 4, 
# return 2 -> 1 -> 4 -> 3.

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


def solution(array):
    node = array
    while node.next != None:
        node.value, node.next.value = node.next.value, node.value

        node = node.next
        if node.next == None:
            break
        node = node.next
    return node

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

solution(head)

assert head.value == 2
assert head.next.value == 1
assert head.next.next.value == 4
assert head.next.next.next.value == 3
print('Test pass.')