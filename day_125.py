# Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def solution(root, value):
    if root.left != None and root.right != None:
        if root.left.value + root.right.value == value:
            return root
        else:
            return solution(root.left, value) or solution(root.right, value) 

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(11)
root.right.right = Node(15)

node = solution(root, 20)
print('Node value: {} Left node value: {} right node value: {}'.format(node.value, node.left.value, node.right.value))
