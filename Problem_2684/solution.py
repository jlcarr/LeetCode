class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        curr = [True] * m
        for icol in range(n-1):
            new = [False] * m
            for irow in range(m):
                if not curr[irow]:
                    continue
                if irow-1 >= 0 and grid[irow][icol] < grid[irow-1][icol+1]:
                    new[irow-1] = True
                if grid[irow][icol] < grid[irow][icol+1]:
                    new[irow] = True
                if irow+1 < m and grid[irow][icol] < grid[irow+1][icol+1]:
                    new[irow+1] = True
            if not any(new):
                return icol
            curr = new
        return n-1
