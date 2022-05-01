class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        if not nums:
            return result
        
        # First find first occurance
        L,R = 0, len(nums)-1
        while L+1<R and nums[L] != target:
            M = (L+R)//2
            #print(L,M,R)
            if nums[M] >= target:
                R = M
            else:
                L = M
        if nums[L] == target:
            result[0] = L
        elif nums[R] == target:
            result[0] = R
        #print(result)

        # Second find last occurance
        L,R = 0, len(nums)-1
        while L+1<R and nums[R] != target:
            M = (L+R)//2
            if nums[M] <= target:
                L = M
            else:
                R = M
        if nums[R] == target:
            result[1] = R
        elif nums[L] == target:
            result[1] = L
        #print(result)
        
        return result
