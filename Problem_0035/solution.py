class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)-1
        while L+1<R:
            M = (L+R)//2
            if nums[M] < target:
                L = M
            elif nums[M] > target:
                R = M
            else:
                return M
        #print(L,R)
        if target > nums[R]:
            return R+1
        if target <= nums[L]:
            return L
        return L+1
                
