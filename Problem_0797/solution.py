from functools import cache
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        @cache
        def rec(i):
            if i == n-1:
                return [[n-1]]
            result = []
            for j in graph[i]:
                sub_res = rec(j)
                result += [[i]+p for p in sub_res]
            return result
        
        return rec(0)
