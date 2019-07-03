# Given a complete binary tree, count the number
# of nodes in faster than O(n) time. Recall that a
# complete binary tree has every level filled except
# the last, and the nodes in the last level are filled starting from the left.

class Node:
    def __init__(self):
        self.left = None
        self.right = None


def count(root, left=0, right=0):
    if not root:
        return 0

    if not left:
        node = root
        while node:
            node = node.left
            left += 1
    if not right:
        node = root
        while node:
            node = node.right
            right += 1

    if left == right:
        return 2 ** left - 1

    return 1 + count(root.left, left=left - 1) + count(root.right, right=right - 1)