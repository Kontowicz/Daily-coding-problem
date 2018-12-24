#  There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
#  Given N, write a function that returns the number of unique ways you can climb the staircase. 
#  The order of the steps matters.

#  For example, if N is 4, then there are 5 unique ways:

#  1, 1, 1, 1
#  2, 1, 1
#  1, 2, 1
#  1, 1, 2
#  2, 2
#  What if, instead of being able to climb 1 or 2 steps at a time, you
#  could climb any number from a set of positive integers X? For example, 
#  if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


# To test implementation plese uncoment code
# 1 or 2 steps by one

# def countRecursive(N):
#     if N <= 1:
#         return 1
#     return countRecursive(N - 1) + countRecursive(N - 2)
# assert countRecursive(4) == 5

# ////////////////////////////////////////////////////////////////////
# Set of posible steps

def countRecursive(N, X):
    if N <= 1:
        return 1
    r = 0
    for i in X:
        if i <= N:
            r += countRecursive(N - i, X)
    return r

def run(N, X):
    return countRecursive(N, X)

print(countRecursive(4, [1,2]))