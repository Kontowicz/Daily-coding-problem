# Given a list of points, a central point, and 
# an integer k, find the nearest k points from the central point.

# For example, given the list of points [(0, 0), (5, 4), (3, 1)],
# the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].


import math
def calculateDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def getClosestPoints(point, array, k):
    return sorted(array, key = lambda x: calculateDistance(point, x))[:k]

assert getClosestPoints((1, 2), [(0, 0), (5, 4), (3, 1)], 2) == [(0, 0), (3, 1)]
print('Test pass.')