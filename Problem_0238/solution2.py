class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        acc = 1
        for i,v in enumerate(nums):
            result[i] = acc
            acc *= v
        acc = 1
        for i,v in enumerate(nums[::-1]):
            result[len(nums)-1-i] *= acc
            acc *= v
        return result
