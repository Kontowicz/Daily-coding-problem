# Given a linked list and a positive integer k, rotate the list to the right by k places.

class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

def getLinkedList(array):
    head = Node(array[0])
    iter = head
    for item in array[0::]:

        iter.next = Node(item)
        iter = iter.next

    return head


def convToArray(head):
    toReturn = []

    while head.next != None:
        toReturn.append(head.value)
        head = head.next

    return toReturn

def rotate(llist, k):
    tmpNode = llist
    head = tmpNode
    size = 0
    while tmpNode:
        tail = tmpNode
        tmpNode = tmpNode.next
        size += 1

    newHead = llist
    newTail = None
    for _ in range(size - k):
        newTail = newHead
        newHead = newHead.next

    tail.next = head
    newTail.next = None

    return newHead