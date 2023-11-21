from collections import Counter
import math
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        return sum(
            math.comb(v,2)
            for v in Counter([num - int(str(num)[::-1]) for num in nums]).values()
            if v >= 2
        ) % (10**9 + 7)
