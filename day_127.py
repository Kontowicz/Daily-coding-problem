# Let's represent an integer in a linked list format by having each node 
# represent a digit in the number. The nodes make up the number in reversed order.

# For example, the following linked list:

# 1 -> 2 -> 3 -> 4 -> 5

# is the number 54321.

# Given two linked lists in this format, return their sum in the same linked list format.

# For example, given

# 9 -> 9

# 5 -> 2

# return 124 (99 + 25) as:

# 4 -> 2 -> 1

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

def getNum(valueList):
    tmp = []
    toReturn = 0
    factor = 1
    while valueList != None:
        toReturn += (valueList.value*factor)
        factor *= 10
        valueList = valueList.next

    return toReturn

def createList(value):
    numstr = str(value)
    head = Node(0)
    prev = head
    for num in numstr[::-1]:
        curr = Node(int(num))
        prev.next = curr
        prev = curr

    return head.next

def printList(l):
    while l != None:
        print(l.value, end='->')
        l = l.next
    print('None')
l = Node(9)
l.next = Node(9)


r = Node(5)
r.next = Node(2)

result = createList(getNum(l) + getNum(r))
printList(result)