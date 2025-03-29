import heapq
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        q = sorted(set(queries))
        qmap = dict()
        m,n = len(grid),len(grid[0])
        reached = set()
        seen = set([(0,0)])
        boundary = [(grid[0][0], 0,0)]
        for vmax in q:
            while boundary and boundary[0][0] < vmax:
                _, i,j = heapq.heappop(boundary)
                if grid[i][j] < vmax:
                    reached.add((i,j))
                    for ip,jp in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if (0 <= ip < m) and (0 <= jp < n) and (ip,jp) not in seen:
                            seen.add((ip,jp))
                            heapq.heappush(boundary, (grid[ip][jp], ip,jp))
            qmap[vmax] = len(reached)
        return [qmap[i] for i in queries]
