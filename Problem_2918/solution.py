class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(i + (i==0) for i in nums1)
        sum2 = sum(i + (i==0) for i in nums2)
        if (sum1 < sum2 and 0 not in nums1) or (sum2 < sum1 and 0 not in nums2):
            return -1
        return max(sum1, sum2)
