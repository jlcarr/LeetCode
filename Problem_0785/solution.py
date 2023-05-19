class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [False] * n
        unsearched = set(range(n))
        while unsearched:
            q = [unsearched.pop()]
            while q:
                curr = q.pop()
                color = colors[curr]
                for neighbor in graph[curr]:
                    if neighbor in unsearched:
                        unsearched.remove(neighbor)
                        q.append(neighbor)
                        colors[neighbor] = not color
                    elif colors[neighbor] == color:
                        return False
        return True
