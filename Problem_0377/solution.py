from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(t):
            result = 0
            for i in nums:
                if i == t:
                    result += 1
                elif i < t:
                    result += dp(t-i)
            return result
            
        return dp(target)
