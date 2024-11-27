import heapq
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        costs = list(range(n))
        G = {i:[i+1] for i in range(n-1)}

        answer = []
        for iq,(u,v) in enumerate(queries):
            G[u].append(v)
            #print(iq,(u,v))
            #print(G)
            if costs[v] <= costs[u] + 1:
                answer.append(costs[-1])
                #print(costs)
                continue
            costs[v] = costs[u] + 1
            if v == n-1:
                answer.append(costs[-1])
                #print(costs)
                continue
            q = [v]
            searched = set(q+[n-1])
            while q:
                curr = heapq.heappop(q)
                for child in G[curr]:
                    if costs[child] > costs[curr] + 1:
                        costs[child] = costs[curr] + 1
                        if child not in searched:
                            searched.add(child)
                            heapq.heappush(q, child)
            answer.append(costs[-1])
            #print(costs)
        return answer
