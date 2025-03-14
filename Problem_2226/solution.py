class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l,r = 0,max(candies)+1
        while l+1 < r:
            cpk = l + (r-l)//2
            if sum(c//cpk for c in candies) < k:
                r = cpk
            else:
                l = cpk
        return l
                
