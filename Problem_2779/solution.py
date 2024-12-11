class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 1
        l = 0
        window = 0
        for r in range(len(nums)):
            while l < r and nums[r] - nums[l] > 2 * k:
                l += 1
            result = max(result, r+1-l)
        return result
