# Given a binary tree, return all paths from the root to leaves.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

path = []

def getPath(root):
    if root == None:
        return []

    nodePath = []
    leftPath = getPath(root.left)
    for path in leftPath:
        nodePath.append([root.value] + path)

    rightPath = getPath(root.right)
    for path in rightPath:
        nodePath.append([root.value] + path)
    
    return nodePath if nodePath else [[root.value]]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

print(getPath(root))