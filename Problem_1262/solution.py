class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # rem 1: smallest rem 1 or 2 smallest rem 2
        # rem 2: rallest rem 2 or 2 smallest rem 1
        s = sum(nums)
        rem = s % 3
        if rem == 0:
            return s
        rem1 = sorted(filter(lambda x: x%3 == 1, nums))
        rem2 = sorted(filter(lambda x: x%3 == 2, nums))
        if rem == 1:
            result = -1
            if rem1:
                result = max(result, s - rem1[0])
            if len(rem2) >= 2:
                result = max(result, s - rem2[0] - rem2[1])
            return result
        if rem == 2:
            result = -1
            if rem2:
                result = max(result, s - rem2[0])
            if len(rem1) >= 2:
                result = max(result, s - rem1[0] - rem1[1])
            return result
        return -1
