class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        root = [1] * n
        for u,v in edges:
            root[v] = 0
        if sum(root) != 1:
            return -1
        return root.index(1)
