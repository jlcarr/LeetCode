class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i + 2 < len(nums):
            if nums[i] == nums[i+2]:
                del nums[i]
            else:
                i += 1
