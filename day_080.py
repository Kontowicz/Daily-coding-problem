# Given the root of a binary tree, return a deepest node. 
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(root): 
    if(not root): 
        return 0
      
    left = height(root.left)  
    right = height(root.right)  
      
    return max(left, right) + 1

def deepest(root, levels):
    if not root:
        return
    if(levels == 1): 
        print(root.value)
    elif(levels > 1): 
        deepest(root.left, levels - 1)  
        deepest(root.right, levels - 1) 

root = Node(1)  
root.left = Node(2)  
root.right = Node(3)  
root.left.left = Node(4)  
root.right.left = Node(5)  
root.right.right = Node(6)  
root.right.left.right = Node(7)  
root.right.right.right = Node(8)  
root.right.left.right.left = Node(9) 

deepest(root, 5)