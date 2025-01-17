class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        if len(nums2) % 2:
            result = reduce(lambda x,y:x^y, nums1)
        if len(nums1) % 2:
            result ^= reduce(lambda x,y:x^y, nums2)
        return result
