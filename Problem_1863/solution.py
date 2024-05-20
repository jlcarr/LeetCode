class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # get bits with any set
        tot = 0
        for i in nums:
            tot |= i
        return tot * (1 << (len(nums)-1))
