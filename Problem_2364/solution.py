from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        offsets = defaultdict(int)
        for j,v in enumerate(nums):
            offs = j-v
            result += offsets[offs]
            offsets[offs] += 1
        return n*(n-1)//2 - result
