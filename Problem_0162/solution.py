class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (r+l)//2
            if nums[mid] < nums[mid+1]: #increasing
                l = mid+1
            else:
                r = mid
        return l
        
