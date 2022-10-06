class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        curr_prod = 1
        r = 0
        l = 0
        while r < len(nums):
            if nums[r] >= k:
                curr_prod = 1
                r += 1
                l = r
                continue
            curr_prod *= nums[r]
            while curr_prod >= k:
                curr_prod //= nums[l]
                l += 1
            result += 1 + r - l
            r += 1
        return result
