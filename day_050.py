#Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'

class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def inorder(node):
    if node != None:
        inorder(node.left)
        print(node.data, end='')
        inorder(node.right)

n = Node('*', Node('+', Node('3', None, None), Node('2', None, None)), Node('+', Node('4', None, None), Node('5', None, None)))
inorder(n)