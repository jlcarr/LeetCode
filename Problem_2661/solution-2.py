class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # remap
        m,n = len(mat),len(mat[0])
        remap = [0] * len(arr)
        for i,v in enumerate(arr):
            remap[v-1] = i
        return min(
            min(max(remap[mat[i][j]-1] for j in range(n)) for i in range(m)),
            min(max(remap[mat[i][j]-1] for i in range(m)) for j in range(n))
            )
