class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # first remove extraneous data in-place
        i = 0
        while i < len(nums):
            if nums[i] <= 0:
                del nums[i]
            else:
                i += 1
        #print("filtered", nums)
                
        # next place number in their 1-base position if possible
        for i in range(len(nums)):
            #print("upped", nums, i, nums[i]-1 < len(nums))
            while nums[i]-1 < i:
                #print("pre", nums[i], nums[nums[i]-1])
                if nums[nums[i]-1] == nums[i]:
                    break
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
                #print("post", nums[i], nums[nums[i]-1])
        #print("sorted", nums)
                
        # Finally search for the answer
        i = 1
        while i <= len(nums):
            if nums[i-1] != i:
                return i
            i += 1
        return i
