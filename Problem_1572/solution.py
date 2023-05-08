class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        return sum(mat[i][i]+mat[i][n-1-i] for i in range(n)) - (n%2)*(mat[n//2][n//2])
        
