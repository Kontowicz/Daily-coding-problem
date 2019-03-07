# Given a matrix of 1s and 0s, return the number of "islands" in the matrix. 
# A 1 represents land and 0 represents water, so an island is a group of 1s 
# that are neighboring whose perimeter is surrounded by water.

class Solution():
    def __init__(self, array):
        self.row = len(array)
        self.column = len(array[0])
        self.graph = array

    def safe(self, i, j, visited):
        return (i >= 0 and i < self.row and j >= 0 and j < self.column and not visited[i][j] and self.graph[i][j])

    def DFS(self, i, j, visited):
        rowN = [-1, -1, -1,  0, 0,  1, 1, 1]
        columnsN = [-1,  0,  1, -1, 1, -1, 0, 1]

        visited[i][j] = True

        for k in range(8):
            if self.safe(i + rowN[k], j + columnsN[k], visited):
                self.DFS(i + rowN[k], j + columnsN[k], visited)

    def count(self):
        visited = [[False for j in range(self.column)] for i in range(self.row)]

        count = 0

        for i in range(self.row):
            for j in range(self.column):
                if visited[i][j] == False and self.graph[i][j] == 1:
                    self.DFS(i, j, visited)
                    count += 1
        return count

array = [[1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1]]

g = Solution(array)
print(g.count())