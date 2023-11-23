class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for lv,rv in zip(l,r):
            result.append(True)
            if rv - lv <= 1:
                continue
            s = sorted(nums[lv:rv+1])
            d = s[1] - s[0]
            for i in range(rv-lv):
                if s[i+1]-s[i] != d:
                    result[-1] = False
                    break
        return result
