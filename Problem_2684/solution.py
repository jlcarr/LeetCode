class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        result = 0
        m,n = len(grid), len(grid[0])
        curr = [0] * m
        for icol in range(n-1):
            new = [0] * m
            for irow in range(m):
                if icol > 0 and curr[irow] == 0:
                    continue
                if irow-1 >= 0 and grid[irow][icol] < grid[irow-1][icol+1]:
                    new[irow-1] = max(new[irow-1], 1 + curr[irow])
                if grid[irow][icol] < grid[irow][icol+1]:
                    new[irow] = max(new[irow], 1 + curr[irow])
                if irow+1 < m and grid[irow][icol] < grid[irow+1][icol+1]:
                    new[irow+1] = max(new[irow+1], 1 + curr[irow])
            result = max(result, *new)
            curr = new
        return result
