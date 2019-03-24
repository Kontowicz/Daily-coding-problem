# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList():
    def __init__(self):
        self.head = None
    
    def addElement(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def remove(self, n):
        main = self.head
        ref = self.head

        cnt = 0

        if(self.head is not None):
            while(cnt < n - 1):
                if ref is None:
                    return
                ref = ref.next
                cnt += 1

        before = main
        
        if ref is not None:
            main = main.next
            ref = ref.next
        while(ref.next is not None):
            before = before.next
            main = main.next
            ref = ref.next

        
        before.next = main.next

    def printList(self):
        ptr = self.head
        while(ptr is not None):
            print(ptr.data, end='')
            ptr = ptr.next
        print()

lis = linkedList()
lis.addElement(1)
lis.addElement(2)
lis.addElement(3)
lis.addElement(4)
lis.addElement(5)
lis.addElement(6)
lis.printList()
lis.remove(2)
lis.printList()