import math
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # construct the graph
        G = {0:set()}
        for a,b in roads:
            if a not in G:
                G[a] = set()
            if b not in G:
                G[b] = set()
            G[a].add(b)
            G[b].add(a)

        def rec(curr, prev):
            tot = 1
            result = 0
            for neighbor in G[curr]:
                if neighbor == prev:
                    continue
                sub_tot, sub_result = rec(neighbor, curr)
                result += sub_result
                tot += sub_tot
            if curr != 0:
                result += int(math.ceil(tot / seats))
            #print(curr, prev, tot, result)
            return tot, result
        
        _, result = rec(0, -1)
        return result
