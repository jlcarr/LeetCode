class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l,r = 0,len(nums)
        while r-l > 1:
            m = (r+l)//2
            m -= m%2
            #print(l,r,m)
            if nums[m] == nums[m+1]:
                l = m+2
            else:
                r = m+1
        #print(l,r)
        return nums[l]
