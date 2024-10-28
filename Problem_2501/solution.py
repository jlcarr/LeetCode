class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        curr_streaks = dict()
        prev = -1
        for i in nums:
            if i == prev:
                continue
            v = 1
            if i in curr_streaks:
                v += curr_streaks[i]
            result = max(result, v)
            curr_streaks[i*i] = v
            prev = i
        if result < 2:
            return -1
        return result
