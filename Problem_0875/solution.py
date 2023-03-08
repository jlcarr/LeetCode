class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l,r = 0,max(piles)
        while l+1<r:
            k = (l+r)//2
            if -sum(((-b)//k) for b in piles) > h:
                l = k
            else:
                r = k
        return l+1
