class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        acc = 0
        result = []
        for i in nums:
            acc = (acc << 1) + i
            result.append(acc % 5 == 0)
        return result
