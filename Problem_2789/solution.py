class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        curr = nums.pop()
        result = curr
        while nums:
            if nums[-1] <= curr:
                curr += nums[-1]
            else:
                curr = nums[-1]
            nums.pop()
            result = max(result, curr)
        return result
