class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n-1
        while nums[l] > nums[r] and l+1<r:
            m = (l+r)//2
            if nums[m] >= nums[l]:
                l = m
            if nums[m] <= nums[r]:
                r = m
        #print(l,r)
        if nums[l] == nums[r]:
            return min(nums[l:r+1])
        return min(nums[l], nums[r])
