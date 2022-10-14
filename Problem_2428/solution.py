class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                s = 0
                s += grid[i][j] 
                s += grid[i-1][j] 
                s += grid[i-1][j-1] 
                s += grid[i-1][j+1]
                s += grid[i+1][j] 
                s += grid[i+1][j-1] 
                s += grid[i+1][j+1]
                result = max(result, s)
        return result
