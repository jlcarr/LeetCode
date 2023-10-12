# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        # find middle
        l,r = 0,n-1
        if mountain_arr.get(0) == target:
            return 0
        while l+1 < r:
            m = (r+l)//2
            print(l,r,m)
            mv = mountain_arr.get(m)
            mvp = mountain_arr.get(m+1)
            if mv < mvp:
                l = m
            else:
                r = m
        peak = r
        print(peak)

        # search left
        l,r = 0,peak
        while l+1 < r:
            m = (r+l)//2
            mv = mountain_arr.get(m)
            if mv == target:
                return m

            if mv < target:
                l = m
            else:
                r = m
        if mountain_arr.get(peak) == target:
            return peak
        # search right
        l,r = peak,n
        while l+1 < r:
            m = (r+l)//2
            mv = mountain_arr.get(m)
            if mv == target:
                return m

            if mv > target:
                l = m
            else:
                r = m
        if mountain_arr.get(n-1) == target:
            return n-1
        return -1
