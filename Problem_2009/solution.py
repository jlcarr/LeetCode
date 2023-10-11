import bisect
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = len(nums)
        nums = sorted(set(nums))
        result = l
        for i,num in enumerate(nums):
            j = bisect.bisect_left(nums, num+l)
            result = min(result, l - (j-i))
        return result
