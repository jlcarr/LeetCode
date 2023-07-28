class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0, len(arr)-1
        while l < r:
            m = (l + r) // 2
            if arr[m] < arr[m+1]:
                l = m
            elif arr[m-1] > arr[m]:
                r = m
            else:
                l = m
                break
        return l