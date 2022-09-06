class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search for closest to x
        l,r = 0, len(arr)-1
        while l+1 < r:
            mid = (r+l)//2
            if arr[mid] <= x:
                l = mid
            else:
                r = mid
        #print(l,r)
        
        # correct off-by-one by bumping to the closest
        if abs(arr[l] - x) > abs(arr[r] - x):
            l = r
        r = l+1

        # grow linearly to grab k
        while r - l < k:
            if l <= 0:
                r = k
                break
            if r >= len(arr):
                l = r-k
                break
            if abs(arr[l-1] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
            
        return arr[l:r]
