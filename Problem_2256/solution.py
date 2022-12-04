import math
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        result = 0
        min_avg_diff = sum([abs(i) for i in nums])
        n = len(nums)
        cum_start, cum_end = 0, sum(nums)
        for i in range(n):
            cum_start += nums[i]
            cum_end -= nums[i]
            avg_start = int(math.floor(cum_start/(i+1)))
            avg_end = 0
            if i < n-1:
                avg_end = int(math.floor(cum_end/(n-i-1)))
            #print(avg_start,avg_end)
            avg_diff = abs(avg_start-avg_end)
            if avg_diff < min_avg_diff:
                min_avg_diff = avg_diff
                result = i
        return result
