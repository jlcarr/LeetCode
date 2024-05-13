class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        grid = [[v ^ row[0] for v in row] for row in grid]
        m,n = len(grid),len(grid[0])
        result = 0
        for j in range(n):
            colsum = sum(grid[i][j] for i in range(m))
            result += max(colsum, m-colsum) * (1 << (n-1-j))
        return result
