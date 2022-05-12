from functools import cache
class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        result = 2 *  self.numTrees(n-1)
        for i in range(1,n-1):
            result += self.numTrees(i) * self.numTrees(n-1-i)
        return result
