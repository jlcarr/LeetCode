class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for v in nums:
            if v == original:
                original *= 2
        return original
