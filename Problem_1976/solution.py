import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        G = {i:dict() for i in range(n)}
        for u,v,t in roads:
            G[u][v] = t
            G[v][u] = t

        q = [(0,0)]
        costs = {0:0}
        counts = {0:1}
        while q:
            cost,curr = heapq.heappop(q)
            if costs[curr] < cost:
                continue
            for v,t in G[curr].items():
                if v not in costs or costs[v] > cost + t:
                    costs[v] = cost + t
                    counts[v] = counts[curr]
                    heapq.heappush(q, (cost + t, v))
                elif costs[v] == cost + t:
                    counts[v] = (counts[v] + counts[curr]) % mod
        return counts[n-1]
