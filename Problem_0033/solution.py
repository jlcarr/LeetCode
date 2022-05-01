class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # Find rotation amount
        L, R = 0, n-1
        while L+1 < R:
            M = (L+R)//2
            #print(L,R,M)
            if nums[M] > nums[R]:
                L = M
            elif nums[M] < nums[L]:
                R = M
            else:
                break
        k = 0
        if nums[L] > nums[R]:
            k = R # The true start of the array
        #print(k)
        
        L, R = 0, n-1
        while L+1 < R:
            M = (L+R)//2
            #print(L,R,M)
            L_rot, M_rot, R_rot = (L+k)%n, (M+k)%n, (R+k)%n
            
            if target == nums[M_rot]:
                return M_rot
            if target == nums[L_rot]:
                return L_rot
            if target == nums[R_rot]:
                return R_rot
            
            if target < nums[M_rot]:
                R = M
            elif target > nums[M_rot]:
                L = M
 
        M = (L+R)//2
        L_rot, M_rot, R_rot = (L+k)%n, (M+k)%n, (R+k)%n
        if target == nums[L_rot]:
            return L_rot
        if target == nums[R_rot]:
            return R_rot
        return -1
            
            
            

            
            
