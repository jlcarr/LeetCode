class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(nums[-4+i] - nums[i] for i in range(4))

