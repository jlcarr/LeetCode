class Solution:
    def rob(self, nums: List[int]) -> int:
        result = 0
        for took_first in [True, False]:
            prev, curr = 0,0
            for i,v in enumerate(nums):
                if (i == 0 and took_first) \
                    or (i > 0 and i < len(nums)-1) \
                    or (i == len(nums)-1 and not took_first):
                    prev, curr = curr, max(prev+v, curr)
            result = max(curr, result)
        return result
            
