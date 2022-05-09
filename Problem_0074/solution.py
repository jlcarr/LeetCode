class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search rows
        L,R = 0, len(matrix)
        while L+1<R:
            M = (R+L)//2
            if matrix[M][0] == target:
                return True
            if matrix[M][0] < target:
                L = M
            else:
                R = M
        row = L
        
        if matrix[row][0] > target:
            return False
        
        # search columns
        L,R = 0, len(matrix[row])
        while L+1<R:
            M = (R+L)//2
            if matrix[row][M] == target:
                return True
            if matrix[row][M] < target:
                L = M
            else:
                R = M
        return matrix[row][L] == target
