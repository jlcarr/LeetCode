from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        @lru_cache(maxsize=None)
        def dp(i,j):
            result = 0
            if i == m-1 and j == n-1:
                return 1
            if i < m-1 and obstacleGrid[i+1][j] == 0:
                result += dp(i+1,j)
            if j < n-1 and obstacleGrid[i][j+1] == 0:
                result += dp(i,j+1)
            return result
        return dp(0,0)
