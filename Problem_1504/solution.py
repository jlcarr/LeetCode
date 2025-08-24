class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        for i in range(m):
            for j in range(1, n):
                if mat[i][j]:
                    mat[i][j] += mat[i][j-1] 
        #print(mat)
        result = 0
        for i in range(m):
            for j in range(n):
                h = 0
                w = n
                while i-h >= 0 and (w := min(w, mat[i-h][j])) > 0:
                    result += w
                    h += 1
        return result
                


