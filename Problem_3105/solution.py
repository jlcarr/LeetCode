class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result = 1
        dec, inc = 1, 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc += 1
                dec = 1
            elif nums[i] > nums[i+1]:
                inc = 1
                dec += 1
            else:
                inc = 1
                dec = 1
            result = max(result, inc, dec)
        return result
