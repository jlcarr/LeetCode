class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def perm(nums):
            if len(nums) == 1:
                return [nums]
            result = []
            prev = None
            for i in range(len(nums)):
                if prev is not None and nums[i] == prev:
                    continue
                prev = nums[i]
                
                temp = perm(nums[:i] + nums[i+1:])
                result += [[nums[i]]+p for p in temp]
            return result
        
        return perm(nums)
