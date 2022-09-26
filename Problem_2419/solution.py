class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        result = 0
        sub_res = 0
        for i in nums:
            if m & i == m:
                sub_res += 1
            else:
                sub_res = 0
            result = max(result, sub_res)
        return result
