class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        rowc = [0] * m
        colc = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rowc[i] += 1
                    colc[j] += 1
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rowc[i] > 1 or colc[j] > 1):
                    result += 1

        return result
        
