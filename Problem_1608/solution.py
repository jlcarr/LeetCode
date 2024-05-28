class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1
        for ix,v in enumerate(nums):
            if v == prev:
                continue
            x = len(nums)-ix
            #print(ix, x, v, prev, v >= x > prev)
            if v >= x > prev:
                return x
            prev = v
        return -1
