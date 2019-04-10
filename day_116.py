# Generate a finite, but an arbitrarily large binary tree quickly in O(1).

import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def generate():
    root = Node(0)

    if random.random() < 0.5:
        root.left = generate()
    if random.random() < 0.5:
        root.right = generate()

    return root