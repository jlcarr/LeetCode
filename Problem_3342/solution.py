import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m = len(moveTime), len(moveTime[0])
        searched = set([(0,0)])
        q = [(0,0,0)]
        while q:
            t, i,j = heapq.heappop(q)
            for ip,jp in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if not (0 <= ip < n) or not (0 <= jp < m) or (ip,jp) in searched:
                    continue
                tp = max(t, moveTime[ip][jp]) + 1 + (i+j)%2
                if (ip,jp) == (n-1, m-1):
                    return tp
                searched.add((ip,jp))
                heapq.heappush(q, (tp,ip,jp))
        return -1
