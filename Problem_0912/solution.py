class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def rec(l,r):
            if r-l <= 1:
                return
            m = (r+l)//2
            rec(l,m)
            rec(m,r)
            i,j = l,m
            sub_res = []
            while i < m and j < r:
                if nums[i] <= nums[j]:
                    sub_res.append(nums[i])
                    i += 1
                else:
                    sub_res.append(nums[j])
                    j += 1
            while i < m :
                sub_res.append(nums[i])
                i += 1
            while j < r:
                sub_res.append(nums[j])
                j += 1
            for i,n in enumerate(sub_res):
                nums[l+i] = n
        
        rec(0,len(nums))

        return nums
