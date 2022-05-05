class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            v = nums[i]
            temp = self.permute(nums[:i] + nums[i+1:])
            temp = [[v]+p for p in temp]
            result += temp
        return result
            
