from functools import cache
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.graph = {i:[] for i in range(n)}
        for e in edges:
            self.graph[e[1]].append(e[0])
        @cache
        def dfs(i):
            result = set(self.graph[i])
            for j in self.graph[i]:
                result |= dfs(j)
            return result
        return [sorted(dfs(i)) for i in range(n)]

