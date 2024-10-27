class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])

        left = [[0]*n for irow in range(m)]
        up = [[0]*n for irow in range(m)]
        diag = [[0]*n for row in range(m)]

        for irow in range(m):
            for icol in range(n):
                if matrix[irow][icol] == 0:
                    left[irow][icol] = 0
                    up[irow][icol] = 0
                    diag[irow][icol] = 0
                    continue
                # left
                left[irow][icol] = left[irow][icol-1] + 1 if icol > 0 else 1
                # up
                up[irow][icol] = up[irow-1][icol] + 1 if irow > 0 else 1
                # diag
                v = diag[irow-1][icol-1] + 1 if icol > 0 and irow > 0 else 1
                diag[irow][icol] = min(v, left[irow][icol], up[irow][icol])

        return sum([sum(row) for row in diag])
