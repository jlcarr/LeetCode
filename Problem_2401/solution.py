class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        j = 0
        acc = 0
        result = 0
        for i in range(len(nums)):
            while acc & nums[i]:
                acc &= ~nums[j]
                j += 1
            acc |= nums[i]
            result = max(result, i+1-j)
        return result
