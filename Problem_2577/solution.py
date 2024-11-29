import heapq
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        m, n = len(grid), len(grid[0])
        searched = set()
        q = [(0,0,0)]
        while q:
            cost, i,j = heapq.heappop(q)
            for ii,jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if not (0 <= ii < m) or not (0 <= jj < n) or (ii,jj) in searched:
                    continue
                searched.add((ii,jj))
                newcost = max(cost+1, grid[ii][jj] + int((ii+jj) % 2 != grid[ii][jj]%2))
                if (ii,jj) == (m-1,n-1):
                    return newcost
                heapq.heappush(q, (newcost,ii,jj))
        return -2
