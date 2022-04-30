class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find a preceeding higher value, put the rest in sorted order
        max_prev = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < max_prev: # found
                # find the true swap
                swap_val, i_swap = min([(nums[j], j) for j in range(i+1,len(nums)) if nums[j] > nums[i]])
                #print(i)
                nums[i],nums[i_swap], = swap_val,nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return
            elif nums[i] > max_prev:
                max_prev = nums[i]
                i_max_prev = i
        
        nums[:] = sorted(nums)
