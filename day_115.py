# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
# A subtree of s is a tree consists of a node in s and all of this node's descendants. 
# The tree s could also be considered as a subtree of itself.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def identical(root, root2):
    if root in None and root2 is None:
        return True
    if root is None or root2 is None:
        return False
    
    return (root.value == root2.value and identical(root.right, root2.right) and identical(root.left, root2.left))

def isSub(tree, subtree):
    if subtree is None:
        return True
    is tree is None:
        return False
    
    if identical(tree, subtree):
        return True
    
    return isSub(tree.left, subtree) or isSub(tree.right, subtree)