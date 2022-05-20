class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        L, R = 0, len(nums)-1
        while L+1 < R:
            M = (R+L)//2
            if nums[M] > nums[L]:
                L = M
            else:
                R = M
        return nums[R]
