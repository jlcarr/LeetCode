from functools import cache
from collections import Counter
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7
        m,n = len(grid), len(grid[0])
        @cache
        def rec(i,j):
            if (i == m-1) and (j == n-1):
                return Counter([grid[i][j]%k])
            result = Counter()
            if i < m-1:
                result += Counter({
                    (v+grid[i][j])%k: c 
                    for v,c in rec(i+1,j).items()
                })
            if j < n-1:
                result += Counter({
                    (v+grid[i][j])%k: c 
                    for v,c in rec(i,j+1).items()
                })
            for v in list(result.keys()):
                result[v] %= mod
            return result
        result = rec(0,0)
        return result[0]
