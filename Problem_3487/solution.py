class Solution:
    def maxSum(self, nums: List[int]) -> int:
        uniques = set(filter(lambda x: x > 0, nums))
        if not uniques:
            return max(nums)
        return sum(uniques)
