import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        G = {i:dict() for i in range(n)}
        for u,v,w in edges:
            G[u][v] = w
            G[v][u] = w
        
        result = 0
        result_count = n
        for i in range(n):
            #print("Search", i)
            q = [(0,i)]
            searched = {i:0}
            while q:
                dist,u = heapq.heappop(q)
                if dist > searched[u]:
                    continue
                #print("- at",u)
                for v,w in G[u].items():
                    #print("-- to", v, dist+w)
                    if (v not in searched or searched[v] > dist+w) and dist+w <= distanceThreshold:
                        searched[v] = dist+w
                        heapq.heappush(q, (dist+w,v))
            #print(f"Result", i, searched)
            if len(searched)-1 <= result_count:
                result = i
                result_count = len(searched)-1
        return result
                    
