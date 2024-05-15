from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
        q = [(i,j) for i,row in enumerate(grid) for j,val in enumerate(row) if val == 1]
        for i,j in q:
            grid[i][j] = 0
        searched = set(q)
        q = deque(q)
        while q:
            i,j = q.pop()
            for ip,jp in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if (0<=ip<n) and (0<=jp<n) and (ip,jp) not in searched:
                    grid[ip][jp] = grid[i][j] + 1
                    q.appendleft((ip,jp))
                    searched.add((ip,jp))
        
        maxsafe = {(0,0): grid[0][0]}
        q = [(-grid[0][0], 0,0)]
        while q:
            safety, i,j = heapq.heappop(q)
            for ip,jp in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if ip == n-1 and jp == n-1:
                    return min(grid[ip][jp], -safety)
                if (0<=ip<n) and (0<=jp<n) and (ip,jp) not in maxsafe:
                    maxsafe[(ip,jp)] = min(grid[ip][jp], -safety)
                    heapq.heappush(q, (-maxsafe[(ip,jp)], ip, jp))

