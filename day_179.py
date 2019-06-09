# Given the sequence of keys visited by a postorder
# traversal of a binary search tree, reconstruct the tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def createTree(postorder):
    head = Node(postorder[-1])

    if len(postorder) == 1:
        return head

    for i in range(0, len(postorder) - 1):
        if postorder[i] > head.value:
            s = i
            break

    less, gt = postorder[:s], postorder[s:-1]

    head.left = createTree(less) if less else None
    head.right = createTree(gt) if less else None

    return head