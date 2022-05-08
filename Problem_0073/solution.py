class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        found = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    found.append((i,j))
        
        for row,col in found:
            for i in range(m):
                matrix[i][col] = 0
            for j in range(n):
                matrix[row][j] = 0
