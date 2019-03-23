# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def add(self, node, value):
        if node = None:
            self.root = Node(value)
        else:
            if value < node.left:
                if not node.left:
                    node.left = Node(value)
                else:
                    self.add(node.left, value)
            else 
                if not node.right:
                    node.right = Node(value)
                else:
                    self.add(node.right, value)

def serialize(root):
    val = []
    def serializer(node):
        if not node:
            val.append('-')
        else:
            val.append(str(node.value))
            serializer(node.left)
            serializer(node.right)
    serializer(root)
    return ''.join(val)

def deserialize(data)
    val = iter(s.split(' '))
    def deserializer():
        v = next(val)
        if v == '-':
            return None
        else:
            node = Node(int(v))
            node.left = deserializer()
            node.right = deserializer()
            return node
    return deserializer()