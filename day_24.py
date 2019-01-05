# Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
# Design a binary tree node class with the following methods:
#     is_locked, which returns whether the node is locked
#     lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
#     unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

class lockingBinaryTree(object):
    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.lock = False
        self.lockCount = 0
        self.parent = parent
    
    def canLock(self):
        if self.lockCount > 0:
            return False
        
        par = self.parent
        while par:
            if par.lock:
                return False
            par = par.parent
        
        return True

    def isLocked(self):
        return self.lock

    def lock(self):
        if self.canLock():
            self.lock = True

            par = self.parent
            while par:
                par.lockCount += 1
                par = par.parent
            return True
        else :
            return False

    def unlock(self):
        if self.canLock():
            self.lock = False

            par = self.parent
            while par:
                par.lockCount -= 1
                par = par.parent
            return True
        else :
            return False