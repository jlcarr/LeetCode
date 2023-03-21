class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        streak = 0
        for i in nums:
            if i == 0:
                streak += 1
            else:
                result += streak * (streak+1) // 2
                streak = 0
        result += streak * (streak+1) // 2
        return result
