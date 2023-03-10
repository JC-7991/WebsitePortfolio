'''
Given a matrix of 1s and 0s, return the number of "islands" in 
the matrix. A 1 represents land and 0 represents water, so an 
island is a group of 1s that are neighboring whose perimeter is surrounded by water.
For example, this matrix has 4 islands.
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
'''

class Graph:
 
    def __init__(self, row, col, g):

        self.ROW = row
        self.COL = col
        self.graph = g

    def isSafe(self, i, j, visited):
        return(i >= 0 and i < self.ROW and j >= 0 and j < self.COL and not visited[i][j] and self.graph[i][j])

    def DFS(self, i, j, visited):

        row_num = [-1, -1, -1,  0, 0,  1, 1, 1]
        col_num = [-1,  0,  1, -1, 1, -1, 0, 1]
        visited[i][j] = True

        for k in range(8):
            if self.isSafe(i + row_num[k], j + col_num[k], visited):
                self.DFS(i + row_num[k], j + col_num[k], visited)
 
    def countIslands(self):

        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
        cnt = 0

        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] == False and self.graph[i][j] == 1:
                    self.DFS(i, j, visited)
                    cnt += 1
 
        return cnt

if __name__ == "__main__":
 
    graph = [[1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1]]
    
    
    row = len(graph)
    col = len(graph[0])
    g = Graph(row, col, graph)
    
    print("Number of islands:"), print(g.countIslands())