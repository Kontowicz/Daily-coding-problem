# Print the nodes in bnary tree lavel-wise.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def p(self):
        print(self.val)
        if self.left:
            self.left.p()
        if self.right:
            self.right.p()