import math
class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        return math.factorial(2*n)//math.factorial(n)//math.factorial(n)//(n+1)
