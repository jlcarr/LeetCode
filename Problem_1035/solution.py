from functools import cache
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2 = len(nums1),len(nums2)

        n2indices = {}
        for index,n2 in enumerate(nums2):
            if n2 not in n2indices:
                n2indices[n2] = []
            n2indices[n2].append(index)

        @cache
        def rec(i1,i2):
            if i1 == l1 or i2 == l2:
                return 0
            result = 0
            if nums1[i1] in n2indices:
                for i2_new in n2indices[nums1[i1]]:
                    if i2_new >= i2:
                        result = max(result, 1 + rec(i1+1, i2_new+1))
            result = max(result, rec(i1+1, i2))
            return result
        return rec(0,0)
