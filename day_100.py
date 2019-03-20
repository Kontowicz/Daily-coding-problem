# You are in an infinite 2D grid where you can move in any of the 8 directions:
#     (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
# You are given a sequence of points and the order in which you need to cover 
# the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

def shortestPath(point_1, point_2):
    dx = abs(point_1[0] - point_2[0])

    dy = abs(point_1[1] - point_2[1])

    return max(dx, dy)

def countRoad(array):
    count = 0

    for i in range(0, len(array) - 1):
        count += shortestPath(array[i], array[i+1])

    return count

print(countRoad([[0, 0], [1, 1], [1, 2]]))