# Given a binary tree, find a minimum path sum from root to a leaf.

import sys
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def getMinPath(root, valuePath, sumPath):
    candidate_sum = sumPath + root.value
    candidate_path = valuePath + [root.value]

    if not root.left and not root.right:
        return candidate_sum, candidate_path

    leftMin, rightMin = sys.maxsize, sys.maxsize
    if root.left:
        leftMin, leftPath = getMinPath(root.left, candidate_path, candidate_sum)
    
    if root.right:
        rightMin, rightPath = getMinPath(root.right, candidate_path, candidate_sum)

    return (leftMin, leftPath) if leftMin < rightMin else (rightMin, rightPath)

def minPathInTree(root):
    return getMinPath(root, [], 0)