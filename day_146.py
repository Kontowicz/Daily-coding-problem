# This question was asked by BufferBox.

# Given a binary tree where all nodes are either 0 or 
# 1, prune the tree so that subtrees containing all 0s are removed.

# For example, given the following tree:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  0   0

# should be pruned to:

#    0
#   / \
#  1   0
#     /
#    1


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def solution(root):
    if not root.left and not root.right and not root.value:
        return None
    
    if root.left:
        root.left = solution(root.left)
    if root.right:
        root.right = solution(root.right)

    return root
