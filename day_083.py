
class binaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if self.value:
            if value < self.value:
                if self.left == None:
                    self.left = binaryTree(value)
                else:
                    self.left.add(value)
            else:
                if self.right == None:
                    self.right = binaryTree(value)
                else:
                    self.right.add(value)
        else:
            self.value = value
    
    def show(self):
        if self.left:
            self.left.show()
        print(self.value)
        if self.right:
            self.right.show()

def invert(node):
    if node == None:
        return 
    tmp = node.left
    node.left = invert(node.right)
    node.right = invert(tmp)
    return node


b = binaryTree(10)
b.add(1)
b.add(12)
b.add(112)
b.add(2)
b.add(4)
b.show()

invert(b)

b.show()