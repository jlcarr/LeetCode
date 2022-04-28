class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        total = len(nums1)+len(nums2)
        target = total//2
        
        if nums1 and nums2:
            min_val = min(nums1[0], nums2[0])
            max_val = max(nums1[-1], nums2[-1])
        elif nums1:
            min_val = nums1[0]
            max_val = nums1[-1]
        elif nums2:
            min_val = nums2[0]
            max_val = nums2[-1]
        
        # binary search on the longer array
        L, R = -1, len(nums1)
        while True:
            M = (R+L)//2
            complement = target - M - 2
            
            nums1_lower = nums1[M] if M >= 0 else min_val-1
            nums1_upper = nums1[M+1] if M+1 < len(nums1) else max_val+1
            nums2_lower = nums2[complement] if complement >= 0 else min_val-1
            nums2_upper = nums2[complement+1] if complement+1 < len(nums2) else max_val+1
            
            #print("L R M c", L, R, M, complement)
            #print(nums1_lower, nums1_upper, nums2_lower, nums2_upper)
            
            if nums1_lower <= nums2_upper and nums1_upper >= nums2_lower:
                if total%2:
                    return min(nums1_upper, nums2_upper)
                else:
                    return (max(nums1_lower,nums2_lower) + min(nums1_upper, nums2_upper)) /2
            elif nums1_lower >= nums2_upper:
                R = M-1
            else:
                L = M+1
