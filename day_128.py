# All the disks start off on the first rod in a stack. They are ordered by size, with the 
# largest disk on the bottom and the smallest one at the top.

# The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

#     You can only move one disk at a time.
#     A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
#     You cannot place a larger disk on top of a smaller disk.

# Write a function that prints out all the steps necessary to complete the Tower of Hanoi. 
# You should assume that the rods are numbered, with the first rod being 1, the second 
# (auxiliary) rod being 2, and the last (goal) rod being 3.

def hanoiSolver(disks, tower_1, tower_2, tower_3):
    if disks == 1:
        tower_3.append(tower_1.pop())
    else:
        hanoiSolver(disks - 1, tower_1, tower_3, tower_2)
        print(tower_1, tower_2, tower_3)
        tower_3.append(tower_1.pop())
        print(tower_1, tower_2, tower_3)
        hanoiSolver(disks - 1, tower_2, tower_1, tower_3)

    print(tower_1, tower_2, tower_3)


def solver(n):
    tower_1, tower_2, tower_3 = list(range(1, n + 1))[::-1], list(), list()
    hanoiSolver(n, tower_1, tower_2, tower_3)


solver(3)