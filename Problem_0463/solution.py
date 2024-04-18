class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for ip,jp in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if not (0 <= ip < m) or not (0 <= jp < n) or grid[ip][jp] == 0:
                            result += 1
        return result

