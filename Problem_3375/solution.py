class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        m = min(nums)
        if m < k:
            return -1
        return len(nums) - int(m == k)

