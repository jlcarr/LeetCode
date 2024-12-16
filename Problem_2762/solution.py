import heapq
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 0
        maxq = []
        minq = []
        l = 0
        for r,v in enumerate(nums):
            heapq.heappush(maxq, (-v,r))
            heapq.heappush(minq, (v,r))
            while -maxq[0][0] - minq[0][0] > 2:
                l += 1
                while maxq[0][1] < l:
                    heapq.heappop(maxq)
                while minq[0][1] < l:
                    heapq.heappop(minq)
            lr = r+1-l
            result += lr
            #print(l,r, result, maxq, minq)
        return result
