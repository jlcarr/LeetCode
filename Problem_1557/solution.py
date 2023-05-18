class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = set(range(n))
        for head,tail in edges:
            if tail in result:
                result.remove(tail)
        return list(result)
