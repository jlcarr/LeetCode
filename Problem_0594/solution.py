class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = 0
        result = 0
        while j < len(nums):
            while nums[i]+1 < nums[j]:
                i += 1
            if nums[i]+1 == nums[j]:
                result = max(result, j+1 - i)
            j += 1
        return result
