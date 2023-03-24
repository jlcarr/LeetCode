class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        G = {i:set() for i in range(n)}
        Gcomp = {i:set() for i in range(n)}
        for a,b in connections:
            G[a].add(b)
            Gcomp[b].add(a)
        q = [0]
        searched = set(q)
        result = 0
        while q:
            curr = q.pop()
            for neighbor in list(G[curr] | Gcomp[curr]):
                if neighbor not in searched:
                    if neighbor in G[curr]:
                        result += 1
                        #print(curr, neighbor)
                    q.append(neighbor)
                    searched.add(neighbor)
        return result
