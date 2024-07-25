class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        nrows,ncols = len(rowSum),len(colSum)
        result = [[0]*ncols for row in range(nrows)]
        for i in range(nrows):
            for j in range(ncols):
                v = min(rowSum[i], colSum[j])
                result[i][j] = v
                rowSum[i] -= v
                colSum[j] -= v
        return result
