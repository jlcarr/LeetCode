class Solution:
    def averageValue(self, nums: List[int]) -> int:
        l = [i for i in nums if i % 6 == 0]
        if not l:
            return 0
        return int(sum(l)/len(l))
