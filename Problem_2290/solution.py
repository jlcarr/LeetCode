import heapq
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # Dijkstra
        m, n = len(grid), len(grid[0])

        q = [(0,0,0)]
        searched = set([(0,0)])
        while q:
            cost, i,j = heapq.heappop(q)
            for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if not (0 <= ii < m) or not (0 <= jj < n) or (ii,jj) in searched:
                    continue
                if (ii,jj) == (m-1,n-1):
                    return cost
                searched.add((ii,jj))
                heapq.heappush(q,(cost+grid[ii][jj], ii, jj))
        return -1


