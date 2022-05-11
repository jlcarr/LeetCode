class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        i = 0
        while i < len(nums):
            count = 1
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                count += 1
                i += 1
            temp = result.copy()
            for j in range(count):
                result += [s+[nums[i]]*(j+1) for s in temp]
            i += 1
            
        return result
