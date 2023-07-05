class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums.append(0)
        result = 0
        prevrun = 0
        run = 0
        for n in nums:
            if n == 1:
                run += 1
            else:
                result = max(result, run+prevrun)
                prevrun = run
                run = 0
        if result == len(nums)-1:
            return result-1
        return result
