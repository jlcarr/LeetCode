class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        G = {i:[] for i in range(n)}
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)

        stack = [source]
        searched = set(stack)
        while stack:
            u = stack.pop()
            for v in G[u]:
                if v == destination:
                    return True
                if v not in searched:
                    stack.append(v)
                    searched.add(v)
        return False
