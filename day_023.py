# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. 
# If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7,
# since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

import sys

minDistance = sys.maxsize

def findShortestPathLen(maze, source, destination, visited, curr):
    x, y = source
    global minDistance

    if x not in range(0, len(maze)) or y not in range(0, len(maze)):        
        return

    if maze[x][y] == True or source in visited:
        return
    
    if source == destination:
        if curr < minDistance:
            minDistance = curr
            return

    findShortestPathLen(maze, (x-1, y  ), destination, visited+[source], curr+1)
    findShortestPathLen(maze, (x  , y-1), destination, visited+[source], curr+1)
    findShortestPathLen(maze, (x  , y+1), destination, visited+[source], curr+1)
    findShortestPathLen(maze, (x+1, y  ), destination, visited+[source], curr+1)
            
def shortestDistance(maze, source, destination):
    findShortestPathLen(maze, source, destination, [], 0)
    
shortestDistance([[False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]], (3, 0), (0, 0))

print(minDistance)
assert minDistance == 7