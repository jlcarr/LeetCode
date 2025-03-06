class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                while grid[i][j]-1 != n*i+j:
                    v = grid[i][j] - 1
                    vi, vj = v // n, v % n
                    if grid[i][j] == grid[vi][vj]:
                        break
                    grid[i][j] = grid[vi][vj]
                    grid[vi][vj] = v + 1
        print(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] - 1 != i * n + j:
                    return [grid[i][j], i * n + j + 1]
        return -1
