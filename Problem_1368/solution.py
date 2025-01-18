import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = [(0,0,0)]
        costs = {(0,0): 0}
        # (cost, di, dj)
        redirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            cost, i,j = heapq.heappop(q)
            #print(cost, i,j)
            if i == m-1 and j == n-1:
                return cost
            if costs[(i,j)] < cost:
                continue

            for v,(di,dj) in enumerate(redirs):
                newcost = cost + int(v+1 != grid[i][j])
                ip,jp = i+di, j+dj
                if (0 <= ip < m) and (0 <= jp < n) \
                    and ((ip,jp) not in costs or costs[(ip,jp)] > newcost):
                    costs[(ip,jp)] = newcost
                    heapq.heappush(q, (newcost, ip, jp))
        return -1
