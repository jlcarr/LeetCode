from functools import cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if all([n < 0 for n in nums1]) and all([n > 0 for n in nums2]):
            return max(nums1) * min(nums2)
        if all([n > 0 for n in nums1]) and all([n < 0 for n in nums2]):
            return min(nums1) * max(nums2)

        @cache
        def rec(i,j):
            if i == len(nums1) or j == len(nums2):
                return 0
            result = 0
            # keep
            result = max(result, result + nums1[i]*nums2[j] + rec(i+1,j+1))
            # skip
            result = max(result, rec(i+1,j))
            result = max(result, rec(i,j+1))

            return result
        
        return rec(0,0)
