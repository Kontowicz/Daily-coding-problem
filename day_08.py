# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

def is_unival(root):
    if root == None:
        return True
    if root.left != null and root.left.val != root.val:
        return False
    if root.right != null and root.right.val != root.val:
        return False
    if is_unival(root.left) and is_unival(root.right):
        return True
    return False

def count(root):
    if root == None:
        return 0
    total = count(root.left)  + count(root.right)

    if is_unival(root):
        total += 1
    return total