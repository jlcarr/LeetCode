from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        @cache
        def dp(i, target):
            if i == len(nums):
                return int(target == 0)
            n = self.nums[i]
            return dp(i+1, target-n) + dp(i+1, target+n)
        
        return dp(0, target)
