import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        q = []
        for l,r in intervals:
            if q and q[0] < l:
                heapq.heappop(q)
            heapq.heappush(q, r)
        return len(q)
