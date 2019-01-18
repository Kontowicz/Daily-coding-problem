# Given the root to a binary search tree, find the second largest node in the tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = Node(data)
                else :
                    self.left.insert(data)
            elif data> self.value:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    
def secondLargest(root):
    tmp = root.right
    if tmp.right == None:
        return root.value
    else:
        secondLargest(root.right)

root = Node(12)
root.insert(15)
root.insert(11)
root.insert(10)
root.insert(9)
root.insert(8)
print(secondLargest(root))