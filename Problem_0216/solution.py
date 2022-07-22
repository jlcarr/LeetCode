from functools import cache
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        @cache
        def dp(k, n, i):
            if k == 0 and n == 0: #found solution
                return [[]]
            if k == 0 or n == 0 or i == 10 or i > n: # didn't find solution
                return []
            # without i
            result = dp(k,n,i+1)
            # with i
            if i <= n:
                sub_result = dp(k-1, n-i, i+1)
                result = result + [[i] + comb for comb in sub_result]
            return result
        
        return dp(k, n, 1)
