from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
