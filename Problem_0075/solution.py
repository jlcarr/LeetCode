class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rwb = [0,0,0]
        for c in nums:
            rwb[c] +=1 
        for i in range(len(nums)):
            if i < rwb[0]:
                nums[i] = 0
            elif i < rwb[0] + rwb[1]:
                nums[i] = 1
            else:
                nums[i] = 2
