class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        result = 0
        vdecstack = []
        idecstack = []
        for i,v in enumerate(nums):
            if not vdecstack or vdecstack[-1] > v:
                vdecstack.append(v)
                idecstack.append(i)
        for i,v in reversed(list(enumerate(nums))):
            while vdecstack and vdecstack[-1] <= v:
                vdecstack.pop()
                result = max(result, i - idecstack.pop())
            if not vdecstack:
                break
        return result
