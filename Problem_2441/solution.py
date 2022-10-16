class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        return max([i for i in nums if -i in s]+[-1])
