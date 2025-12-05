class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return (1 - (sum(nums) % 2)) * (len(nums)-1)
