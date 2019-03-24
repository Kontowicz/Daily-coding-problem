# Given a tree, find the largest tree/subtree that is a BST.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def largest(node):
    INT_MIN = -2147483648
    INT_MAX = 2147483647
    if node == None:
        return 0, INT_MIN, INT_MAX, 0, True
    if node.left == None and node.right == None:
        return 1, node.value, node.value, 1, True
    
    l = largest(node.left)
    r = largest(node.right)

    ret = [0] * 5
    ret[0] = (1 + l[0] + r[0])

    if l[4] and r[4] and l[1] < node.value and r[2] > node.value:
        ret[2] = min(l[2], min(r[2], node.value))
        ret[1] = max(r[1], max(l[1], node.value))

        ret[3] = ret[0]
        ret[4] = True

        return ret

    ret[3] = max(l[3], r[3])
    ret[4] = False

    return ret

root = Node(60)  
root.left = Node(65)  
root.right = Node(70)  
root.left.left = Node(50) 
print(largest(root)[3])