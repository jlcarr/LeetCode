from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # parse graph
        G = dict()
        for fro,to,price in flights:
            if fro not in G:
                G[fro] = dict()
            if to not in G:
                G[to] = dict()
            G[fro][to] = price
        if src not in G:
            G[src] = dict()
        if dst not in G:
            G[dst] = dict()
        
        start = (src, 0)
        ops = {start: 0}
        q = deque([start])
        while q:
            curr,dist = q.pop()
            if dist-1 == k:
                break
            cost = ops[(curr,dist)]
            for neighbor,n_cost in G[curr].items():
                if (neighbor, dist+1) not in ops:
                    ops[(neighbor, dist+1)] = cost + n_cost
                    q.appendleft((neighbor, dist+1))
                ops[(neighbor, dist+1)] = min(ops[(neighbor, dist+1)], cost + n_cost)
        
        #print(ops)
        #print([ops[(dst, ik)] for ik in range(k+1) if (dst, ik) in ops])
        return min([ops[(dst, ik)] for ik in range(k+2) if (dst, ik) in ops], default=-1)
