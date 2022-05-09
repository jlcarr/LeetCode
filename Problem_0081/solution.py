class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) <= 2:
            return target in nums
        # find k
        L, R = 0, len(nums)-1
        while L+1 < R:
            M = (R+L)//2
            if target in (nums[L], nums[M], nums[R]):
                return True
            if nums[L] < nums[R]:
                break
            if nums[L] == nums[M] == nums[R]: # go to linear search
                while L+1 < R and nums[R] == nums[M]:
                    R -= 1
            elif nums[L] <= nums[M]:
                L = M
            else:
                R = M
        if nums[0] < nums[-1]:
            k = 0
        elif L > 0 and nums[L] < nums[L-1]:
            k = L
        elif R < len(nums)-1 and nums[R] > nums[R+1]:
            k = R+1
        else:
            k = R
        #print(L,R,k)
        
        # proper binary search, correcting for the rotation
        n = len(nums)
        L, R = 0, len(nums)-1
        while L+1 < R:
            M = (R+L)//2
            #print(L,M,R, (nums[(L+k)%n], nums[(M+k)%n], nums[(R+k)%n]))
            if target in (nums[(L+k)%n], nums[(M+k)%n], nums[(R+k)%n]):
                return True
            if nums[(M+k)%n] < target:
                L = M
            else:
                R = M
        return False
