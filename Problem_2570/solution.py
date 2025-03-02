class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i1 = 0
        i2 = 0
        result = []
        while i1 < len(nums1) or i2 < len(nums2):
            if i2 == len(nums2) or (i1 < len(nums1) and nums1[i1][0] < nums2[i2][0]):
                result.append(nums1[i1])
                i1 += 1
            elif i1 == len(nums1) or nums1[i1][0] > nums2[i2][0]:
                result.append(nums2[i2])
                i2 += 1
            else:
                result.append([nums1[i1][0], nums1[i1][1] + nums2[i2][1]])
                i1 += 1
                i2 += 1
        return result
