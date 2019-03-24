# Given a binary tree of integers, find the maximum path sum between two nodes. 
# The path must go through at least one node, and does not need to go through the root.

class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findMax(root):
    if root is None:
        return 0

    left = findMax(root.left)
    right = findMax(root.right)

    max_value = max(max(left, right) + root.value, root.value)    

    max_top_value = max(max_value, left + right + root.value)

    findMax.val = max(findMax.val, max_top_value)

    return max_value

def maxTree(root):
    findMax.val = float('-inf')
    findMax(root)
    return findMax.val