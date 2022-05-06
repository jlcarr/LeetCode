class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        curr = result
        for i in range(1, len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            if curr > result:
                result = curr
        return result
