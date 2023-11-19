class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 1
        nums.sort()
        ilag = 0
        windowsum = 0
        result = 1
        for icurr in range(n):
            windowsum += nums[icurr]
            while k < nums[icurr] * (icurr - ilag + 1) - windowsum:
                windowsum -= nums[ilag]
                ilag += 1
            result = max(result, icurr - ilag + 1)
        return result
