# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.
# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

def getPath(root, path, value):
    if root == None:
        return False
    
    path.append(root.value)

    if root.value == value:
        return True
    
    if ((root.left != None and getPath(root.left, path, value)) or
        (root.right != None and getPath(root.right, path, value))):
        return True

    path.pop()
    return False

def findLCA(root, value1, value2):
    pathFirst = []
    pathSecond = []

    if (not getPath(root, pathFirst, value1) or not getPath(root, pathSecond, value2)):
        return -1

    i = 0

    while(i < len(pathFirst) and i < len(pathSecond)):
        if pathFirst[i] != pathSecond[i]:
            break
        i += 1
    
    return pathFirst[i-1]

root = Node(1, None)
root.left = Node(2, root)
root.left.left = Node(4, root.left)
root.left.right = Node(5, root.left)

root.right = Node(3, root)
root.right.right = Node(7, root.right)
root.right.left = Node(6, root.right)

print(findLCA(root, 4, 5))
print(findLCA(root, 4, 6))
print(findLCA(root, 6, 2))
