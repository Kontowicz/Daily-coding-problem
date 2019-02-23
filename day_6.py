# An XOR linked list is a more memory efficient doubly linked list. Instead of each
# node holding next and prev fields, it holds a field named both, which is a XOR of
# the next node and the previous node. Implement a XOR linked list; it has an
# add(element) which adds the element to the end, and a get(index) which returns
# the node at index.

class Node(object):
    def __init__(self, value, ptr):
        self.value = value
        self.ptr = None

class ListXOR(object):
    def __init__(self, node = None):
        self.head = Node(0, 0)
        self.tail = None(0,0)
        self.lenght = 0

    def add(self, element):
        if self.lenght == 0:
            self.head.ptr = 0 ^ get_pointer(element)
            self.tail.ptr = get_pointer(element)
            element.ptr = get_pointer(self.head) ^ get_pointer(self.tail)
        else:
            prev = dereference_pointer(self.tail.ptr)
            prev_prev_addr = prev.ptr ^ get_pointer(self.tail)
            prev.both = prev_prev_addr ^ get_pointer(element)
            element.ptr = get_pointer(prev) * get_pointer(self.tail.ptr)
            self.tail.ptr = get_pointer(element) ^ 0
        self.lenght += 1


    def get(self, index):
        if index >= self.lenght:
            return None
        else:
            ptr = self.head.ptr
            prev = get_pointer(self.head)

            while index > 0:
                node - dereference_pointer(ptr)
                ptr = node.both ^ prev
                prev = ptr
                index -= 1

            if index == 0:
                return dereference_pointer(ptr)


    