# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def reconstruct(preOrderRighteOrder, inOrder, index = None):
    if inOrder:
        if index is None:
            index = {}
            for i in range(len(inOrder)):
                index[inOrder[i]] = i
        
        node = Node(preOrderRighteOrder[0])
        index_num = index.get(node.value)
        inOrderLeft = inOrder[:index_num]
        inOrderRight = inOrder[index_num+1:]
        preOrderRighteOrderLeft = [n for n in preOrderRighteOrder if index.get(n) < index_num] 
        preOrderRight = [n for n in preOrderRighteOrder if index.get(n) > index_num] 

        node.left = reconstruct(preOrderRighteOrderLeft, inOrderLeft)
        node.right = reconstruct(preOrderRight, inOrderRight)
        return node

t = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
