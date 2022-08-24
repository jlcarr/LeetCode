class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        
        for i in range(m):
            l, r = 0, n-1
            if matrix[i][l] > target:
                return False
            if matrix[i][r] < target:
                continue
            if matrix[i][l] == target or matrix[i][r] == target:
                return True
            while l < r:
                #print(i, l , r)
                mid = (l+r)//2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] < target:
                    l = mid + 1
                else:
                    r = mid
                    
        return False
