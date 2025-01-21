class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # remap
        m,n = len(mat),len(mat[0])
        remap = [None] * len(arr)
        for i,row in enumerate(mat):
            for j,c in enumerate(row):
                remap[c-1] = (i,j)
        # rowcount
        rowcounts = [0] * m
        colcounts = [0] * n
        for index,v in enumerate(arr):
            i,j = remap[v-1]
            rowcounts[i] += 1
            colcounts[j] += 1
            if rowcounts[i] == n or colcounts[j] == m:
                return index
        return -1
