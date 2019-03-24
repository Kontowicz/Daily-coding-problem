# Determine whether a tree is a valid binary search tree.
INT_MAX = 4294967296
INT_MIN = -4294967296

def isBST(node): 
    return (check(node, INT_MIN, INT_MAX)) 

def check(node, m, ma): 
    if node is None: 
        return True
  
    if node.data < m or node.data > ma: 
        return False
  
    return (check(node.left, m, node.data -1) and
          check(node.right, node.data+1, ma)) 
